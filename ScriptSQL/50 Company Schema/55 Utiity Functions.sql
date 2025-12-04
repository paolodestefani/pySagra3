--
-- **************************
-- ** APPLICATION DATABASE **
-- **************************
--

-- Paolo De Stefani 01.2025

-- This script MUST be executed by postgres user or a postgres like user
-- Connected to a database ("postgres" database is OK)

---------------------------------
-- APPLICATION DB ARCHITECTURE --
---------------------------------

-- * one database {pyAppPgDataBase}
-- * one role that own the database {pyAppPgOwnerRole} without login privilege
-- * one login role {pyAppPgLoginRole} that inherit {pyAppPgOwnerRole} privileges

-- Every database has 4 schemas:
-- * system     for system objects
-- * common     for common objects that are shared with all companies
-- * company    for objects associated with a company
-- * temp       for temporary tables

-- This set of variables will be be resolved before executing the scripts:
-- {pyAppPgOwnerRole}           = PostgresSQL Role that own all db objects without login privilege
-- {pyAppPgDataBase}            = Postgres database name
-- {pyAppPgLoginRole}           = PostgresSQL Role used for standard login users
-- {pyAppPgLoginPassword}       = Password for pyAppPgLoginRole
-- {pyAppName}                  = Python application name
-- {pyAppDescription}           = Python application description
-- {pyAppVersionMajor}          = Application version major number
-- {pyAppVersionMinor}          = Application version minor number
-- {pyAppVersionPatch}          = Application version patch number
-- {pyAppVersionTag}            = Application version tag
-- {pyAppVersionDescription}    = Application version description
-- {pyAppPgDataBaseTS}          = Database table space (MUST be created before script execution)
-- {pyAppPgTablesTS}            = Tables table space (MUST be created before script execution)
-- {pyAppPgIndexesTS}           = Indexes table space (MUST be created before script execution)


---------------------------
-- COMMON SCHEMA OBJECTS --
---------------------------

SET search_path = company;


-- delete orders utility function
CREATE FUNCTION delete_event_order(in_event int) 
RETURNS VOID AS
$$
BEGIN
	-- delete event orders
	DELETE FROM company.order_header 
    WHERE event_id = in_event; -- event include company
	-- stock inventory update
	UPDATE company.stock_inventory 
    SET unloaded = 0 
    WHERE event_id = in_event; -- event include company
	-- delete from stock unload
	DELETE FROM company.stock_unload 
    WHERE event_id = in_event; -- event include company
	-- delte from numbering
	DELETE FROM company.numbering 
    WHERE event_id = in_event; -- event include company
END;
$$ 
LANGUAGE plpgsql;
COMMENT ON FUNCTION delete_event_order(int) IS
    'Function for delete all orders';
ALTER FUNCTION delete_event_order(in_event int) 
    OWNER TO {pyAppPgOwnerRole};


-- unloads rebuild on stock_inventory utility function
CREATE FUNCTION unload_rebuild(in_event int) 
RETURNS VOID AS
$$
DECLARE
    odr RECORD; -- order detail dep record
    ity char; -- item tpe
    ipr integer; -- item part
    qty numeric(12, 2); -- quantity
BEGIN
    -- clear stock inventory and stock unload
    UPDATE company.stock_inventory 
    SET unloaded = 0 
    WHERE event_id = in_event; -- event include company
    DELETE FROM company.stock_unload 
    WHERE event_id = in_event; -- event include company
    -- loop trough details deps records
    FOR odr IN
        SELECT company_id, event_id, event_date, day_part, item_id, quantity
        FROM company.order_line_department
        WHERE event_id = in_event -- event include company
    LOOP
        -- find item type and item unload control
        SELECT item_type INTO ity 
        FROM company.item 
        WHERE item_id = odr.item_id; -- item include company
        -- for kit items
        IF ity = 'K' THEN 
            FOR ipr, qty IN 
                SELECT ip.part_id, ip.quantity
                FROM company.item_part ip
                WHERE ip.item_id = odr.item_id -- don't need to check item type as an item id can not be kit and menu 
            LOOP
                -- stock inventory
                UPDATE company.stock_inventory 
                SET unloaded = unloaded + odr.quantity * qty
                WHERE event_id = in_event -- event include company
                    AND item_id = ipr; -- don't need to check has_stock_control as only record already in table are updated
                -- stock unload
                -- initialize values on not present/change day/change daypart
                IF NOT EXISTS(  SELECT stock_unload_id 
                                FROM company.stock_unload 
                                WHERE event_id = odr.event_id -- event include company 
                                    AND event_date = odr.event_date 
                                    AND day_part = odr.day_part 
                                    AND item_id = ipr) THEN
                    INSERT INTO company.stock_unload (company_id, event_id, event_date, day_part, item_id) 
                    VALUES (odr.company_id, odr.event_id, odr.event_date, odr.day_part, ipr);
                END IF;
                -- update unload
                UPDATE company.stock_unload
                SET unloaded = unloaded + odr.quantity * qty
                WHERE event_id = odr.event_id 
                    AND event_date = odr.event_date 
                    AND day_part = odr.day_part 
                    AND item_id = ipr;
            END LOOP;
        -- for normal items
        ELSE
            -- stock inventory
            UPDATE company.stock_inventory 
            SET unloaded = unloaded + odr.quantity
            WHERE event_id = in_event 
                AND item_id = odr.item_id; -- don't need to check has_stock_control as only record already in table are updated
            -- stock unload
            -- initialize values on not present/change day/change daypart
            IF NOT EXISTS(  SELECT stock_unload_id 
                            FROM company.stock_unload 
                            WHERE event_id = odr.event_id 
                                AND event_date = odr.event_date 
                                AND day_part = odr.day_part 
                                AND item_id = odr.item_id) THEN
                INSERT INTO company.stock_unload (company_id, event_id, event_date, day_part, item_id) 
                VALUES (odr.company_id, odr.event_id, odr.event_date, odr.day_part, odr.item_id);
            END IF;
            -- update unload
            UPDATE company.stock_unload
            SET unloaded = unloaded + odr.quantity
            WHERE event_id = odr.event_id 
                AND event_date = odr.event_date 
                AND day_part = odr.day_part 
                AND item_id = odr.item_id;
        END IF;
    END LOOP;
END;
$$ 
LANGUAGE plpgsql;
COMMENT ON FUNCTION unload_rebuild(int) IS
    'Function for unload rebuild';
ALTER FUNCTION unload_rebuild(in_event int) 
    OWNER TO {pyAppPgOwnerRole};


-- numbering rebuild utility function
CREATE FUNCTION numbering_rebuild(in_event int) 
RETURNS VOID AS
$$
DECLARE 
    odh         RECORD; -- order header record
    num         int;
    lunch_time  time;
    dinner_time time;  
    i           integer; 
BEGIN
    -- clear old values
    DELETE FROM company.numbering 
    WHERE event_id = in_event; -- event include company
    -- update identity
	i := (SELECT coalesce(max(numbering_id), 0) + 1 FROM company.numbering);
	EXECUTE format('ALTER TABLE company.numbering ALTER COLUMN numbering_id RESTART WITH %s', i);
    -- loop trough details deps records
    FOR odh IN
        SELECT company_id, event_id, order_number, stat_order_date, stat_order_day_part
        FROM company.order_header
        WHERE event_id = in_event
    LOOP
        -- update current order number if > of the previous, create a record if not present
        num := (SELECT current_value 
                FROM company.numbering 
                WHERE sequence_type = 'ORDERNUM' 
                AND event_id = in_event);
        IF num IS NULL THEN
            INSERT INTO company.numbering (company_id, sequence_type, event_id, current_value) 
            VALUES (odh.company_id, 'ORDERNUM', odh.event_id, 0);
            num := 0;
        END IF;
        IF odh.order_number > num THEN
            UPDATE company.numbering 
            SET current_value = odh.order_number 
            WHERE sequence_type = 'ORDERNUM' 
                AND event_id = in_event;
        END IF;
        -- update/insert orders count
        /*IF NOT EXISTS(  SELECT current_value 
                        FROM company.numbering 
                        WHERE sequence_type = 'ORDERS' 
                            AND event_id = in_event 
                            AND event_date = odh.stat_order_date 
                            AND day_part = odh.stat_order_day_part) THEN
            INSERT INTO company.numbering (company_id, sequence_type, event_id, event_date, day_part, current_value) 
            VALUES (odh.company_id, 'ORDERS', odh.event_id, odh.stat_order_date, odh.stat_order_day_part, 1);
        ELSE 
            UPDATE company.numbering 
            SET current_value = current_value + 1 
            WHERE sequence_type = 'ORDERS' 
                AND event_id = odh.event_id 
                AND event_date = odh.stat_order_date 
                AND day_part = odh.stat_order_day_part;
        END IF;*/
    END LOOP;
END;
$$ 
LANGUAGE plpgsql;
COMMENT ON FUNCTION numbering_rebuild(int) IS
    'Function for numbering rebuild';
ALTER FUNCTION numbering_rebuild(in_event int) 
    OWNER TO {pyAppPgOwnerRole};


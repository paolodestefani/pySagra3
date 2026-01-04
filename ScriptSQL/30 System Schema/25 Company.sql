--
-- **************************
-- ** APPLICATION DATABASE **
-- **************************
--

-- Paolo De Stefani 10.2018

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

-- This set of variables MUST be resolved before executing the scripts:
-- {pyAppPgOwnerRole} = PostgresSQL Role that own all db objects without login privilege
-- {pyAppPgDataBase} = Postgres database name
-- {pyAppPgLoginRole} = PostgresSQL Role used for standard login users
-- {pyAppPgLoginPassword} = Password for pyAppPgLoginRole
-- {pyAppName} = Python application name
-- {pyAppDescription} = Python application description
-- {pyAppVersion} = Application release version
-- {pyAppPgDataBaseTS} = Database table space (MUST be created before script execution)
-- {pyAppPgTablesTS} = Tables table space (MUST be created before script execution)
-- {pyAppPgIndexesTS} = Indexes table space (MUST be created before script execution)


---------------------------
-- SYSTEM SCHEMA OBJECTS --
---------------------------

SET search_path = system;


-- system table: companies
CREATE TABLE company (
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          integer NOT NULL,
    --
    company_id              integer,
    description             text NOT NULL,
    company_image           bytea,
    is_system_object        boolean NOT NULL DEFAULT False,
    --
    CONSTRAINT company_pk 
        PRIMARY KEY (company_id) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS}
)
TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE company IS 
    '{pyAppName} companies table and companies'' settings';
ALTER TABLE company 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON company 
    FOR EACH ROW EXECUTE PROCEDURE update_company_user_date();


-- system function: create company 
CREATE FUNCTION system.pa_company_create( new_id int,
                                          new_description text,
                                          new_system_object boolean,
                                          new_company_image bytea)
RETURNS void AS
$$
BEGIN
	-- check if company id already exists
	IF EXISTS(
                SELECT company_id 
                FROM system.company 
                WHERE company_id = new_id) THEN
		RAISE EXCEPTION 'Company ID % already exists', new_id USING HINT = 'Try a different company ID', ERRCODE = 'PA012';
	END IF;
	-- create company reference on system.company
	INSERT INTO system.company (company_id, description, is_system_object, company_image) 
	VALUES (new_id, new_description, new_system_object, new_company_image);
    -- create company settings for th new company
	INSERT INTO company.setting (company_id) 
	VALUES (new_id);
END;
$$
LANGUAGE plpgsql;
COMMENT ON FUNCTION pa_company_create(int, text, boolean, bytea) IS 
    'Function for create a new company';
ALTER FUNCTION pa_company_create(int, text, boolean, bytea) 
    OWNER TO {pyAppPgOwnerRole};


-- system function: drop company 
CREATE FUNCTION pa_company_drop(in_company int) 
RETURNS void AS
$$
DECLARE
i integer;
t text[];
BEGIN
	-- check if company is in use
	IF EXISTS(
                SELECT company_id 
                FROM system.connection 
                WHERE company_id = in_company) THEN
		RAISE EXCEPTION 'Can not drop company % because it is in use', in_company
        USING HINT = 'Disconnect users from this company', ERRCODE = 'PA013';
	END IF;
	-- delete some table first, shoul be faster
	DELETE FROM company.items_ordered_delivered WHERE company_id = in_company;
	DELETE FROM company.items_inventory WHERE company_id = in_company;
	-- disable triggers
	ALTER TABLE company.order_line_department DISABLE TRIGGER t10_order_line_to_inventory;
    ALTER TABLE company.order_line_department DISABLE TRIGGER t20_order_line_to_ordered_delivered;
	ALTER TABLE company.order_line_department DISABLE TRIGGER t99_update_company_user_date;
	ALTER TABLE company.order_line DISABLE TRIGGER t99_update_company_user_date;
	ALTER TABLE company.order_header_department DISABLE TRIGGER t10_update_order_header_department;
	ALTER TABLE company.order_header_department DISABLE TRIGGER t99_update_company_user_date;
	ALTER TABLE company.order_header DISABLE TRIGGER t10_update_numbering;
	ALTER TABLE company.order_header DISABLE TRIGGER t99_update_company_user_date;
	
    -- delete company record
	DELETE FROM system.company WHERE company_id = in_company;
	
    -- ri-enable triggers
	ALTER TABLE company.order_line_department ENABLE TRIGGER t10_order_line_to_inventory;
    ALTER TABLE company.order_line_department ENABLE TRIGGER t20_order_line_to_ordered_delivered;
	ALTER TABLE company.order_line_department ENABLE TRIGGER t99_update_company_user_date;
	ALTER TABLE company.order_line ENABLE TRIGGER t99_update_company_user_date;
	ALTER TABLE company.order_header_department ENABLE TRIGGER t10_update_order_header_department;
	ALTER TABLE company.order_header_department ENABLE TRIGGER t99_update_company_user_date;
	ALTER TABLE company.order_header ENABLE TRIGGER t10_update_numbering;
	ALTER TABLE company.order_header ENABLE TRIGGER t99_update_company_user_date;
	-- update identity
	FOREACH t SLICE 1 IN ARRAY ARRAY[
		['system.connection_history', 'history_id'],
		['company.cash_desk', 'cash_desk_id'],
		['company.department', 'department_id'],
		['company.event', 'event_id'],
		['company.item', 'item_id'],
		['company.item_part', 'item_part_id'],
		['company.item_variant', 'item_variant_id'],
		['company.numbering', 'numbering_id'],
		['company.order_header', 'order_header_id'],
		['company.order_header_department', 'order_header_department_id'],
		['company.order_line', 'order_line_id'],
		['company.order_line_department', 'order_line_department_id'],
		['company.price_list', 'price_list_id'],
		['company.price_list_item', 'price_list_item_id'],
		['company.printer_class', 'printer_class_id'],
		['company.printer_class_printer', 'printer_class_printer_id'],
		['company.stand_table', 'stand_table_id'],
		['company.items_inventory', 'items_inventory_id'],
		['company.items_ordered_delivered', 'items_ordered_delivered_id'],
		['company.web_order_header', 'web_order_header_id'],
		['company.web_order_line', 'web_order_line_id']
		] LOOP
		EXECUTE format('SELECT coalesce(max(%s), 0) + 1 FROM %s', t[2], t[1]) INTO i;
		EXECUTE format('ALTER TABLE %s ALTER COLUMN %s RESTART WITH %s', t[1], t[2], i) ;
		--RAISE NOTICE '%', t[2];
	END LOOP;
	-- reindex main tables
	REINDEX TABLE company.order_header;
	REINDEX TABLE company.order_header_department;
	REINDEX TABLE company.order_line;
	REINDEX TABLE company.order_line_department;
	REINDEX TABLE company.item;
	REINDEX TABLE company.item_part;
	REINDEX TABLE company.item_variant;
END;
$$
LANGUAGE plpgsql;
COMMENT ON FUNCTION pa_company_drop(int) IS 
    'Function for drop a company';
ALTER FUNCTION pa_company_drop(int) 
    OWNER TO {pyAppPgOwnerRole};


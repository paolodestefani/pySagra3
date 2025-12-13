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


----------------------------
-- COMPANY SCHEMA OBJECTS --
----------------------------

SET search_path = company;

--
-- VIEWS
--
-- item availability view
CREATE OR REPLACE VIEW company.item_availability_detail AS
SELECT 
    e.company_id                AS company_id,
    e.event_id                  AS event_id,
    e.description               AS event_description,
    i.department_id             AS department_id,
    d.description               AS department_description,
    i.item_type                 AS item_type,
    i.item_id                   AS item_id,
    i.description               AS item_description,
    i.is_salable                AS is_salable,
    COALESCE(p.price, 0.00)     AS price,
    COALESCE(i.pos_row, 0)      AS pos_row,
    COALESCE(i.pos_column, 0)   AS pos_column,
	i.normal_text_color         AS normal_text_color,
	i.normal_background_color   AS normal_background_color,
    i.has_stock_control         AS has_stock_control,
    i.has_unload_control        AS has_unload_control,
    i.has_variants              AS has_variants,
    COALESCE(s.quantity, 0.00)  AS quantity, -- from stock_inventory
	i.is_web_available          AS is_web_available,
	i.web_sorting				AS web_sorting,
    CASE i.has_stock_control
		WHEN true AND s.quantity > 0 THEN true
		WHEN false THEN true
		ELSE false
	END                         AS is_available
    FROM company.event e
    LEFT JOIN company.item i ON e.company_id = i.company_id
    JOIN company.department d ON i.department_id = d.department_id
	LEFT JOIN company.price_list pl ON pl.price_list_id = e.price_list_id
	LEFT JOIN company.price_list_item p ON p.price_list_id = pl.price_list_id AND p.item_id = i.item_id
    LEFT JOIN (
        -- regular items
        SELECT 
            s.event_id                AS event,
            i.item_id                 AS item, 
            coalesce(s.balance, 0.00) AS quantity
        FROM company.item i
        LEFT JOIN ( SELECT event_id, item_id, balance 
                    FROM company.stock_inventory) s ON  i.item_id = s.item_id
        WHERE i.item_type = 'I'
        UNION 
        -- kit items    
        SELECT 
            t.event		    AS event,
            i.item_id 	    AS item,
            round(min(t.quantity/ik.quantity), 2) AS quantity -- quantity is the minimum of each component quantity, link quantity
        FROM company.item i
        JOIN company.item_part ik ON ik.item_id = i.item_id
        JOIN (-- quantity for each child
            SELECT 
                s.event_id  AS event,
                k.part_id   AS item,
                coalesce(s.balance, 0.00) AS quantity
            FROM company.item_part k
            JOIN company.item pi ON k.part_id = pi.item_id
            LEFT JOIN ( SELECT event_id, item_id, balance 
                        FROM company.stock_inventory 
                        ) s ON k.part_id = s.item_id
            WHERE pi.has_stock_control IS true 
                AND pi.is_obsolete IS false
            ) t ON ik.part_id = t.item
        WHERE i.item_type = 'K'
        GROUP BY t.event, i.item_id
        UNION
        -- menu items
        SELECT 
            s.event 		AS event,
            i.item_id		AS item,
            round(min(s.quantity/im.quantity), 2) AS quantity -- quantity is the minimum of each component quantity, link quantity
        FROM company.item i
        JOIN company.item_part im ON i.item_id = im.item_id
        JOIN (
            -- regular items
            SELECT 
                s.event_id	   AS event,
                i.item_id      AS item,
                COALESCE(s.balance, 0.00) AS quantity
            FROM company.item i
            LEFT JOIN (	SELECT event_id, item_id, balance 
						FROM company.stock_inventory) s ON i.item_id = s.item_id
            WHERE i.item_type = 'I'
            UNION 
            -- kit items
            SELECT 
                t.event AS event,
                i.item_id AS item,
                round(min(t.quantity/ik.quantity), 2) AS quantity -- quantity is the minimum of each component quantity, link quantity
            FROM company.item i
            JOIN company.item_part ik ON ik.item_id = i.item_id
            JOIN (-- quantity for each child
                SELECT 
                    s.event_id 	AS event,
                    k.part_id 	AS item,
                    coalesce(s.balance, 0.00) AS quantity
                FROM company.item_part k
                JOIN company.item pi ON k.part_id = pi.item_id
                LEFT JOIN (	SELECT event_id, item_id, balance 
                            FROM company.stock_inventory 
                            ) s ON k.part_id = s.item_id
                WHERE pi.has_stock_control IS true 
                    AND pi.is_obsolete IS false
                ) t ON ik.part_id = t.item
                WHERE i.item_type = 'K'
                GROUP BY t.event, i.item_id
            ) s ON im.part_id = s.item
            WHERE i.item_type = 'M'
            GROUP BY s.event, i.item_id
    ) s ON e.event_id = s.event AND i.item_id = s.item
WHERE i.is_obsolete IS false;
COMMENT ON VIEW item_availability_detail IS 
    'Item detail list with availability';
ALTER VIEW item_availability_detail 
    OWNER TO {pyAppPgOwnerRole};

-- item availability view
CREATE OR REPLACE VIEW company.income_summary AS
SELECT 
    oh.company_id           AS company_id,
    oh.event_id             AS event_id,
    ev.description          AS event_description,
    oh.stat_order_date      AS order_date,
    count(
        CASE
            WHEN oh.stat_order_day_part = 'L' THEN oh.order_header_id
            ELSE NULL
        END)                AS num_orders_lunch,
    count(
        CASE
            WHEN oh.stat_order_day_part = 'D' THEN oh.order_header_id
            ELSE NULL
        END)                AS num_orders_dinner,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'L' THEN oh.covers
            ELSE 0
        END)                AS num_covers_lunch,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'D' THEN oh.covers
            ELSE 0
        END)                AS num_covers_dinner,
    sum(
        CASE
            WHEN oh.delivery = 'A' AND oh.stat_order_day_part = 'L' THEN oh.total_amount
            ELSE 0
        END)                AS tot_take_away_lunch,
    sum(
        CASE
            WHEN oh.delivery = 'A' AND oh.stat_order_day_part = 'D' THEN oh.total_amount
            ELSE 0
        END)                AS tot_take_away_dinner,
    sum(
        CASE
            WHEN oh.delivery = 'T' AND oh.stat_order_day_part = 'L' THEN oh.total_amount
            ELSE 0
        END)                AS tot_table_lunch,
    sum(
        CASE
            WHEN oh.delivery = 'T' AND oh.stat_order_day_part = 'D' THEN oh.total_amount
            ELSE 0
        END)                AS tot_table_dinner,
    sum(
        CASE
            WHEN oh.is_electronic_payment IS false AND oh.stat_order_day_part = 'L' THEN oh.total_amount
            ELSE 0
        END)                AS tot_cash_lunch,
    sum(
        CASE
            WHEN oh.is_electronic_payment IS false AND oh.stat_order_day_part = 'D' THEN oh.total_amount
            ELSE 0
        END)                AS tot_cash_dinner,
    sum(
        CASE
            WHEN oh.is_electronic_payment IS true AND oh.stat_order_day_part = 'L' THEN oh.total_amount
            ELSE 0
        END)                AS tot_electronic_lunch,
    sum(
        CASE
            WHEN oh.is_electronic_payment IS true AND oh.stat_order_day_part = 'D' THEN oh.total_amount
            ELSE 0
        END)                AS tot_electronic_dinner,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'L' THEN oh.total_amount
            ELSE 0
        END)                AS amount_lunch,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'D' THEN oh.total_amount
            ELSE 0
        END)                AS amount_dinner,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'L' THEN oh.discount
            ELSE 0
        END)                AS discount_lunch,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'D' THEN oh.discount
            ELSE 0
        END)                AS discount_dinner,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'L' THEN oh.total_amount - oh.discount
            ELSE 0
        END)                AS cash_lunch,
    sum(
        CASE
            WHEN oh.stat_order_day_part = 'D' THEN oh.total_amount - oh.discount
            ELSE 0
        END)                AS cash_dinner
   FROM order_header oh
   JOIN event ev ON oh.event_id = ev.event_id
   GROUP BY oh.company_id, oh.event_id, ev.description, oh.stat_order_date
   ORDER BY oh.company_id, ev.description, oh.stat_order_date;
COMMENT ON VIEW income_summary IS 
    'Income summary view';
ALTER VIEW income_summary 
    OWNER TO {pyAppPgOwnerRole};


CREATE OR REPLACE VIEW company.bi_order_detail AS
SELECT 
    ev.company_id       AS "Azienda",
    ev.description      AS "Evento",
    pr.description      AS "Listino",
    oh.order_number     AS "Num.Ordine",
    oh.order_date       AS "Data",
    oh.order_time       AS "Ora",
    oh.stat_order_date  AS "Data Statistica",
    CASE oh.stat_order_day_part
        WHEN 'D'::bpchar THEN 'C'::text
        WHEN 'L'::bpchar THEN 'P'::text
        ELSE NULL::text
    END                 AS "Pranzo/Cena",
    oh.delivery         AS "Consegna",
    CASE oh.is_electronic_payment 
		WHEN true THEN 'E'
		ELSE 'C'
	END                 AS "Pagamento",
    oh.table_num        AS "Tavolo",
    oh.customer_name    AS "Nome cliente",
    oh.covers           AS "Coperti",
    de.description      AS "Reparto",
    it.item_type        AS "Tipo Articolo",
    it.description      AS "Articolo",
    ol.variants         AS "Varianti",
    it.description::text || COALESCE(' '::text || ol.variants::text, ''::text) AS "Articolo+Varianti",
    pri.price           AS "Prezzo di Listino",
    ol.quantity         AS "Quantità",
    ol.price            AS "Prezzo Ordine",
    ol.amount           AS "Importo",
    oh.total_amount     AS "Importo ordine",
    oh.discount         AS "Sconto",
    oh.cash             AS "Incasso",
    oh.change           AS "Resto"
FROM order_line ol
JOIN order_header oh ON ol.order_header_id = oh.order_header_id
JOIN event ev ON oh.event_id = ev.event_id
JOIN item it ON ol.item_id = it.item_id
JOIN department de ON it.department_id = de.department_id
LEFT JOIN price_list pr ON ev.price_list_id = pr.price_list_id
LEFT JOIN price_list_item pri ON pr.price_list_id = pri.price_list_id AND it.item_id = pri.item_id;

COMMENT ON VIEW bi_order_detail IS 
    'Order betail for BI analysis view';
ALTER VIEW bi_order_detail 
    OWNER TO {pyAppPgOwnerRole};


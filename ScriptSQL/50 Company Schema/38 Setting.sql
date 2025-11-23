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


-- company settings
CREATE TABLE setting (
    created_at                  timestamptz(3) NOT NULL,
	created_by                  text NOT NULL,
    updated_at                  timestamptz(3) NOT NULL,
	updated_by                  text NOT NULL,
    object_version              integer NOT NULL,
    --
    company_id                  integer NOT NULL,
    --
    lunch_start_time            integer NOT NULL DEFAULT 11,
    dinner_start_time           integer NOT NULL DEFAULT 18,
	order_entry_ui              integer NOT NULL DEFAULT 0,
    normal_background_color     char(7) DEFAULT '#4141c5',
    normal_text_color           char(7) DEFAULT '#FFFFFF',
    warning_background_color    char(7) DEFAULT '#F0F032',
    warning_text_color          char(7) DEFAULT '#000000',
    warning_stock_level         int NOT NULL DEFAULT 10,
    critical_background_color   char(7) DEFAULT '#C80000',
    critical_text_color         char(7) DEFAULT '#FFFFFF',
    critical_stock_level        int NOT NULL DEFAULT 5,
    disabled_background_color   char(7) DEFAULT '#CBCBCB',
    disabled_text_color         char(7) DEFAULT '#000000',
    default_delivery_type       char DEFAULT 'T',
    default_payment_type        char DEFAULT 'C', -- Cache or Electronic
    order_list_tab_position     char NOT NULL DEFAULT 'N',
    order_list_rows             int NOT NULL DEFAULT 4,
    order_list_columns          int NOT NULL DEFAULT 4,
    order_list_spacing          int NOT NULL DEFAULT 8,
    order_list_font_family      varchar(60) NOT NULL DEFAULT 'Arial',
    order_list_font_size        integer NOT NULL DEFAULT 12,
    print_customer_copy         boolean NOT NULL DEFAULT False,
    print_department_copy       boolean NOT NULL DEFAULT False,
    print_cover_copy            boolean NOT NULL DEFAULT False,
    customer_copies             int DEFAULT 1,
    department_copies           int DEFAULT 1,
    cover_copies                int DEFAULT 1,
    customer_report             varchar(48),
    department_report           varchar(48),
    cover_report                varchar(48),
    customer_printer_class      int,
    cover_printer_class         int,
    max_covers                  int NOT NULL DEFAULT 12,
	manage_order_progress       boolean NOT NULL DEFAULT False,
    automatic_show_variants     boolean NOT NULL DEFAULT False,
    always_show_stock_inventory boolean NOT NULL DEFAULT False,
    mandatory_table_number      boolean NOT NULL DEFAULT True,
    use_table_list              boolean NOT NULL DEFAULT True,
    table_list_rows             int NOT NULL DEFAULT 8,
    table_list_columns          int NOT NULL DEFAULT 8,
    table_list_spacing          int NOT NULL DEFAULT 8,
    table_list_font_family      varchar(60) NOT NULL DEFAULT 'Arial',
    table_list_font_size        integer NOT NULL DEFAULT 12,
    check_inactivity            boolean NOT NULL DEFAULT True,
    inactivity_time             int NOT NULL DEFAULT 180,
    stock_unload_automatic_update       boolean NOT NULL DEFAULT False,
    stock_unload_update_interval        int NOT NULL DEFAULT 0,
    print_stock_unload_report   boolean NOT NULL DEFAULT False,
	stock_unload_copies         int DEFAULT 1,
    stock_unload_report         varchar(48),
    stock_unload_printer_class  int,
    num_orders_for_start_stock_unload   int DEFAULT 30,
    num_orders_for_next_stock_unload    int DEFAULT 10,
	quantity_decimal_places             int NOT NULL DEFAULT 0,
	currency_symbol             varchar(3) NOT NULL DEFAULT '€',
    --
    CONSTRAINT setting_pk 
        PRIMARY KEY (company_id) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS},
    CONSTRAINT setting_company_fk 
        FOREIGN KEY (company_id)
        REFERENCES system.company (company_id) 
        MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT setting_tab_position_check 
        CHECK (order_list_tab_position IN ('N', 'S', 'E', 'W')),
    CONSTRAINT setting_customer_printer_class_fk 
        FOREIGN KEY (customer_printer_class) 
        REFERENCES printer_class (printer_class_id)
        MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT setting_covers_printer_class_fk 
        FOREIGN KEY (cover_printer_class) 
        REFERENCES printer_class (printer_class_id)
        MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    --CONSTRAINT setting_stock_unload_report_fkey FOREIGN KEY (stock_unload_report) REFERENCES system.report (id)
    --    MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT setting_stock_unload_printer_class_fk 
        FOREIGN KEY (stock_unload_printer_class) 
        REFERENCES printer_class (printer_class_id)
        MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT setting_default_delivery_type_check 
        CHECK (default_delivery_type IN ('T', 'A')), -- Table, take-Away
    CONSTRAINT setting_default_payment_type_check 
        CHECK (default_payment_type IN ('C', 'E')) -- Cache, Electronic

) TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE setting IS 
    'Company specific application settings';
ALTER TABLE setting 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON company.setting 
    FOR EACH ROW EXECUTE PROCEDURE system.update_company_user_date();

--INSERT INTO setting (id) VALUES (True); -- create one record filled with all default values


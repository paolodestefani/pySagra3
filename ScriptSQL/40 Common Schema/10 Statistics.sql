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

SET search_path = common;

/*
-- table: statistics sql scripts
CREATE TABLE statistics_configuration (
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          int NOT NULL,
    --
    code                    varchar(48),
    description             text NOT NULL,
	active                  boolean NOT NULL DEFAULT true,
	sorting                 integer NOT NULL DEFAULT 0,
	sql_query               text,
	totals_row              boolean NOT NULL DEFAULT false,
	total_label_column      int,
	report_code             varchar(48),
    --
    CONSTRAINT statistics_configuration_pkey 
        PRIMARY KEY (code) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS}
	
) TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE statistics_configuration IS 
    'Statistics query definition table';
ALTER TABLE statistics_configuration 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON statistics_configuration  
    FOR EACH ROW EXECUTE PROCEDURE system.update_company_user_date();


-- table: statistics sql scripts
CREATE TABLE statistics_configuration_column (
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          int NOT NULL,
    --
    configuration_code      varchar(48),
	definition              text NOT NULL,
    description             text NOT NULL,
	column_type             text NOT NULL,
	total_required          boolean NOT NULL DEFAULT false,
	sorting                 int,
    --
    CONSTRAINT statistics_configuration_column_pkey 
        PRIMARY KEY (configuration_code, definition) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS},
	CONSTRAINT statistics_configuration_column_configuration_fkey 
        FOREIGN KEY (configuration_code) 
        REFERENCES statistics_configuration (code)
        MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE
	
) TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE statistics_configuration_column IS 
    'Statistics query definition columns table';
ALTER TABLE statistics_configuration_column 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON statistics_configuration_column  
    FOR EACH ROW EXECUTE PROCEDURE system.update_company_user_date();

*/

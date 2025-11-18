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
-- SYSTEM SCHEMA OBJECTS --
---------------------------

SET search_path = system;


-- system table: profile
CREATE TABLE profile (
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          integer NOT NULL,
    --
    profile_code            varchar(48),
    description             text NOT NULL,
    is_system_object        boolean NOT NULL DEFAULT False,
    --
    CONSTRAINT profile_pk 
        PRIMARY KEY (profile_code) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS}
)
TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE profile IS 
    '{pyAppName} profiles table';
ALTER TABLE profile 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON profile 
    FOR EACH ROW EXECUTE PROCEDURE update_company_user_date();


-- system table: actions for profiles
CREATE TABLE profile_action (
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          integer NOT NULL,
    --
    profile_code            varchar(48),
    action                  varchar(48),
    auth                    char,
    --
    CONSTRAINT profile_action_pk 
        PRIMARY KEY (profile_code, action) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS},
    CONSTRAINT profile_action_profile_fk 
        FOREIGN KEY (profile_code) 
        REFERENCES profile (profile_code)
        MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT profile_action_auth_check 
        CHECK (auth IN ('R', 'W', 'X'))
)
TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE profile_action IS 
    'Actions for each profile and authorization setting';
ALTER TABLE profile_action 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON profile_action 
    FOR EACH ROW EXECUTE PROCEDURE update_company_user_date();


-- system table: menu
CREATE TABLE menu(
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          integer NOT NULL,
    --
    menu_code               varchar(48),
    description             text,
    is_system_object        boolean NOT NULL DEFAULT False,
    --
    CONSTRAINT menu_pk 
        PRIMARY KEY (menu_code) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS}
)
TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE menu IS 
    'Menu class definition';
ALTER TABLE menu 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON menu 
    FOR EACH ROW EXECUTE PROCEDURE update_company_user_date();


-- system table: menu item
CREATE TABLE menu_item(
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          integer NOT NULL,
    --
    parent                  varchar(48),
    child                   varchar(48),
    description             text,
    sorting                 integer NOT NULL,
    item_type               char(1) NOT NULL,
    action                  varchar(48),
    --
    CONSTRAINT menu_item_pk 
        PRIMARY KEY (parent, child) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS},
    CONSTRAINT menu_item_type_check 
        CHECK (item_type IN ('A', 'M', 'S')) -- Action, Menu, Separator
)
TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE menu_item IS 
    'Menu and structure';
ALTER TABLE menu_item 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON menu_item 
    FOR EACH ROW EXECUTE PROCEDURE update_company_user_date();


-- system table: toolbar
CREATE TABLE toolbar(
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          integer NOT NULL,
    --
    toolbar_code            varchar(48),
    description             text,
    is_system_object        boolean NOT NULL DEFAULT False,
    --
    CONSTRAINT toolbar_pk 
        PRIMARY KEY (toolbar_code) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS}
)
TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE toolbar IS 
    'Toolbar class definition';
ALTER TABLE toolbar 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON toolbar 
    FOR EACH ROW EXECUTE PROCEDURE update_company_user_date();


-- system table: toolbar item
CREATE TABLE toolbar_item(
    created_at              timestamptz(3) NOT NULL,
	created_by              text NOT NULL,
    updated_at              timestamptz(3) NOT NULL,
	updated_by              text NOT NULL,
    object_version          integer NOT NULL,
    --
    parent                  varchar(48),
    child                   varchar(48),
    description             text,
    sorting                 integer NOT NULL,
    item_type               char(1) NOT NULL,
    action                  varchar(48),
    --
    CONSTRAINT toolbar_item_pk 
        PRIMARY KEY (parent, child) 
        USING INDEX TABLESPACE {pyAppPgIndexesTS},
    CONSTRAINT toolbar_item_type_check 
        CHECK (item_type IN ('T', 'A', 'S', 'W')) -- Toolbar, Action, Separator,  Widget
)
TABLESPACE {pyAppPgTablesTS};
COMMENT ON TABLE toolbar_item IS 
    'Toolbar structure';
ALTER TABLE toolbar_item 
    OWNER TO {pyAppPgOwnerRole};

CREATE TRIGGER t99_update_company_user_date 
    BEFORE INSERT OR UPDATE ON toolbar_item 
    FOR EACH ROW EXECUTE PROCEDURE update_company_user_date();


-- system function: get current user/profile actions
CREATE FUNCTION pa_get_actions()
RETURNS TABLE (action varchar, auth char) AS
$$
BEGIN
    RETURN QUERY 
        SELECT pa.action, pa.auth
        FROM system.profile_action pa
        JOIN system.connection cn ON pa.profile_code = cn.profile_code
        JOIN system.app_user u ON cn.app_user_code = u.user_code
        WHERE cn.session_id = pg_backend_pid();
END;
$$
LANGUAGE plpgsql;
COMMENT ON FUNCTION pa_get_actions() IS 
    'Get current user/profile actions';
ALTER FUNCTION pa_get_actions() 
    OWNER TO {pyAppPgOwnerRole};


-- system function: get current user menu
CREATE FUNCTION pa_get_menu(object varchar)
RETURNS TABLE ( child varchar, 
                item_type char,
                description text,
                action varchar) AS
$$
BEGIN
    RETURN QUERY 
        EXECUTE 'SELECT m.child, m.item_type, m.description, m.action
            FROM system.menu_item m
            WHERE m.parent = $1
            ORDER BY m.sorting;' 
            USING object;
END;
$$
LANGUAGE plpgsql;
COMMENT ON FUNCTION pa_get_menu(varchar) IS 
    'Get current user menu';
ALTER FUNCTION pa_get_menu(varchar) 
    OWNER TO {pyAppPgOwnerRole};


-- system function: get current user toolbar
CREATE OR REPLACE FUNCTION pa_get_toolbar(object varchar)
RETURNS TABLE ( child varchar,
                item_type char,
                description text, 
                action varchar) AS
$$
BEGIN
    RETURN QUERY 
        EXECUTE 'SELECT t.child, t.item_type, t.description, t.action
            FROM system.toolbar_item t
            WHERE t.parent = $1
            ORDER BY t.sorting;' 
            USING object;
END;
$$
LANGUAGE plpgsql;
COMMENT ON FUNCTION pa_get_toolbar(varchar) IS 
    'Get current user toolbar';
ALTER FUNCTION pa_get_toolbar(varchar) 
    OWNER TO {pyAppPgOwnerRole};

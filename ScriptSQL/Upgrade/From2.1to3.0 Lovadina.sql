--
-- Execute in the new database after restore the schema of the company to be imported
-- 
-- This is for lovadina company, "lovadina" schema, new company code 40
-- Execute one table at a time
--
-- 1 Clean previous import
-- 2 Create users (in script) from user_ins of order_header
-- 3 Create a specific company (in script) numeber 40
-- 4 Set default profile/medu/toolbar to all user for the company 40
-- 5 Import data
--

SET search_path = system, common, company;

DO $$ BEGIN RAISE NOTICE '% Set path', clock_timestamp(); END; $$;


--
-- DELETE PREVIOUS IMPORT
--

-- Drop company

DO $$ BEGIN RAISE NOTICE '% BEGIN Drop company 40', clock_timestamp(); END; $$;

SELECT system.pa_company_drop(40);

DO $$ BEGIN RAISE NOTICE '% END Drop company 40', clock_timestamp(); END; $$;

-- delete users from importing company
DELETE FROM system.app_user
WHERE user_code IN (
	SELECT DISTINCT
		user_ins
	FROM lovadina.order_header
	WHERE user_ins NOT IN ('postgres', 'system', 'utente')
	);

DO $$ BEGIN RAISE NOTICE '% Deleted users', clock_timestamp(); END; $$;


--
-- BEGIN COMPANY IMPORT
--

--
-- create users from order_header
--

INSERT INTO system.app_user (
	user_code,
	description,
	user_password,
	is_admin,
	l10n,
	is_system_object)
SELECT
	u.user_ins AS code,
	u.user_ins AS description,
	system.crypt(u.user_ins, system.gen_salt('bf')) AS user_password, -- password is set as user_name
	false AS is_admin,
	'it_IT' AS l10n,
	False AS is_system_object
FROM (
	SELECT DISTINCT
		user_ins
	FROM lovadina.order_header
	WHERE user_ins NOT IN ('postgres', 'system', 'utente')
	) u
ON CONFLICT DO NOTHING;

DO $$ BEGIN RAISE NOTICE '% Imported users', clock_timestamp(); END; $$;


--
-- create company
--

SELECT system.pa_company_create(40, 'Lovadina', false, Null);

DO $$ BEGIN RAISE NOTICE '% Created new company 40', clock_timestamp(); END; $$;


--
-- Set default profile/menu/toolbar to all users for company 40
--

INSERT INTO system.app_user_company (
	app_user_code,
	company_id, 
	profile_code,
	menu_code,
	toolbar_code)
SELECT 
	u.user_ins,
	40,
	'default',
	'default_it',
	'default_it'
FROM (
	SELECT DISTINCT
		user_ins
	FROM lovadina.order_header
	WHERE user_ins NOT IN ('postgres', 'system', 'utente')
	) u
ON CONFLICT DO NOTHING;
-- set profile/menu/toolbar for system user
INSERT INTO system.app_user_company (
	app_user_code,
	company_id, 
	profile_code,
	menu_code,
	toolbar_code)
VALUES ('system', 40, 'full', 'full_en', 'full_en')
ON CONFLICT DO NOTHING;

DO $$ BEGIN RAISE NOTICE '% Set profile/menu/toolbar for users on company 40', clock_timestamp(); END; $$;


--
-- DISABLE TRIGGERS
--

ALTER TABLE company.event DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.printer_class DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.printer_class_printer DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.department DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.stand_table DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.item DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.item_variant DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.item_part DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.price_list DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.price_list_item DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_header DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_header_department DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_line DISABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_line_department DISABLE TRIGGER t10_order_line_to_unloaded;
ALTER TABLE company.order_line_department DISABLE TRIGGER t99_update_company_user_date;


--
-- Import events
--

INSERT INTO company.event (
	external_code,
	company_id,
	description,
	start_date,
	end_date,
	image,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT
	id,				-- external_code
	40,				-- company_id
	description,	-- description
	date_start,		-- date_start
	date_end,		-- date_end
	image,			-- image
	user_ins,		-- created_by
	date_ins, 		-- created_at
	user_upd,		-- updated_by
	date_upd,		-- updated_at
	0				-- object_version
FROM lovadina.event;

DO $$ BEGIN RAISE NOTICE '% Imported events', clock_timestamp(); END; $$;


--
-- Import printer class
--

INSERT INTO company.printer_class (
	external_code,
	company_id,
	description,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	id,				-- external_code
	40,				-- company_id
	description,	-- description
	user_ins,		-- created_by
	date_ins,		-- created_at
	user_upd,		-- updated_by
	date_upd,		-- updated_at
	0				-- object_version
FROM lovadina.printer_class;

DO $$ BEGIN RAISE NOTICE '% Imported printer class', clock_timestamp(); END; $$;


--
-- Import printer class printer
--

INSERT INTO company.printer_class_printer (
	external_code,
	company_id,
	printer_class_id,
	computer,
	printer,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id,				-- external_code
	40,					-- company_id
	c.printer_class_id,	-- class_id
	i.computer,			-- computer
	i.printer,			-- printer
	i.user_ins,			-- created_by
	i.date_ins,			-- created_at
	i.user_upd,			-- updated_by
	i.date_upd,			-- updated_at
	0					-- object_version
FROM lovadina.printer_class_printer i
JOIN company.printer_class c ON i.class_id = c.external_code AND c.company_id = 40;

DO $$ BEGIN RAISE NOTICE '% Imported printer class printer', clock_timestamp(); END; $$;


--
-- Import settings
--

WITH par AS (
	SELECT 
		40 AS company_id,
		i.lunch_start_time,
		i.dinner_start_time,
		i.normal_background_color,
		i.normal_text_color,
		i.warning_background_color,
		i.warning_text_color,
		i.warning_stock_level,
		i.critical_background_color,
		i.critical_text_color,
		i.critical_stock_level,
		i.disabled_background_color,
		i.disabled_text_color,
		i.default_delivery_type,
		-- i.default_payment_type,
		i.order_list_tab_position,
		i.order_list_rows,
		i.order_list_columns,
		i.order_list_spacing,
		i.order_list_font_family,
		i.order_list_font_size,
		i.print_customer_copy,
		i.print_department_copy,
		i.print_cover_copy,
		i.customer_copies,
		i.department_copies,
		i.cover_copies,
		i.customer_report,
		i.department_report,
		i.cover_report,
		c1.printer_class_id AS customer_printer_class,
		c2.printer_class_id AS cover_printer_class,
		i.max_covers,
		i.manage_order_progress,
		i.automatic_show_variants,
		i.always_show_stock_inventory,
		i.mandatory_table_number,
		i.use_table_list,
		i.table_list_rows,
		i.table_list_columns,
		i.table_list_spacing,
		i.table_list_font_family,
		i.table_list_font_size,
		i.check_inactivity,
		i.inactivity_time,
		i.stock_unload_automatic_update,
		i.stock_unload_update_interval,
		i.print_stock_unload_report,
		i.stock_unload_copies,
		i.stock_unload_report,
		c3.printer_class_id AS stock_unload_printer_class,
		i.num_orders_for_start_stock_unload,
		i.num_orders_for_next_stock_unload,
		i.quantity_decimal_places,
		i.currency_symbol
	FROM lovadina.setting i
	LEFT JOIN company.printer_class c1 ON i.customer_printer_class = c1.external_code AND c1.company_id = 40
	LEFT JOIN company.printer_class c2 ON i.cover_printer_class = c2.external_code AND c2.company_id = 40
	LEFT JOIN company.printer_class c3 ON i.stock_unload_printer_class = c3.external_code AND c3.company_id = 40
	WHERE i.id IS true
)
UPDATE company.setting
SET lunch_start_time = par.lunch_start_time,
	dinner_start_time = par.dinner_start_time,
	normal_background_color = par.normal_background_color,
	normal_text_color = par.normal_text_color,
	warning_background_color = par.warning_background_color,
	warning_text_color = par.warning_text_color,
	warning_stock_level = par.warning_stock_level,
	critical_background_color = par.critical_background_color,
	critical_text_color = par.critical_text_color,
	critical_stock_level = par.critical_stock_level,
	disabled_background_color = par.disabled_background_color,
	disabled_text_color = par.disabled_text_color,
	default_delivery_type = par.default_delivery_type,
	-- default_payment_type = par.default_payment_type,
	order_list_tab_position = par.order_list_tab_position,
	order_list_rows = par.order_list_rows,
	order_list_columns = par.order_list_columns,
	order_list_spacing = par.order_list_spacing,
	order_list_font_family = par.order_list_font_family,
	order_list_font_size = par.order_list_font_size,
	print_customer_copy = par.print_customer_copy,
	print_department_copy = par.print_department_copy,
	print_cover_copy = par.print_cover_copy,
	customer_copies = par.customer_copies,
	department_copies = par.department_copies,
	cover_copies = par.cover_copies,
	customer_report = par.customer_report,
	department_report = par.department_report,
	cover_report = par.cover_report,
	customer_printer_class = par.customer_printer_class,
	cover_printer_class = par.cover_printer_class,
	max_covers = par.max_covers,
	manage_order_progress = par.manage_order_progress,
	automatic_show_variants = par.automatic_show_variants,
	always_show_stock_inventory = par.always_show_stock_inventory,
	mandatory_table_number = par.mandatory_table_number,
	use_table_list = par.use_table_list,
	table_list_rows = par.table_list_rows,
	table_list_columns = par.table_list_columns,
	table_list_spacing = par.table_list_spacing,
	table_list_font_family = par.table_list_font_family,
	table_list_font_size = par.table_list_font_size,
	check_inactivity = par.check_inactivity,
	inactivity_time = par.inactivity_time,
	stock_unload_automatic_update = par.stock_unload_automatic_update,
	stock_unload_update_interval = par.stock_unload_update_interval,
	print_stock_unload_report = par.print_stock_unload_report,
	stock_unload_copies = par.stock_unload_copies,
	stock_unload_report = par.stock_unload_report,
	stock_unload_printer_class = par.stock_unload_printer_class,
	num_orders_for_start_stock_unload = par.num_orders_for_start_stock_unload,
	num_orders_for_next_stock_unload = par.num_orders_for_next_stock_unload,
	quantity_decimal_places = par.quantity_decimal_places,
	currency_symbol = par.currency_symbol
FROM par
WHERE company.setting.company_id = par.company_id; 

DO $$ BEGIN RAISE NOTICE '% Updated settings', clock_timestamp(); END; $$;


--
-- Import departments
--

INSERT INTO company.department (
	external_code,
	company_id,
	description, 
	sorting, 
	printer_class_id, 
	is_obsolete, 
	is_menu_container, 
	is_for_takeaway,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id, 				-- external_code
	40,					-- company_id
	i.description,		-- description
	i.sorting,			-- sorting
	p.printer_class_id,	-- printer_class
	i.is_obsolete,		-- is_obsolete
	i.is_not_managed,	-- is_menu_container
	i.is_for_takeaway, 	-- is_for_takeaway
	i.user_ins, 		-- created_by
	i.date_ins,			-- created_at
	i.user_upd,			-- updated_by
	i.date_upd,			-- updated_at
	0					-- object_version
FROM lovadina.department i
JOIN company.printer_class p ON i.printer_class = p.external_code AND p.company_id = 40;

-- add a temporary department used for items that not have a department
-- set created/delete/etc because trigger are disabled
INSERT INTO company.department (
	company_id, 
	description,
	is_obsolete,
	is_menu_container,
	is_for_takeaway,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
VALUES (
	40,
	'*** REPARTO MANCANTE ***',
	true,
	false,
	false,
	system.pa_current_user(),
	now(),
	system.pa_current_user(),
	now(),
	0); 

DO $$ BEGIN RAISE NOTICE '% Imported departments', clock_timestamp(); END; $$;


--
-- Import stand tables
--

INSERT INTO company.stand_table (
	external_code,
	company_id,
	table_code,
	pos_row,
	pos_column,
	text_color,
	background_color,
	is_obsolete,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT
	id,					-- external_code
	40, 				-- company_id
	table_code,			-- table_code
	pos_row,			-- pos_row
	pos_column,			-- pos_column
	text_color,			-- text_color
	background_color,	-- background_color
	is_obsolete,		-- is_obsolete
	user_ins,			-- created_by
	date_ins,			-- created_at
	user_upd,			-- updated_by
	date_upd,			-- updated_at
	0					-- object_version
FROM lovadina.numbered_table;

DO $$ BEGIN RAISE NOTICE '% Imported tables', clock_timestamp(); END; $$;


--
-- Import items
--

INSERT INTO company.item (
	external_code,
	company_id,
	item_type, 
	description, 
	customer_description,
	department_id,
	sorting,
	pos_row,
	pos_column,
	normal_background_color,
	normal_text_color,
	has_variants,
	has_stock_control,
	has_unload_control,
	is_kit_part,
	is_menu_part,
	is_salable,
	is_web_available,
	web_sorting,
	is_obsolete,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id,						-- external_code
	40, 						-- company_id
	i.item_type,				-- item_type
	i.description,				-- description
	i.customer_description,		-- customer_description
	coalesce(d.department_id, m.department_id),		-- department_id
	i.sorting,					-- sorting
	i.pos_row,					-- pos_row
	i.pos_column,				-- pos_column
	i.normal_background_color,	-- normal_background_color
	i.normal_text_color,		-- normal_text_color
	i.has_variants,				-- has_variants
	i.has_stock_control,		-- has_stock_control
	i.has_unload_control,		-- has_unload_control
	i.is_kit_part,				-- is_kit_part
	i.is_menu_part,				-- is_menu_part
	i.is_salable,				-- is_salable
	i.is_web_available,			-- is_web_available
	i.web_sorting,				-- web_sorting
	i.is_obsolete,				-- is_obsolete
	i.user_ins,					-- created_by
	i.date_ins,					-- created_at
	i.user_upd,					-- updated_by
	i.date_upd,					-- updated_at
	0							-- object_version
FROM lovadina.item i
LEFT JOIN company.department d ON i.department = d.external_code AND d.company_id = 40
CROSS JOIN (
	SELECT department_id
	FROM company.department 
	WHERE company_id = 40 
		AND description = '*** REPARTO MANCANTE ***') m;

DO $$ BEGIN RAISE NOTICE '% Imported items', clock_timestamp(); END; $$;


--
-- Import item variants
--

INSERT INTO company.item_variant (
	external_code,
	company_id,
	item_id, 
	variant_description, 
	sorting, 
	price_delta,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id,					-- external_code
	40, 					-- company_id
	y.item_id,				-- item_id
	i.variant_description,	-- variant_description
	i.sorting,				-- sorting
	i.price_delta,			-- price_delta
	i.user_ins,				-- created_by
	i.date_ins,				-- created_at
	i.user_upd,				-- updated_by
	i.date_upd,				-- updated_at
	0						-- object_version
FROM lovadina.item_variant i
LEFT JOIN company.item y ON i.item = y.external_code AND y.company_id = 40;

DO $$ BEGIN RAISE NOTICE '% Imported item variants', clock_timestamp(); END; $$;


--
-- Import item parts
--

INSERT INTO company.item_part (
	external_code,
	company_id,
	item_type, 
	item_id,
	part_id, 
	quantity,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT
	i.id,			-- external_code
	40,				-- company_id
	i.item_type,	-- item_type
	y1.item_id,		-- item_id
	y2.item_id,		-- part_id
	i.quantity,		-- quantity
	i.user_ins,		-- created_by
	i.date_ins,		-- created_at
	i.user_upd,		-- updated_by
	i.date_upd,		-- updated_at
	0				-- object_version
FROM lovadina.item_part i
LEFT JOIN company.item y1 ON i.item = y1.external_code AND y1.company_id = 40
LEFT JOIN company.item y2 ON i.part = y2.external_code AND y2.company_id = 40;

DO $$ BEGIN RAISE NOTICE '% Imported item parts', clock_timestamp(); END; $$;


--
-- Import price list
--

INSERT INTO company.price_list (
	external_code,
	company_id,
	description,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT
	id,				-- external_code,
	40,				-- company_id,
	description,	-- description
	user_ins,		-- created_by
	date_ins,		-- created_at
	user_upd,		-- updated_by
	date_upd,		-- updated_at
	0				-- object_version
FROM lovadina.price_list;

DO $$ BEGIN RAISE NOTICE '% Imported price list', clock_timestamp(); END; $$;


--
-- Import price list items
--

INSERT INTO company.price_list_item (
	external_code,
	company_id,
	price_list_id, 
	item_id, 
	price,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT
    i.id,				-- external_code
	40, 				-- company_id
	l.price_list_id,	-- price_list_id
	y.item_id,	 		-- item_id
    i.price,			-- price
    i.user_ins,			-- created_by
    i.date_ins,			-- created_at
    i.user_upd,			-- updated_by
    i.date_upd,			-- updated_at
    0 					-- object_version
FROM lovadina.price_list_detail i
LEFT JOIN company.price_list l ON i.id_price_list = l.external_code AND l.company_id = 40
LEFT JOIN company.item y ON i.item = y.external_code AND y.company_id = 40;

DO $$ BEGIN RAISE NOTICE '% Imported price list items', clock_timestamp(); END; $$;


-- 
-- Import order header
--

DO $$ BEGIN RAISE NOTICE '% BEGIN Import order headers', clock_timestamp(); END; $$;

INSERT INTO company.order_header (
	external_code,
	company_id,
	event_id,
	date_time,
	order_number,
	order_date,
	order_time,
	stat_order_date,
	stat_order_day_part,
	cash_desk,
	delivery,
	table_num,
	customer_name,
	covers,
	total_amount,
	discount,
	cash,
	change, 
	--is_electronic_payment,
	status,
	fullfillment_date,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id, 					-- external_code,
	40, 					-- company_id,
	e.event_id, 			-- event_id,
	i.date_time,			-- date_time
	i.order_number,			-- order_number
	i.order_date,			-- order_date
	i.order_time,			-- order_time
	i.stat_order_date,		-- stat_order_date
	i.stat_order_day_part,	-- stat_order_day_part
	i.cash_desk,			-- cash_desk
	i.delivery,				-- delivery
	i.table_num,			-- table_num
	i.customer_name,		-- customer_name
	i.covers,				-- covers
	i.total_amount,			-- total_amount
	i.discount,				-- discount
	i.cash,					-- cash
	i.change,				-- change
	--is_electronic_payment, -- is_electronic_payment
	i.status,				-- status
	i.fullfillment_date,	-- fullfillment_date
	i.user_ins,				-- created_by
	i.date_ins,				-- created_at
	i.user_upd,				-- updated_by
	i.date_upd,				-- updated_at
	0 						-- object_version
FROM lovadina.order_header i
LEFT JOIN company.event e ON i.event = e.external_code AND e.company_id=40;

DO $$ BEGIN RAISE NOTICE '% END Import order headers', clock_timestamp(); END; $$;


--
-- Import order header department
--

DO $$ BEGIN RAISE NOTICE '% BEGIN Import order header departments', clock_timestamp(); END; $$;

INSERT INTO company.order_header_department (
	external_code,
	company_id,
	order_header_id, 
	department_id,
	note,
	other_departments,
	fullfillment_date,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id, 					-- external_code
	40, 					-- company_id
	h.order_header_id,		-- header_id 
	d.department_id, 		-- department_id
	i.note,					-- note
	i.other_departments, 	-- other_departments
	i.fullfillment_date, 	-- fullfillment_date
	i.user_ins,				-- created_by
	i.date_ins,				-- created_at
	i.user_upd,				-- updated_by
	i.date_upd,				-- updated_at
	0						-- object_version
FROM lovadina.order_header_department i
LEFT JOIN company.order_header h ON i.id_header = h.external_code AND h.company_id = 40
LEFT JOIN company.department d ON i.department = d.external_code AND d.company_id = 40;

DO $$ BEGIN RAISE NOTICE '% END Import order header departments', clock_timestamp(); END; $$;


--
-- Import order line
--

DO $$ BEGIN RAISE NOTICE '% BEGIN Import order lines', clock_timestamp(); END; $$;

INSERT INTO company.order_line (
	external_code,
	company_id,
	order_header_id, 
	item_id, 
	variants, 
	quantity, 
	price, 
	amount,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id, 				-- external_code
	40,					-- company_id
	h.order_header_id, 	-- header_id
	y.item_id,			-- item_id
	i.variants,			-- variants
	i.quantity,			-- quantity
	i.price,			-- price
	i.amount,			-- amount
	i.user_ins,			-- created_by
	i.date_ins,			-- created_at
	i.user_upd,			-- updated_by
	i.date_upd,			-- updated_at 
	0 					-- object_version
FROM lovadina.order_detail i
LEFT JOIN company.order_header h ON i.id_header = h.external_code AND h.company_id = 40
LEFT JOIN company.item y ON i.item = y.external_code AND y.company_id = 40;

DO $$ BEGIN RAISE NOTICE '% END Import order lines', clock_timestamp(); END; $$;


--
-- Import order line departments
--

DO $$ BEGIN RAISE NOTICE '% BEGIN Import order line departments', clock_timestamp(); END; $$;

INSERT INTO company.order_line_department (
	external_code,
	company_id,
	order_header_id, 
	event_id, 
	event_date, 
	day_part, 
	department_id, 
	item_id, 
	variants,
	quantity,
	created_by,
	created_at,
	updated_by,
	updated_at,
	object_version)
SELECT 
	i.id,				-- external_code
	40,					-- company_id
	h.order_header_id,	-- header_id
	e.event_id,			-- event_id
	i.event_date,		-- event_date
	i.day_part,			-- day_part
	d.department_id,	-- department_id
	y.item_id,			-- item_id
	i.variants,			-- variants
	i.quantity,			-- quantity
	i.user_ins,			-- created_by
	i.date_ins, 		-- created_at
	i.user_upd, 		-- updated_by
	i.date_upd, 		-- updated_at
	0 					-- object_version
FROM lovadina.order_detail_department i
LEFT JOIN company.order_header h ON i.id_header = h.external_code AND h.company_id = 40
LEFT JOIN company.event e ON i.event = e.external_code AND e.company_id = 40
LEFT JOIN company.department d ON i.department = d.external_code AND d.company_id = 40
LEFT JOIN company.item y ON i.item = y.external_code AND y.company_id = 40;

DO $$ BEGIN RAISE NOTICE '% END Import order line departments', clock_timestamp(); END; $$;

-- stock_inventory will be rebuild


--
-- update unloads and numbering
--

DO $$ BEGIN RAISE NOTICE '% BEGIN Update unloads and numbering', clock_timestamp(); END; $$;

DO $$
DECLARE
i int;
BEGIN

DELETE FROM company.numbering WHERE company_id = 40;

FOR i IN 	SELECT event_id 
			FROM company.event 
			WHERE company_id = 40 
			ORDER BY event_id
	LOOP
		PERFORM company.numbering_rebuild(i);
		PERFORM company.unload_rebuild(i);
	END LOOP;
	
END;
$$
language plpgsql;

DO $$ BEGIN RAISE NOTICE '% END Update unloads and numbering', clock_timestamp(); END; $$;


--
-- ENABLE TRIGGERS
--

ALTER TABLE company.event ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.printer_class ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.printer_class_printer ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.department ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.stand_table ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.item ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.item_variant ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.item_part ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.price_list ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.price_list_item ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_header ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_header_department ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_line ENABLE TRIGGER t99_update_company_user_date;
ALTER TABLE company.order_line_department ENABLE TRIGGER t10_order_line_to_unloaded;
ALTER TABLE company.order_line_department ENABLE TRIGGER t99_update_company_user_date;

--
-- rebuild main index
--

REINDEX TABLE company.order_header;
REINDEX TABLE company.order_header_department;
REINDEX TABLE company.order_line;
REINDEX TABLE company.order_line_department;

-- END


#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author: Paolo De Stefani
# Contact: paolo <at> paolodestefani <dot> it
# Copyright (C) 2026 Paolo De Stefani
# License: GPL v3

# This file is part of pySagra.
#
# pySagra is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pySagra is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pySagra.  If not, see <http://www.gnu.org/licenses/>.

"""database - sql report extraction



"""

# psycopg
import psycopg

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.Connect import appconn


def load_report(report_code, l10n, report_class, system, description, xml_data):
    "Load a report filling system.report"
    script = """
INSERT INTO system.report (
    report_code,
    l10n,
    report_class,
    description,
    xml_data,
    is_system_object)
VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT report_unique DO
	UPDATE SET report_class = %s, description = %s, xml_data = %s, is_system_object = %s;
    """
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (report_code,
                                     l10n,
                                     report_class,
                                     description,
                                     xml_data,
                                     system,
                                     report_class,
                                     description,
                                     xml_data,
                                     system))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def list_all_report():
    "List all reports from system.report for exporting purposes"
    script = """
SELECT
    report_code,
    l10n,
    report_class,
    is_system_object,
    description,
    xml_data
FROM system.report
ORDER BY report_code ASC, l10n ASC;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def clear_report_adapt(adapt_id):
    "Clear the report customizations setting"
    script = """
DELETE FROM system.report_adapt_setting
WHERE report_adapt_id = %s;"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (adapt_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def get_report_adapt(adapt_id, adapt_type):
    "Returns the report customizations"
    script = """
SELECT 
    layout_row,
    combo1_index,
    combo2_index,
    widget_value
FROM system.report_adapt_setting
WHERE report_adapt_id = %s AND adapt_type = %s
ORDER BY layout_row;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (adapt_id, adapt_type))
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def set_report_adapt(adapt_id,
                         adapt_type,
                         layout_row,
                         combo1_index,
                         combo2_index,
                         widget_value):
    "Set the view definition"
    script = """
INSERT INTO system.report_adapt_setting (
    report_adapt_id, 
    adapt__type, 
    layout_row, 
    combo1_index, 
    combo2_index, 
    widget_value)
VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT ON CONSTRAINT report_adapt_setting_pkey DO 
UPDATE
SET combo1_index = %s,
    combo2_index = %s,
    widget_value = %s;"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (adapt_id,
                                     adapt_type,
                                     layout_row,
                                     combo1_index,
                                     combo2_index,
                                     widget_value,
                                     combo1_index,
                                     combo2_index,
                                     widget_value))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def delete_report_adapt(adapt_id):
    "Delete report adapt"
    script = """
DELETE FROM system.report_adapt
WHERE report_adapt_id = %s;"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (adapt_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def create_new_adapt(report_id, adapt_desc):
    "Create a new customization"
    script = """
INSERT INTO system.report_adapt (
    report_adapt_id, 
    description)
VALUES (%s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (report_id, adapt_desc))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def report_class_adapt_list(class_code):
    "Return id and description of all the report customizations of the input class"
    script1 = """
SELECT 
    ra.report_id, 
    ra.description
FROM system.report_adapt ra
JOIN system.report r ON ra.report_id = r.report_id
WHERE r.report_class = %s
ORDER BY ra.class_sorting;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script1, (class_code,))
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def report_adapt_sorting(adapt_id):
    "Returns the report customization sorting index"
    script = """
SELECT 
    class_sorting
FROM system.report_adapt
WHERE report_adapt_id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (adapt_id,))
            if cur.rowcount == 1:
                return cur.fetchone()[0]
            else:
                return 0
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def set_report_adapt_sorting(adapt_id, sorting):
    "Set customization sorting index"
    script = """
UPDATE system.report_adapt
SET class_sorting = %s
WHERE report_adapt_id = %s;"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (sorting, adapt_id))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))


def report_list(report_class, l10n, null=False):
    "Return code and description of all reports of l10n localization or en_US"
    script = """
SELECT 
    report_id, 
    description
FROM system.report
WHERE 
    report_class = %s AND
    l10n = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (report_class, l10n))
            records = cur.fetchall()
            return [(None, '')] + records if null else records
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def report_description(report_id):
    "Return the report description of report code of l10n localization or en_US"
    script = """
SELECT 
    description
FROM system.report
WHERE report_id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (report_id,))
            if cur.rowcount:
                return cur.fetchone()[0]
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def report_xml(adapt_id):
    "Report XML definition of the report for required report customization"
    script = """
SELECT 
    r.xml_data
FROM system.report_adapt ra
JOIN system.report r ON ra.report_id = r.id
WHERE ra.report_id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (adapt_id,))
            if cur.rowcount == 1:
                return cur.fetchone()[0]
            else:
                return (None,)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def report_id_xml(report_id):
    script = """
SELECT 
    xml_data
FROM system.report
WHERE report_id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (report_id,))
            if cur.rowcount == 1:
                return cur.fetchone()[0]
            else:
                return (None,)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def report_query(report, condition=None, sorting=None):
    "Returns dataset from report query/where/order by and dynamic where/orderby clauses"
    # remove trailing ; if any
    if not report.query:
        return
    query = report.query.strip()
    script = query if query[-1] != ';' else query[:-1]
    # parameters
    if report.parameter:
        for i in report.parameter:
            if isinstance(report.parameter[i], tuple):
                script = script.replace(f"{{{{{i}}}}}", str(report.parameter[i][0]))
            else:
                script = script.replace(f"{{{{{i}}}}}", str(report.parameter[i]))
    # fixed where clause
    if report.query_where:
        script += f"\nWHERE {report.query_where}"
    # construct dynamic where clause
    # args must be a list, conditions can have the same field
    args = []
    if condition:
        if not report.query_where:
            script += "\nWHERE "
        else:
            script += ' AND '
        script += f"{' AND '.join([i[0] for i in condition])}"
        args += [i[1] for i in condition if i[1] is not None] # for unary operant es. IS NULL, IS NOT NULL
    # fixed order by
    if report.query_order_by:
        script += f"\nORDER BY {report.query_order_by}"
    # construct dynamic order by clause
    if sorting:
        if not report.query_order_by:
            script += "\nORDER BY "
        script += f"{', '.join(sorting)}"
    script += ";"
    # execute query and returns result set
    print(script)
    print(args)
    try:
        with appconn.cursor() as cur:
            #print(cur.mogrify(script, args))
            cur.execute(script, args)
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

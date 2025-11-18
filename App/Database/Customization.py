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

"""Database - Customizations



"""

# psycopg
import psycopg

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.Connect import appconn



def get_itemview_customization(setting=False):
    "Returns all the item views customizations"
    if not setting:
        script = """SELECT id, description, itemview_class, is_default_for_class
FROM system.itemview_customize
ORDER BY id"""
    else:
        script = """SELECT view_id, column_number, sorting, is_visible, size
FROM system.itemview_customize_setting
ORDER BY view_id, column_number;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

#def delete_itemview_customization():
    #"Delete all itemview customizations"
    #s1 = "DELETE FROM system.itemview_customize_setting;"
    #s2 = "DELETE FROM system.itemview_customize;"
    #try:
        #with appconn.conn:
            #with appconn.cursor() as cur:
                #for script in s1, s2:
                    #cur.execute(script)
    #except psycopg2.Error as er:
        #raise PyAppDBError(er.pgcode, er.pgerror)

def set_itemview_customize(vid, vdes, vclass, vdef):
    "Set all the item views customizations"
    script = """
DELETE FROM system.itemview_customize WHERE id = %s;
INSERT INTO system.itemview_customize (
        id,
        description,
        itemview_class,
        is_default_for_class)
VALUES (%s, %s, %s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (vid, vid, vdes, vclass, vdef))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def set_itemview_customize_setting(vid, vcol, vsort, vvis, vsize):
    "Set all the item views customizations settings"
    script = """
INSERT INTO system.itemview_customize_setting (
    view_id,
    column_number,
    sorting,
    is_visible,
    size)
VALUES (%s, %s, %s, %s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (vid, vcol, vsort, vvis, vsize))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def get_sortfilter_customization(setting=False):
    "Returns all the sort filter customizations"
    if not setting:
        script = """
SELECT id, description, sortfilter_class, class_sorting
FROM system.sortfilter_customize
ORDER BY id;"""
    else:
        script = """
SELECT sortfilter_id, element_type, layout_row, combo1_index, combo2_index, widget_value
FROM system.sortfilter_customize_setting
ORDER BY sortfilter_id, element_type, layout_row;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

#def delete_sortfilter_customization():
    #"Delete all itemview customizations"
    #s1 = "DELETE FROM system.sortfilter_customize_setting;"
    #s2 = "DELETE FROM system.sortfilter_customize;"
    #try:
        #with appconn.conn:
            #with appconn.cursor() as cur:
                #for script in s1, s2:
                    #cur.execute(script)
    #except psycopg2.Error as er:
        #raise PyAppDBError(er.pgcode, er.pgerror)

def set_sortfilter_customize(sid, sdes, sclass, sdef):
    "Set all the item views customizations"
    script = """
DELETE FROM system.sortfilter_customize WHERE id = %s;
INSERT INTO system.sortfilter_customize (
    id,
    description,
    sortfilter_class,
    class_sorting)
VALUES (%s, %s, %s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (sid, sid, sdes, sclass, sdef))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def set_sortfilter_customize_setting(sid, selem, slrow, scmb1, scmb2, svv):
    "Set all the item views customizations settings"
    script = """
INSERT INTO system.sortfilter_customize_setting (
    sortfilter_id,
    element_type,
    layout_row,
    combo1_index,
    combo2_index,
    widget_value)
VALUES (%s, %s, %s, %s, %s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (sid, selem, slrow, scmb1, scmb2, svv))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def get_report_customization(setting=False):
    "Returns all the report customizations"
    if not setting:
        script = """
SELECT id, report_code, description, class_sorting
FROM system.report_customize
ORDER BY id;"""
    else:
        script = """
SELECT customize_id, customize_type, layout_row, combo1_index, combo2_index, widget_value
FROM system.report_customize_setting
ORDER BY customize_id, customize_type, layout_row;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

#def delete_report_customization():
    #"Delete all itemview customizations"
    #s1 = "DELETE FROM system.report_customize_setting;"
    #s2 = "DELETE FROM system.report_customize;"
    #try:
        #with appconn.conn:
            #with appconn.cursor() as cur:
                #for script in s1, s2:
                    #cur.execute(script)
    #except psycopg2.Error as er:
        #raise PyAppDBError(er.pgcode, er.pgerror)

def set_report_customize(rid, rrc, rdes, rclass):
    "Set all the report customizations"
    script = """
DELETE FROM system.report_customize WHERE id = %s;
INSERT INTO system.report_customize (
    id,
    report_code,
    description,
    class_sorting)
VALUES (%s, %s, %s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (rid, rid, rrc, rdes, rclass))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def set_report_customize_setting(rcid, rctyp, rlrow, rcmb1, rcmb2, rvv):
    "Set all the item views customizations settings"
    script = """
INSERT INTO system.report_customize_setting (
    customize_id,
    customize_type,
    layout_row,
    combo1_index,
    combo2_index,
    widget_value)
VALUES (%s, %s, %s, %s, %s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (rcid, rctyp, rlrow, rcmb1, rcmb2, rvv))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def clear_customization(custtype):
    "Clear customizations"
    scriptS = """
DELETE FROM system.sortfilter_customize;
ALTER TABLE system.sortfilter_customize ALTER COLUMN id RESTART WITH 1;"""
    scriptI = """
DELETE FROM system.itemview_customize;
ALTER TABLE system.itemview_customize ALTER COLUMN id RESTART WITH 1;"""
    scriptR = """
DELETE FROM system.report_customize;
ALTER TABLE system.report_customize ALTER COLUMN id RESTART WITH 1;"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                if custtype == 'S':
                    cur.execute(scriptS)
                if custtype == 'I':
                    cur.execute(scriptI)
                if custtype == 'R':
                    cur.execute(scriptR)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def update_identity():
    "Update identity value to last present in all customization tables"
    script = """DO $$
DECLARE
i int;
t text;
BEGIN
FOREACH t IN ARRAY ARRAY['system.itemview_customize',
                         'system.sortfilter_customize',
                         'system.report_customize']
    LOOP
	    EXECUTE format('SELECT coalesce(max(id), 0) + 1 FROM %s', t) INTO i;
	    EXECUTE format('ALTER TABLE %s ALTER COLUMN id RESTART WITH %s', t, i) ;
    END LOOP;
END;
$$
language plpgsql;"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))


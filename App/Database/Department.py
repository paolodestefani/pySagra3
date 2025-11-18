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

"""Database - Department

"""

# psycopg
import psycopg

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.Connect import appconn



def department_list(only_active=True, include_menu=False):
    "Get a list of active departments or all departments"
    where = []
    where.append('company_id = system.pa_current_company()')
    if only_active is True:
        where.append('is_obsolete IS false')
    if include_menu is False:
        where.append('is_menu_container IS false')
    if where:
        script = (f"""
SELECT department_id, description
FROM department """
f"""WHERE {' AND '.join(where)} """
f"""ORDER BY sorting;""")
    else:
        script = """
SELECT department_id, description
FROM department
WHERE company_id = system.pa_current_company()
ORDER BY sorting;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def get_department(desc):
    "Returns department id of given department description"
    script = """
SELECT department_id 
FROM department 
WHERE 
    company_id = system.pa_current_company()
    AND description = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (desc,))
            return cur.fetchall()[0]
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def department_desc(dep):
    "Returns department description of given department id"
    script = """
SELECT description 
FROM department 
WHERE department_id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (dep,))
            return cur.fetchone()[0]
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def get_department_printer_class(dep):
    "Returns the printer class for dep department"
    script = """
SELECT printer_class
FROM department
WHERE 
    department_id = %s 
    AND is_obsolete IS false 
    AND is_not_managed IS false;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (dep,))
            if cur.rowcount:
                return cur.fetchone()[0]
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def department_takeaway_list():
    "Returns a list of departments enabled for take away"
    script = """
SELECT description 
FROM department 
WHERE
    company_id = system.pa_current_company()
    AND is_for_takeaway IS True;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            if cur.rowcount:
                return [i[0] for i in cur]
            else:
                return []
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)

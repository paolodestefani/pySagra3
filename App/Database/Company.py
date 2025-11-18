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

"""Company

This module provide companies database functions


"""

# psycopg
import psycopg

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.Connect import appconn



def max_company_code():
    "Return current used max company code"
    script = """
SELECT 
    max(company_id) 
FROM system.company;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchone()[0]
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def company_is_in_use(company):
    "Return True if the company is currently in use"
    script = """
SELECT company_id 
FROM system.connection 
WHERE company_id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (company,))
            return bool(cur.rowcount)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def create_company(company_id, company_desc, company_image):
    "Create a new company with the given parameters"
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute('SELECT system.pa_company_create(%s, %s, %s, %s);',
                            (company_id,
                             company_desc,
                             False,  # system company always false
                             company_image))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def drop_company(company_id):
    "Drop company"
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute('SELECT system.pa_company_drop(%s)', (company_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def set_company_access(company_id, user_code, profile_code, menu_code, toolbar_code):
    "Set access company for one user to the given company"
    script = """
INSERT INTO system.app_user_company (
    company_id,
    app_user_code,
    profile_code,
    menu_code,
    toolbar_code)
VALUES (%s, %s, %s, %s, %s);"""
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (company_id, user_code, profile_code, menu_code, toolbar_code))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def company_list():
    "Return available companies in current database"
    script = """
SELECT 
    company_id, 
    description 
FROM system.company;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

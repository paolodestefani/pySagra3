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

"""Database - Table


"""

# psycopg
import psycopg

# application modules
from App import session
from App.Database.Exceptions import PyAppDBError
from App.Database.Connect import appconn



def table_list():
    "Returns a list of available table codes"
    script = """
    SELECT 
        table_code,
        pos_row,
        pos_column,
        text_color,
        background_color
    FROM company.stand_table
    WHERE company_id = %s AND is_obsolete IS false;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (session['current_company'],))
            return cur.fetchall()
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)

def table_delete():
    "Delete all tables"
    script = """
    DELETE FROM company.stand_table 
    WHERE company_id = %s;"""
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script, (session['current_company'],))
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)

def table_exists(table_code):
    "Returns True if the provided table list exists"
    script = """
    SELECT table_code
    FROM stand_table
    WHERE company_id = %s AND table_code = %s AND is_obsolete IS false;"""
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script, (session['current_company'], table_code))
                if cur.rowcount == 0:
                    return False
                else:
                    return True
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)


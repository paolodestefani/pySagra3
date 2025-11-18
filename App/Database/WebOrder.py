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

"""Database - WebOrder

"""

# psycopg
import psycopg

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.Connect import appconn



def get_web_order_header(order_id):
    "Get web order header of given id"
    script = """SELECT delivery, table_num, customer_name, covers, total_amount, processed
FROM web_order_header
WHERE id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (order_id,))
            if cur.rowcount:
                return cur.fetchall()[0]  # must be only one record
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)


def get_web_order_details(order_id):
    "Get web order details of given id"
    script = """SELECT item, quantity
FROM web_order_detail
WHERE id_header = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (order_id,))
            if cur.rowcount:
                return cur.fetchall()

    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)

def set_web_order_processed(order_id):
    "Set web order as processed"
    script = """UPDATE web_order_header
SET processed = true
WHERE id = %s;"""
    try:
        with appconn.conn:
            with appconn.cursor() as cur:
                cur.execute(script, (order_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)

def delete_web_order(include_all=False):
    "Delete web order"
    script = """DELETE FROM web_order_header"""
    if not include_all:
        script += """ WHERE processed IS true"""
    script += ";"
    try:
        with appconn.conn:
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)

def web_order_totals():
    "Calc web order totals"
    script = """SELECT count(*),
    count(CASE WHEN processed IS true THEN 1 END),
    count(CASE WHEN processed IS false THEN 1 END)
FROM web_order_header;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script)
            return cur.fetchone()
    except psycopg.Error as er:
        raise PyAppDBError(er.pgcode, er.pgerror)

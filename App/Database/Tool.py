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

"""Database - utilities

This module provide a set of utility functions to interact with the archive
database

"""

# psycopg
import psycopg

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.Connect import appconn



def delete_order(event_id):
    "Delete all orders of the given event"
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute('SELECT company.delete_event_order(%s);', (event_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def unload_rebuild(event_id):
    "Unload rebuild for the given event"
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute('SELECT company.unload_rebuild(%s);', (event_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def numbering_rebuild(event_id):
    "Numbering rebuild for the given event"
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute('SELECT company.numbering_rebuild(%s);', (event_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))

def mark_order_as_processed(event_id):
    "Mark all unprocessed orders as processed ad order date"
    # order headers are updated by the trigger
    # no need to filter by company id as event_id is unique per company
    script = """
UPDATE company.order_header_department
SET fullfillment_date = oh.date_time
FROM company.order_header_department ohd
JOIN company.order_header oh ON ohd.order_header_id = oh.order_header_id
WHERE 
    oh.event_id = %s 
    AND ohd.fullfillment_date is null;"""
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script, (event_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
    
def delete_all_orders():
    "Delete ALL orders for current company"
    script = """
DELETE FROM order_header
WHERE company_id = pa_current_company();
DELETE FROM numbering
WHERE company_id = pa_current_company();
"""
    # linked tables (oreder_header_department, order_detail, etc.
    # are automatically deleted from db cascade constraints
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_web_orders():
    "Delete ALL web orders for current company"
    script = """
DELETE FROM web_order_header
WHERE company_id = pa_current_company();"""
    # linked table web_order_detail is automatically deleted from db cascade constraints
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_inventory():
    "Delete ALL stock inventory records for current company"
    script = """
DELETE FROM stock_inventory
WHERE company_id = pa_current_company();"""
    # linked table web_order_detail is automatically deleted from db cascade constraints
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_events():
    "Delete ALL events for current company"
    script = """
DELETE FROM event
WHERE company_id = pa_current_company();"""
    # linked tables (all about orders) are automatically deleted from db cascade constraints
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_price_lists():
    "Delete ALL price lists for current company"
    script = """
DELETE FROM price_list
WHERE company_id = pa_current_company();"""
    # linked table (price_list_detail) is automatically deleted from db cascade constraints
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_items():
    "Delete ALL items for current company"
    script = """
DELETE FROM item
WHERE company_id = pa_current_company();"""
    # linked table (item_part, item_variant) are automatically deleted from db cascade constraints
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_departments():
    "Delete ALL departments for current company"
    script = """
DELETE FROM department
WHERE company_id = pa_current_company();"""
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_tables():
    "Delete ALL tables for current company"
    script = """
DELETE FROM numbered_table
WHERE company_id = pa_current_company();"""
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_cash_desks():
    "Delete ALL cash desks for current company"
    script = """
DELETE FROM cash_desk
WHERE company_id = pa_current_company();"""
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    
def delete_all_printer_classes():
    "Delete ALL printer classes for current company"
    script = """
DELETE FROM printer_class
WHERE company_id = pa_current_company();"""
    # linked table (printer_class_printer) is automatically deleted from db cascade constraints
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script)
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    

def copy_cash_desks(from_company_id):
    "Copy ALL the cash desks from another company to current compani"
    script = """
INSERT INTO cash_desk (
    company_id,
    computer,
    cash_desk_description,
    note)
SElECT
    pa_current_company(),
    computer,
    cash_desk_description,
    note
FROM cash_desk
WHERE company_id = %s;"""
    # linked table (printer_class_printer) is automatically deleted from db cascade constraints
    try:
        with appconn.cursor() as cur:
            with appconn.transaction():
                cur.execute(script, (from_company_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))
    

    
    

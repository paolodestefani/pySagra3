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

"""Database - Order management



"""

# psycopg
import psycopg

# PySide6
from PySide6.QtCore import QTime

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.Utility import Record, RecordSet
from App.Database.Connect import appconn
from App.Database.Setting import SettingClass
from App.Database.Item import is_menu
from App.Database.Item import get_menu_items
from App.Database.Item import get_item_dep
from App.Database.Item import has_stock_management
from App.Database.Item import get_item_stock_level
from App.Database.Item import get_item_desc
from App.Database.Department import department_desc
from App.Database.Event import get_event_from_date



def get_order_number(event_id):
    "Returns the next available order number"
    # actually we don't need to filter company_id as event_id is unique across companies
    script = """
SELECT 
    current_value + 1 
FROM company.numbering 
WHERE 
    company_id = pa_current_company()
    AND sequence_type = 'ORDERNUM'
    AND event_id = %s;"""
    # numbering table is updated by a trigger
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (event_id,))
            if cur.rowcount:
                number = cur.fetchone()[0]
            else:
                number = 1
            return number
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))


def get_orders_issued(event_id, date, day_part):
    "Returns the issued number of orders for day and day part"
     # actually we don't need to filter company_id as event_id is unique across companies
    script = """
SELECT current_value
FROM company.numbering
WHERE 
    company_id = pa_current_company()
    AND sequence_type = 'ORDERS' 
    AND event_id = %s 
    AND event_date = %s 
    AND day_part = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (event_id, date, day_part))
            if cur.rowcount:
                number = cur.fetchone()[0]
            else:
                number = 0
            return number
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))


def get_order_header_department_details(order_id):
    "Returns params of the given order header department"
    # actually we don't need to filter company_id as event_id is unique across companies
    script = """
SELECT 
    ohd.id,
    oh.id,
    oh.order_number,
    oh.order_date,
    oh.order_time,
    oh.delivery,
    oh.table_num,
    oh.customer_name,
    ohd.department_id,
    dep.description,
    ohd.fullfillment_date
FROM company.order_header_department ohd
JOIN company.order_header oh ON ohd.header_id = oh.id
JOIN company.department dep ON ohd.department_id = dep.id
WHERE 
    company_id = pa_current_company()
    AND ohd.id = %s;"""
    try:
        with appconn.cursor() as cur:
            cur.execute(script, (order_id,))
            return cur.fetchone()
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))


def update_order_header_department_status(order_id, mark=True):
    "Set to true processed flag of given order header department_id"
    # actually we don't need to filter company_id as order_id is unique across companies
    if mark:  # set datetime or null to unmark
        script = """
UPDATE company.order_header_department
SET fullfillment_date = CURRENT_TIMESTAMP
WHERE
    company_id = pa_current_company()
    AND id = %s;"""
    else:
        script = """
UPDATE company.order_header_department
SET fullfillment_date = Null
WHERE
    company_id = pa_current_company()
    AND id = %s;"""
    try:
        with appconn.transaction():
            with appconn.cursor() as cur:
                cur.execute(script, (order_id,))
    except psycopg.Error as er:
        raise PyAppDBError(er.diag.sqlstate, str(er))


class Order():
    "A order header and details"

    def __init__(self):
        self.header = Record('company.order_header', ('id',))
        self.details = RecordSet('company.order_detail', ('id',))
        self.depnote = {} # dict(dep: note)
        
    def out_of_stock(self):
        "Returns a list of out of stock items"
        event_id = get_event_from_date(self.header['date_time'])[0]
        out_of_stock = []
        for i in self.details:
            if has_stock_management(i['item_id']):
                if get_item_stock_level(event_id, i['item_id']) - i['quantity'] < 0:
                    out_of_stock.append(get_item_desc(i['item_id']))
        return out_of_stock

    def insert(self):
        "Insert everything after completed the order"
        headersdep = RecordSet('company.order_header_department', ('id',))
        detailsdep = RecordSet('company.order_detail_department', ('id',))
        # set event and order number on header
        self.header['event_id'] = get_event_from_date(self.header['date_time'])[0]
        self.header['order_number'] = get_order_number(self.header['event_id'])
        # from details create an intermediate detail list resolving menu items
        # resolve menu
        intermediate = []
        for i in self.details: # also have to remove price and amount
            if is_menu(i['item_id']):
                for p, q in get_menu_items(i['item_id']):
                    r = dict()
                    r['item_id'] = p
                    r['variants'] = None # menu part can not have variants
                    r['quantity'] = i['quantity'] * q
                    intermediate.append(r)
            else:
                r = dict()
                r['item_id'] = i['item_id']
                r['variants'] = i['variants']
                r['quantity'] = i['quantity']
                intermediate.append(r)
        # sum qty of same item that can come out from previous elaboration
        detail = []
        for i in intermediate:
            if (i['item_id'], i['variants']) in [(r['item_id'], r['variants']) for r in detail]:
                for n, j in enumerate([(r['item_id'], r['variants']) for r in detail]):
                    if (i['item_id'], i['variants']) == j:
                        detail[n]['quantity'] += i['quantity']
            else:
                detail.append(i.copy())
        # assign department
        for i in detail:
            r = dict()
            r['event_id'] = self.header['event_id']
            r['department_id'] = get_item_dep(i['item_id'])
            r['item_id'] = i['item_id']
            r['variants'] = i['variants']
            r['quantity'] = i['quantity']
            detailsdep.append(r)
        # generate headersdep and detailsdep
        # compute used departments set and create headersdep
        used_dep = {get_item_dep(i['item_id']) for i in detail} # set
        used_dep_desc = [department_desc(i) for i in used_dep]
        for i in used_dep:
            r = dict()
            r['department_id'] = i
            r['note'] = self.depnote.get(i)
            others = list(used_dep_desc)
            others.remove(department_desc(i))
            if others:
                r['other_departments'] = ", ".join(others)
            else:
                r['other_departments'] = None
            headersdep.append(r)
        # set date, statistical date and date part
        setting = SettingClass()
        # order date and time set in insert for for management of event date change
        self.header['order_date'] = self.header['date_time'].date()
        self.header['order_time'] = self.header['date_time'].time()
        # if time between 0.0.0 and lunch start time stat date is the day before date part is dinner
        if QTime(0, 0) <= self.header['order_time'] < QTime(setting['lunch_start_time'], 0):
            # dinner of the day before
            self.header['stat_order_date'] = self.header['order_date'].addDays(-1)
            self.header['stat_order_day_part'] = 'D'
        elif QTime(setting['lunch_start_time'], 0) <= self.header['order_time'] < QTime(setting['dinner_start_time'], 0):
            # lunch
            self.header['stat_order_date'] = self.header['order_date']
            self.header['stat_order_day_part'] = 'L'
        else:
            # dinner of the current date
            self.header['stat_order_date'] = self.header['order_date']
            self.header['stat_order_day_part'] = 'D'
        # set status and fullfillment date if required
        if not setting['manage_order_progress']:
            self.header['status'] = 'P'  # set as already processed
            self.header['fullfillment_date'] = self.header['date_time']
            for i in headersdep:
                i['fullfillment_date'] = self.header['fullfillment_date']
        # insert
        try:
            self.header.insert_record()
            t = self.header['id']
            ev = self.header['event_id']
            for i in headersdep:
                i['header_id'] = t
            for i in self.details:
                i['header_id'] = t
            for i in detailsdep:
                i['header_id'] = t
                i['event_id'] = ev
                i['event_date'] = self.header['stat_order_date']
                i['day_part'] = self.header['stat_order_day_part']
            headersdep.insert_records()
            self.details.insert_records()
            detailsdep.insert_records()
        except PyAppDBError as er:
            appconn.rollback()
            raise PyAppDBError(er)
        else:
            appconn.commit()
            return t, used_dep

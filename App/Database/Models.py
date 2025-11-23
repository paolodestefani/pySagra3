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

"""SQL Models

"""

# standard library
import operator
import decimal

# psycopg
import psycopg

# PySide6
from PySide6.QtCore import QObject
from PySide6.QtCore import Qt
from PySide6.QtCore import QDate
from PySide6.QtCore import QTime
from PySide6.QtCore import QDateTime
from PySide6.QtCore import Signal
#from PyQt5.QtCore import QAbstractItemModel
#from PyQt5.QtCore import QAbstractTableModel
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QFont

# application modules
from App import session
from App.Database.Exceptions import PyAppDBError
#from App.Database.Psycopg import DEFAULT
from App.Database.Connect import appconn
from App.Database.AbstractModels.TableModel import QueryModel
from App.Database.AbstractModels.TableModel import QueryWithParamsModel
from App.Database.AbstractModels.TableModel import TableModel
from App.Database.AbstractModels.TreeModel import TreeModel
from App.Database.Company import company_is_in_use
from App.Database.Statistics import statistics_configuration
from App.Database.Statistics import statistics_configuration_columns
from App.Database.Statistics import statistics_configuration_totals_columns
from App.Database.CodeDescriptionList import department_cdl
from App.Database.CodeDescriptionList import event_cdl
from App.Database.CodeDescriptionList import item_salable_cdl
from App.Database.CodeDescriptionList import item_all_cdl
from App.System.Utility import _tr


UPDATED, INSERTED, DELETED = range(3)


class MenuItemTreeModel(TreeModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = "system.menu_item"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("parent", _tr('Models', 'Menu'), False, 'str'),
                        ("child", _tr('Models', 'User description'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("item_type", _tr('Models', 'Item type'), False, 'str'),
                        ("action", _tr('Models', 'Action'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("parent", "child")
        self.parentField = "parent"
        self.parentFieldColumn = 0
        self.childField = "child"
        self.childFieldColumn = 1
        # sql order by clause, plain sql string without ORDER BY
        # self.addOrderBy("parent")
        # self.addOrderBy("sorting")


class ToolbarItemTreeModel(TreeModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = "system.toolbar_item"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("parent", _tr('Models', 'Menu'), False, 'str'),
                        ("child", _tr('Models', 'User description'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("item_type", _tr('Models', 'Item type'), False, 'str'),
                        ("action", _tr('Models', 'Action'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("parent", "child")
        self.parentField = "parent"
        self.parentFieldColumn = 0
        self.childField = "child"
        self.childFieldColumn = 1
        # sql order by clause, plain sql string without ORDER BY
        # self.addOrderBy("parent")
        # self.addOrderBy("sorting")


class ConnectionModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    a.session_id,
    a.access_date,
    a.db_user_name,
    a.app_user_code,
    a.client_name,
    a.client_ip,
    a.client_port,
    a.company_id,
    b.description,
    a.profile_code
FROM system.connection a
LEFT JOIN system.company b ON a.company_id = b.company_id;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("a.session_id", _tr('Models', 'Session ID'), True, 'int'),
                        ("a.access_date,", _tr('Models', 'Access Date'), True, 'datetime'),
                        ("a.db_user_name", _tr('Models', 'Database User'), True, 'str'),
                        ("a.app_user_code", _tr('Models', 'Application User'), True, 'str'),
                        ("a.client_name", _tr('Models', 'Client name'), True, 'str'),
                        ("a.client_ip", _tr('Models', 'Client IP'), True, 'str'),
                        ("a.client_port", _tr('Models', 'Client Port'), True, 'int'),
                        ("a.company_id", _tr('Models', 'Company'), True, 'int'),
                        ("b.description", _tr('Models', 'Company Description'), True, 'str'),
                        ("a.profile_code", _tr('Models', 'Profile'), True, 'str'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Connection model')
        self.addOrderBy('a.access_date DESC')


class ConnectionHistoryModel(QueryModel):
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    session_id,
    login_datetime,
    logout_datetime,
    db_user_name,
    app_user_code,
    client_name,
    client_ip,
    client_port,
    company_desc,
    profile_code
FROM system.connection_history;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, float, str, date, datetime, None = no filter
        self.columns = (("session_id", _tr('Models', 'Session ID'), True, 'int'),
                        ("login_datetime", _tr('Models', 'Login Date'), True, 'datetime'),
                        ("logout_datetime", _tr('Models', 'Logout Date'), True, 'datetime'),
                        ("db_user_name", _tr('Models', 'Database User'), True, 'str'),
                        ("app_user_code", _tr('Models', 'Application User'), True, 'str'),
                        ("client_name", _tr('Models', 'Client name'), True, 'str'),
                        ("client_ip", _tr('Models', 'Client IP'), True, 'str'),
                        ("client_port", _tr('Models', 'Client Port'), True, 'int'),
                        ("company_desc", _tr('Models', 'Company Description'), True, 'str'),
                        ("profile_code", _tr('Models', 'Profile'), True, 'str'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Connection history model')
        self.addOrderBy(('login_datetime DESC', 'session_id'))
        

class CompanyIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    company_id,
    description,
    is_system_object,
    company_image,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM system.company;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("company_id", _tr('Models', 'Company ID'), True, 'int'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("company_image", _tr('Models', 'Picture'), False, None),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Company index model')
        self.addOrderBy('company_id ASC')
        

class CompanyModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.company"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("company_id", _tr('Models', 'Company ID'), True, 'int'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("company_image", _tr('Models', 'Picture'), False, None),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("company_id",)
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy('company_id')
        
    def submitAll(self) -> None:
        # check if delete request of a in use company
        for row in self.toDelete:
            company = self.toDelete[row]['pkey']['company_id']
            if company_is_in_use(company):
                msg = _tr('Company', "Cannot delete company {} because currently in use").format(company)
                raise PyAppDBError(0, msg)
        # otherwise copntinue
        super().submitAll()


class UserIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    user_code,
    description,
    user_image,
    is_system_object,
    is_admin,
    can_edit_views,
    can_edit_sortfilters,
    can_edit_reports,
    l10n,
    last_login,
    last_company_desc,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM system.app_user;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("user_code", _tr('Models', 'User'), False, 'str'),
                        ("description", _tr('Models', 'User description'), False, 'str'),
                        ("user_image", _tr('Models', 'Image'), False, None),
                        ("is_system_object", _tr('Models', 'System user'), True, 'bool'),
                        ("is_admin", _tr('Models', 'Administrator'), False, 'bool'),
                        ("can_edit_views", _tr('Models', 'Can edit views'), False, 'bool'),
                        ("can_edit_sortfilters", _tr('Models', 'Can edit sortfilters'), False, 'bool'),
                        ("can_edit_reports", _tr('Models', 'Can edit reports'), False, 'bool'),
                        ("l10n", _tr('Models', 'Language'), False, 'str'),
                        ("last_login", _tr('Models', 'Last login'), True, 'datetime'),
                        ("last_company_desc", _tr('Models', 'Last company'), True, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('User index model')
        self.addOrderBy('user_code ASC')
        

class UserModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.app_user"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("user_code", _tr('Models', 'User'), False, 'str'),
                        ("description", _tr('Models', 'User description'), False, 'str'),
                        ("user_image", _tr('Models', 'Image'), False, None),
                        ("user_password", _tr('Models', 'Password'), False, 'str'),
                        ("password_date", _tr('Models', 'Last change'), True, 'datetime'),
                        ("new_password_required", _tr('Models', 'Force password change'), False, 'bool'),
                        ("is_system_object", _tr('Models', 'System user'), True, 'bool'),
                        ("is_admin", _tr('Models', 'Administrator'), False, 'bool'),
                        ("can_edit_views", _tr('Models', 'Can edit views'), False, 'bool'),
                        ("can_edit_sortfilters", _tr('Models', 'Can edit sortfilters'), False, 'bool'),
                        ("can_edit_reports", _tr('Models', 'Can edit reports'), False, 'bool'),
                        ("l10n", _tr('Models', 'Language'), False, 'str'),
                        ("last_company_desc", _tr('Models', 'Last company'), True, 'str'),
                        ("last_login", _tr('Models', 'Last login'), True, 'datetime'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("user_code",)
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("is_system_object DESC")
        self.addOrderBy("user_code")


class UserCompanyModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.app_user_company"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("company_id", _tr('Models', 'Company ID'), False, 'int'),
                        ("app_user_code", _tr('Models', 'User'), False, 'str'),
                        ("profile_code", _tr('Models', 'Profile'), False, 'str'),
                        ("menu_code", _tr('Models', 'Menu'), False, 'str'),
                        ("toolbar_code", _tr('Models', 'Toolbar'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("app_user_code", "company_id")
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("company_id")
        self.addOrderBy("app_user_code")


class UserCompanyModelReferenceCompany(UserCompanyModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        # master/detail relation {table column: reference field}
        self.foreignKey = {'company_id': 'company_id'}


class UserCompanyModelReferenceUser(UserCompanyModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        # master/detail relation {table column: reference field}
        self.foreignKey = {'app_user_code': 'app_user_code'}


class ProfileIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    profile_code,
    description,
    is_system_object,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM system.profile;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("profile_code", _tr('Models', 'Profile'), True, 'int'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Profile index model')
        self.addOrderBy('profile_code ASC')
        

class ProfileModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.profile"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("profile_code", _tr('Models', 'Profile'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("profile_code",)
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("profile_code")
        self.newRecordDefault = {'profile_code': None, 
                                 'description': '',
                                 'is_system_object': False,
                                 'created_by': '',
                                 'created_at': None,
                                 'updated_by': '',
                                 'updated_at': None}


class ProfileActionModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.profile_action"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("profile_code", _tr('Models', 'Profile'), False, 'str'),
                        ("action", _tr('Models', 'Action'), False, 'str'),
                        ("auth", _tr('Models', 'Authorization'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("profile_code", "action")
        # master/detail relation {table field: reference field}
        self.foreignKey = {'profile_code': 'profile_code'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("action")


class MenuIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    menu_code,
    description,
    is_system_object,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM system.menu;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("menu_code", _tr('Models', 'Menu'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Menu index model')
        self.addOrderBy('menu_code ASC')
        

class MenuModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.menu"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("menu_code", _tr('Models', 'Menu'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("menu_code",)
        # sql where clause, plain sql string without WHERE
        #self.sqlWhere = ''
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("menu_code")
        

class ToolbarIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    toolbar_code,
    description,
    is_system_object,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM system.toolbar;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("toolbar_code", _tr('Models', 'Toolbar'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Toolbar index model')
        self.addOrderBy('toolbar_code ASC')
        

class ToolbarModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.toolbar"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("toolbar_code", _tr('Models', 'Code'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("is_system_object", _tr('Models', 'System'), True, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("toolbar_code",)
        # sql where clause, plain sql string without WHERE
        #self.sqlWhere = ''
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("toolbar_code")


class ReportIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT
    report_id,
    report_code,
    l10n,
    report_class,
    description,
    is_system_object,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM system.report;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (
            ("reprot_id", _tr('Models', 'ID'), True, 'int'),
            ("report_code", _tr('Models', 'Report code'), False, 'str'),
            ("l10n", _tr('Models', 'Localization'), False, 'str'),
            ("report_class", _tr('Models', 'Report class'), False, 'str'),
            ("description", _tr('Models', 'Description'), False, 'str'),
            ("is_system_object", _tr('Models', 'System'), True, 'bool'),
            ("created_by", _tr('Models', 'User Ins'), True, 'str'),
            ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
            ("updated_by", _tr('Models', 'User Update'), True, 'str'),
            ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Report index model')
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("report_id, report_code, l10n")
        

class ReportModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.report"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (
            ("report_id", _tr('Models', 'ID'), True, 'int'),
            ("report_code", _tr('Models', 'Report code'), False, 'str'),
            ("l10n", _tr('Models', 'Localization'), False, 'str'),
            ("report_class", _tr('Models', 'Report class'), False, 'str'),
            ("description", _tr('Models', 'Description'), False, 'str'),
            ("xml_data", _tr('Models', 'Report XML definition'), False, None),
            ("is_system_object", _tr('Models', 'System'), True, 'bool'),
            ("created_by", _tr('Models', 'User Ins'), True, 'str'),
            ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
            ("updated_by", _tr('Models', 'User Update'), True, 'str'),
            ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.primaryKey = ("report_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        #self.addOrderBy(("code, l10n"))


class ScriptingIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    script_id,
    class_name,
    method_name,
    trigger,
    company_id,
    is_active,
    is_system_object,
    script,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM system.python_scripting;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (
            ("sscript_id", _tr('Models', 'ID'), True, 'int'),
            ("class_name", _tr('Models', 'Class name'), False, 'str'),
            ("method_name", _tr('Models', 'Method name'), False, 'str'),
            ("trigger", _tr('Models', 'Trigger'), False, 'str'),
            ("company_id", _tr('Models', 'Company'), False, 'int'),
            ("is_active", _tr('Models', 'Active'), False, 'bool'),
            ("is_system_object", _tr('Models', 'System'), True, 'bool'),
            ("script", _tr('Models', 'Python script'), False, 'str'),
            ("created_by", _tr('Models', 'User Ins'), True, 'str'),
            ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
            ("updated_by", _tr('Models', 'User Update'), True, 'str'),
            ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        self.setRepr('Scripting index model')
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy(("class_name DESC", "method_name", "trigger"))
        
                
class ScriptingModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "system.python_scripting"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (
            ("script_id", _tr('Models', 'ID'), True, 'int'),
            ("class_name", _tr('Models', 'Class name'), False, 'str'),
            ("method_name", _tr('Models', 'Method name'), False, 'str'),
            ("trigger", _tr('Models', 'Trigger'), False, 'str'),
            ("company_id", _tr('Models', 'Company'), False, 'int'),
            ("is_active", _tr('Models', 'Active'), False, 'bool'),
            ("is_system_object", _tr('Models', 'System'), True, 'bool'),
            ("script", _tr('Models', 'Python script'), False, 'str'),
            ("created_by", _tr('Models', 'User Ins'), True, 'str'),
            ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
            ("updated_by", _tr('Models', 'User Update'), True, 'str'),
            ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("script_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("class_name, method_name, trigger")
        

class EventIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    event_id,
    description,
    start_date,
    end_date,
    price_list_id,
    image,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM company.event;"""
        # available types: int, bool, decimal2, str, date, datetime, None"""
        # model columns: (field, description, readonly, type), tuple of tuples
        self.columns = (("event_id", _tr('Models', 'ID'), True, 'int'),
                        ("description", _tr('Models', 'Event description'), False, 'str'),
                        ("start_date", _tr('Models', 'Start date'), False, 'datetime'),
                        ("end_date", _tr('Models', 'End date'), False, 'datetime'),
                        ("price_list_id", _tr('Models', 'Price list'), False, 'int'),
                        ("image", _tr('Models', 'Event image'), False, None),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        self.setRepr('Event index model')
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("event_id")


class EventModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.event"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("event_id", _tr('Models', 'ID'), True, 'int'),
                        ("description", _tr('Models', 'Event description'), False, 'str'),
                        ("start_date", _tr('Models', 'Start date'), False, 'datetime'),
                        ("end_date", _tr('Models', 'End date'), False, 'datetime'),
                        ("price_list_id", _tr('Models', 'Price list'), False, 'int'),
                        ("image", _tr('Models', 'Event image'), False, None),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("event_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("start_date DESC")


class CashDeskModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.cash_desk"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("cash_desk_id", _tr('Models', 'ID'), True, 'int'),
                        ("computer", _tr('Models', 'Computer name'), False, 'str'),
                        ("cash_desk_description", _tr('Models', 'Cash desk description'), False, 'str'),
                        ("note", _tr('Models', 'Note'), False, 'int'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("cash_desk_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        #self.foreignKey = {'class_id': 'id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("cash_desk_id")
        #self.newRecordDefault = {'is_obsolete': False,
        #                         'is_not_managed': False,
        #                         'is_for_takeaway': True}
        

class PrinterIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    printer_class_id,
    description,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM company.printer_class;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        self.columns = (("printer_class_id", _tr('Models', 'ID'), True, 'int'),
                        ("description", _tr('Models', 'Class description'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        self.setRepr('Printer index model')    
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("printer_class_id")
        

class PrinterModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.printer_class"
        # model columns: (field, description, readonly, type), tuple of tuples
        self.columns = (("printer_class_id", _tr('Models', 'ID'), True, 'int'),
                        ("description", _tr('Models', 'Class description'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("printer_class_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("printer_class_id")
        

class PrinterDetailModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.printer_class_printer"
        self.columns = (("printer_class_printer_id", _tr('Models', 'ID'), True, 'int'),
                        ("printer_class_id", _tr('Models', 'Printer class ID'), False, 'int'),
                        ("computer", _tr('Models', 'Computer'), False, 'str'),
                        ("printer", _tr('Models', 'Printer'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("printer_class_printer_id",)
        self.automaticPKey = True
        # master/detail relation {this table field: reference field}
        self.foreignKey = {'printer_class_id': 'printer_class_id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("printer_class_printer_id")
        

class DepartmentModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.department"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("department_id", _tr('Models', 'ID'), True, 'int'),
                        ("description", _tr('Models', 'Department description'), False, 'str'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("printer_class_id", _tr('Models', 'Printer class'), False, 'str'),
                        ("is_obsolete", _tr('Models', 'Is obsolete'), False, 'bool'),
                        ("is_menu_container", _tr('Models', 'Menu container'), False, 'bool'),
                        ("is_for_takeaway", _tr('Models', 'For takeaway'), False, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("department_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        #self.foreignKey = {'class_id': 'id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("department_id")
        #self.newRecordDefault = {'is_obsolete': False,
        #                         'is_not_managed': False,
        #                         'is_for_takeaway': True}
        

class StandTableModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.stand_table"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("stand_table_id", _tr('Models', 'ID'), True, 'int'),
                        ("table_code", _tr('Models', 'Table code'), False, 'str'),
                        ("pos_row", _tr('Models', 'Row'), False, 'int'),
                        ("pos_column", _tr('Models', 'Column'), False, 'int'),
                        ("text_color", _tr('Models', 'Text color'), False, 'str'),
                        ("background_color", _tr('Models', 'Background color'), False, 'str'),
                        ("is_obsolete", _tr('Models', 'Obsolete'), False, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("stand_table_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("stand_table_id")


class ItemIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    item_id,
    item_type,
    description,
    department_id,
    sorting,
    pos_row,
    pos_column,
    normal_text_color,
    normal_background_color,
    has_stock_control,
    has_unload_control,
    has_variants,
    is_kit_part,
    is_menu_part,
    is_salable,
    is_web_available,
    web_sorting,
    is_obsolete,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM company.item;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        self.columns = (("item_id", _tr('Models', 'ID'), False, 'int'),
                        ("item_type", _tr('Models', 'Item type'), False, 'str'),
                        ("description", _tr('Models', 'Item description'), False, 'str'),
                        ("department_id", _tr('Models', 'Department'), False, 'int'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("pos_row", _tr('Models', 'Row'), False, 'int'),
                        ("pos_column", _tr('Models', 'Column'), False, 'int'),
                        ("normal_text_color", _tr('Models', 'Text color'), False, 'str'),
                        ("normal_background_color", _tr('Models', 'Background color'), False, 'str'),
                        ("has_stock_control", _tr('Models', 'Stock control'), False, 'bool'),
                        ("has_unload_control", _tr('Models', 'Unload control'), False, 'bool'),
                        ("has_variants", _tr('Models', 'Variants'), False, 'bool'),
                        ("is_kit_part", _tr('Models', 'Kit part'), False, 'bool'),
                        ("is_menu_part", _tr('Models', 'Menu part'), False, 'bool'),
                        ("is_salable", _tr('Models', 'Salable'), False, 'bool'),
                        ("is_web_available", _tr('Models', 'Web available'), False, 'bool'),
                        ("web_sorting", _tr('Models', 'Web sorting'), False, 'int'),
                        ("is_obsolete", _tr('Models', 'Obsolete'), False, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        self.setRepr('Item index model')
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy(("item_id", "item_type", "description"))


class ItemModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.item"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("item_id", _tr('Models', 'ID'), False, 'int'),
                        ("item_type", _tr('Models', 'Item type'), False, 'str'),
                        ("description", _tr('Models', 'Item description'), False, 'str'),
                        ("customer_description", _tr('Models', 'Item description for customer'), False, 'str'),
                        ("department_id", _tr('Models', 'Department'), False, 'int'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("pos_row", _tr('Models', 'Row'), False, 'int'),
                        ("pos_column", _tr('Models', 'Column'), False, 'int'),
                        ("normal_text_color", _tr('Models', 'Text color'), False, 'str'),
                        ("normal_background_color", _tr('Models', 'Background color'), False, 'str'),
                        ("has_stock_control", _tr('Models', 'Stock control'), False, 'bool'),
                        ("has_unload_control", _tr('Models', 'Unload control'), False, 'bool'),
                        ("has_variants", _tr('Models', 'Variants'), False, 'bool'),
                        ("is_kit_part", _tr('Models', 'Kit part'), False, 'bool'),
                        ("is_menu_part", _tr('Models', 'Menu part'), False, 'bool'),
                        ("is_salable", _tr('Models', 'Salable'), False, 'bool'),
                        ("is_web_available", _tr('Models', 'Web available'), False, 'bool'),
                        ("web_sorting", _tr('Models', 'Web sorting'), False, 'int'),
                        ("is_obsolete", _tr('Models', 'Obsolete'), False, 'bool'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("item_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("item_id")
        # reference fields dictionary
        self.reference = {'department': department_cdl}


class ItemVariantModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.item_variant"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("item_variant_id", _tr('Models', 'ID'), False, 'int'),
                        ("item_id", _tr('Models', 'Item'), False, None),
                        ("variant_description", _tr('Models', 'Variant description'), False, 'str'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("price_delta", _tr('Models', 'Price delta'), False, 'decimal2'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("item_variant_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'item_id': 'item_id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("item_variant_id")
        self.addOrderBy("sorting")


class KitPartModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.item_part"
        self.recordType = {'item_type': 'K'}
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("item_part_id", _tr('Models', 'ID'), False, 'int'),
                        ("item_id", _tr('Models', 'Kit'), False, 'int'),
                        ("part_id", _tr('Models', 'Part'), False, 'int'),
                        ("quantity", _tr('Models', 'Quantity'), False, 'int'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("item_part_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'item_id': 'id', 'part_id': 'id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("item_part_id")


class MenuPartModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.item_part"
        self.recordType = {'item_type': 'M'}
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("item_part_id", _tr('Models', 'ID'), False, 'int'),
                        ("item_id", _tr('Models', 'Menu'), False, 'int'),
                        ("part_id", _tr('Models', 'Part'), False, 'int'),
                        ("quantity", _tr('Models', 'Quantity'), False, 'int'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("item_part_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'item_id': 'id', 'part_id': 'id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("item_part_id")


class PriceListItemModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.price_list_item"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("price_list_item_id", _tr('Models', 'ID'), False, 'int'),
                        ("price_list_id", _tr('Models', 'Price list'), False, 'int'),
                        ("item_id", _tr('Models', 'Item'), False, 'int'),
                        ("price", _tr('Models', 'Price'), False, 'decimal2'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("price_list_item_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'item_id': 'id', 'price_list_id': 'id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("price_list_item_id")


class PriceListIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    price_list_id,
    description,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM company.price_list;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        self.columns = (("price_list_id", _tr('Models', 'ID'), False, 'int'),
                        ("description", _tr('Models', 'Item description'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        self.setRepr('Price list index model')
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("price_list_id")


class PriceListModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.price_list"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("price_list_id", _tr('Models', 'ID'), False, 'int'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("price_list_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("price_list_id")


class PriceListItemModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.price_list_item"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("price_list_item_id", _tr('Models', 'ID'), False, 'int'),
                        ("price_list_id", _tr('Models', 'Price list'), False, 'int'),
                        ("item_id", _tr('Models', 'Item'), False, 'int'),
                        ("price", _tr('Models', 'Price'), False, 'decimal2'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("price_list_item_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'price_list_id': 'price_list_item_id', 'item_id': 'id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("price_list_item_id")
        # reference fields dictionary
        self.reference = {'item': item_salable_cdl}
        # list of items for sorting by description
        self.itemDescription = {k:v for k, v in item_all_cdl()}

    def sort(self, column, order=Qt.AscendingOrder):
        "Custom inplace sorting of the model for item description"
        if column != 2: # not item column
            super().sort(column, order=Qt.AscendingOrder)
            return
        # inplace list sorting
        if order == Qt.AscendingOrder:
            self.dataSet.sort(key=lambda x: self.itemDescription[x[2]])
        else:
            self.dataSet.sort(key=lambda x: self.itemDescription[x[2]], reverse=True)
        # notify about changes
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount(), self.columnCount()))


class StockInventoryModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.stock_inventory"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("stock_inventory_id", _tr('Models', 'ID'), True, 'int'),
                        ("event_id", _tr('Models', 'event'), False, 'int'),
                        ("item_id", _tr('Models', 'Item'), False, 'int'),
                        ("loaded", _tr('Models', 'Load'), False, 'decimal2'),
                        ("unloaded", _tr('Models', 'Unload'), True, 'decimal2'),
                        ("balance", _tr('Models', 'Balance'), True, 'decimal2'),
                        # (None, _tr('Models', 'New stock'), False, 'decimal2'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("stock_inventory_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("stock_inventory_id")
        self.newRecordDefault = {'loaded': 0,
                                 'unloaded': 0,
                                 'balance': 0}


class KitAvailabilityModel(QueryWithParamsModel):
    
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    item_id,
    item_description,
    quantity
FROM company.item_availability_detail
WHERE company_id = pa_current_company()
    AND item_type = 'K' 
    AND event_id = %(event)s
ORDER BY item_description;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, float, str, date, datetime, None = no filter
        self.columns = (("item", _tr('Models', 'Kit ID'), True, 'int'),
                        ("description", _tr('Models', 'Kit description'), True, 'str'),
                        ("quantity", _tr('Models', 'Quantity'), True, 'int'))
        

class MenuAvailabilityModel(QueryWithParamsModel):
    
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    item_id,
    item_description,
    quantity
FROM item_availability_detail
WHERE company_id = pa_current_company()
    AND item_type = 'M' 
    AND event_id = %(event)s
ORDER BY item_description;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, float, str, date, datetime, None = no filter
        self.columns = (("item", _tr('Models', 'Menu ID'), True, 'int'),
                        ("description", _tr('Models', 'Menu description'), True, 'str'),
                        ("quantity", _tr('Models', 'Quantity'), True, 'int'))


class StockUnloadModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    s.event_id,
    s.event_date,
    s.day_part,
    s.item_id,
    i.description,
    s.unloaded
FROM stock_unload s
JOIN item i ON s.item_id = i.item_id;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("s.event_id", _tr('Models', 'Event'), False, 'int'),
                        ("s.event_date", _tr('Models', 'Event date'), False, 'date'),
                        ("s.day_part", _tr('Models', 'L/D'), True, 'str'),
                        ("s.item_id", _tr('Models', 'Item'), False, 'int'),
                        ("i.description", _tr('Models', 'Item description'), True, 'str'),
                        ("s.unloaded", _tr('Models', 'Unloaded'), True, 'decimal2'))
        self.isCompanyTable = True
        self.companyField = 's.company_id'
        self.setRepr('Stock unload read-nly model')


class IncomeSummaryModel(QueryWithParamsModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
        SELECT 
            event,
            event_description,
            order_date,
            num_orders_lunch,
            num_orders_dinner,
            num_orders_lunch + num_orders_dinner AS num_orders,
            num_covers_lunch,
            num_covers_dinner,
            num_covers_lunch + num_covers_dinner AS num_covers,
            tot_take_away_lunch,
            tot_take_away_dinner,
            tot_take_away_lunch + tot_take_away_dinner AS tot_take_away,
            tot_table_lunch,
            tot_table_dinner,
            tot_table_lunch + tot_table_dinner AS tot_table,
            tot_cash_lunch,
            tot_cash_dinner,
            tot_cash_lunch + tot_cash_dinner AS tot_cash,
            tot_electronic_lunch,
            tot_electronic_dinner,
            tot_electronic_lunch + tot_electronic_dinner AS tot_electronic,
            amount_lunch,
            amount_dinner,
            amount_lunch + amount_dinner AS amount,
            discount_lunch,
            discount_dinner,
            discount_lunch + discount_dinner AS discount,
            amount_lunch - discount_lunch AS total_lunch,
            amount_dinner - discount_dinner AS total_dinner,
            amount_lunch + amount_dinner - discount_lunch - discount_dinner AS total
        FROM income_summary
        WHERE event = %(event)s;
        """
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, float, str, date, datetime, None = no filter
        self.columns = (("event", _tr('Models', 'Event'), True, 'int'),
                        ("event_description", _tr('Models', 'Event description'), True, 'str'),
                        ("order_date", _tr('Models', 'Date'), True, 'date'),
                        ("num_orders_lunch", _tr('Models', 'Orders L'), True, 'int'),
                        ("num_orders_dinner", _tr('Models', 'Orders D'), True, 'int'),
                        ("num_orders", _tr('Models', 'Orders'), True, 'int'),
                        ("num_covers_lunch", _tr('Models', 'Covers L'), True, 'int'),
                        ("num_covers_dinner", _tr('Models', 'Covers D'), True, 'int'),
                        ("num_covers", _tr('Models', 'Covers'), True, 'int'),
                        ("tot_take_away_lunch", _tr('Models', 'Take away L'), True, 'int'),
                        ("tot_take_away_dinner", _tr('Models', 'Take away D'), True, 'int'),
                        ("tot_take_away", _tr('Models', 'Take away'), True, 'int'),
                        ("tot_table_lunch", _tr('Models', 'Table L'), True, 'int'),
                        ("tot_table_dinner", _tr('Models', 'Table D'), True, 'int'),
                        ("tot_table", _tr('Models', 'Table'), True, 'int'),
                        ("tot_cash_lunch", _tr('Models', 'Total cash L'), True, 'decimal2'),
                        ("tot_cash_dinner", _tr('Models', 'Total cash D'), True, 'decimal2'),
                        ("tot_cash", _tr('Models', 'Total cash'), True, 'decimal2'),
                        ("tot_electronic_lunch", _tr('Models', 'Total electronic L'), True, 'decimal2'),
                        ("tot_electronic_dinner", _tr('Models', 'Total electronic D'), True, 'decimal2'),
                        ("tot_electronic", _tr('Models', 'Total electronic'), True, 'decimal2'),
                        ("amount_lunch", _tr('Models', 'Total amount L'), True, 'decimal2'),
                        ("amount_dinner", _tr('Models', 'Total amount D'), True, 'decimal2'),
                        ("amount", _tr('Models', 'Total amount'), True, 'decimal2'),
                        ("discount_lunch", _tr('Models', 'Discount L'), True, 'decimal2'),
                        ("discount_dinner", _tr('Models', 'Discount D'), True, 'decimal2'),
                        ("discount", _tr('Models', 'Discount'), True, 'decimal2'),
                        ("total_lunch", _tr('Models', 'Total L'), True, 'decimal2'),
                        ("total_dinner", _tr('Models', 'Total D'), True, 'decimal2'),
                        ("total", _tr('Models', 'Total'), True, 'decimal2'))
        
    def rowCount(self, index=QModelIndex()):
        # add 1 row for totals
        return QueryWithParamsModel.rowCount(self) + 1

    def data(self, index, role=Qt.DisplayRole):
        if index.row() == QueryWithParamsModel.rowCount(self): # last row
            if role == Qt.FontRole:
                font = QFont()
                font.setBold(True)
                return font
            if role == Qt.TextAlignmentRole:
                return Qt.AlignRight | Qt.AlignVCenter
            if role == Qt.DisplayRole:
                if index.column() == 1:
                    return _tr('Models', "TOTAL")
                elif 3 <= index.column() <= len(self.columns):
                    s = sum([self.dataSet[i, index.column()] for i in range(index.row())])
                    return s
        else:
            return QueryWithParamsModel.data(self, index, role)


class OrderHeaderIndexModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
SELECT 
    order_header_id,
    event_id,
    date_time,
    order_number,
    order_date,
    order_time,
    stat_order_date,
    stat_order_day_part,
    cash_desk,
    delivery,
    is_electronic_payment,
    table_num,
    customer_name,
    covers,
    total_amount,
    discount,
    cash,
    change,
    status,
    fullfillment_date,
    created_by,
    created_at,
    updated_by,
    updated_at
FROM company.order_header;"""
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("order_header_id", _tr('Models', 'ID'), True, 'int'),
                        ("event_id", _tr('Models', 'Event'), True, 'int'),
                        ("date_time", _tr('Models', 'Order date/time'), True, 'date'),
                        ("order_number", _tr('Models', 'Order number'), True, 'int'),
                        ("order_date", _tr('Models', 'Order date'), True, 'date'),
                        ("order_time", _tr('Models', 'Order time'), True, 'time'),
                        ("stat_order_date", _tr('Models', 'Stat order date'), True, 'date'),
                        ("stat_order_day_part", _tr('Models', 'Stat order day part'), True, 'str'),
                        ("cash_desk", _tr('Models', 'Cash desk'), True, 'str'),
                        ("delivery", _tr('Models', 'Delivery'), True, 'str'),
                        ("is_electronic_payment", _tr('Models', 'EP'), True, 'bool'),
                        ("table_num", _tr('Models', 'Table'), True, 'str'),
                        ("customer_name", _tr('Models', 'Customer name'), True, 'str'),
                        ("covers", _tr('Models', 'Covers'), True, 'int'),
                        ("total_amount", _tr('Models', 'Total amount'), True, 'decimal2'),
                        ("discount", _tr('Models', 'Discount'), True, 'decimal2'),
                        ("cash", _tr('Models', 'Cash'), True, 'decimal2'),
                        ("change", _tr('Models', 'Change'), True, 'decimal2'),
                        ("status", _tr('Models', 'Status'), True, 'str'),
                        ("fullfillment_date", _tr('Models', 'Fullfillment date'), True, 'date'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # class representation
        self.setRepr('Order header index query model')      
        # primary key fields, tuple or list
        self.primaryKey = ("order_header_id",)
        self.automaticPKey = True
        # limit number of rows fetched
        self.addLimit(10_000)
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("order_header_id")
        # reference fields dictionary
        self.reference = {'event_id': event_cdl}



class OrderHeaderModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.order_header"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("order_header_id", _tr('Models', 'ID'), True, 'int'),
                        ("event_id", _tr('Models', 'Event'), True, 'int'),
                        ("date_time", _tr('Models', 'Order date/time'), False, 'date'),
                        ("order_number", _tr('Models', 'Order number'), False, 'int'),
                        ("order_date", _tr('Models', 'Order date'), False, 'date'),
                        ("order_time", _tr('Models', 'Order time'), False, 'time'),
                        ("stat_order_date", _tr('Models', 'Stat order date'), False, 'date'),
                        ("stat_order_day_part", _tr('Models', 'Stat order day part'), False, 'str'),
                        ("cash_desk", _tr('Models', 'Cash desk'), False, 'str'),
                        ("delivery", _tr('Models', 'Delivery'), False, 'str'),
                        ("is_electronic_payment", _tr('Models', 'EP'), False, 'bool'),
                        ("table_num", _tr('Models', 'Table'), False, 'str'),
                        ("customer_name", _tr('Models', 'Customer name'), False, 'str'),
                        ("covers", _tr('Models', 'Covers'), False, 'int'),
                        ("total_amount", _tr('Models', 'Total amount'), False, 'decimal2'),
                        ("discount", _tr('Models', 'Discount'), False, 'decimal2'),
                        ("cash", _tr('Models', 'Cash'), False, 'decimal2'),
                        ("change", _tr('Models', 'Change'), False, 'decimal2'),
                        ("status", _tr('Models', 'Status'), False, 'str'),
                        ("fullfillment_date", _tr('Models', 'Fullfillment date'), False, 'date'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("order_header_id",)
        self.automaticPKey = True
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("order_header_id")
        # reference fields dictionary
        #self.reference = {'event': event_cdl}


class OrderHeaderDepartmentModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.order_header_department"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("order_header_department_id", _tr('Models', 'ID'), False, 'int'),
                        ("order_header_id", _tr('Models', 'ID header'), False, 'int'),
                        ("department_id", _tr('Models', 'Department'), False, 'int'),
                        ("note", _tr('Models', 'Notes'), False, 'str'),
                        ("other_departments", _tr('Models', 'Other departments'), False, 'str'),
                        ("fullfillment_date", _tr('Models', 'Fullfillment date'), False, 'date'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("order_header_department_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'order_header_id': 'order_header_id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("order_header_department_id")


class OrderLineModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.order_line"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("order_line_id", _tr('Models', 'ID'), False, 'int'),
                        ("order_header_id", _tr('Models', 'ID header'), False, 'int'),
                        ("item_id", _tr('Models', 'Item'), False, 'int'),
                        ("variants", _tr('Models', 'Variants'), False, 'str'),
                        ("quantity", _tr('Models', 'Quantity'), False, 'decimal2'),
                        ("price", _tr('Models', 'Price'), False, 'decimal2'),
                        ("amount", _tr('Models', 'Amount'), False, 'decimal2'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("order_line_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'order_header_id': 'order_header_id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("order_line_id")


class OrderLineDepartmentModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "company.order_line_department"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("order_line_department_id", _tr('Models', 'ID'), False, 'int'),
                        ("order_header_id", _tr('Models', 'ID header'), False, 'int'),
                        ("event_id", _tr('Models', 'Event'), False, 'int'),
                        ("event_date", _tr('Models', 'Event date'), False, 'date'),
                        ("day_part", _tr('Models', 'Day part'), False, 'str'),
                        ("department_id", _tr('Models', 'Department'), False, 'int'),
                        ("item_id", _tr('Models', 'Item'), False, 'int'),
                        ("variants", _tr('Models', 'Variants'), False, 'str'),
                        ("quantity", _tr('Models', 'Quantity'), False, 'decimal2'),
                        ("created_by", _tr('Models', 'User Ins'), True, 'str'),
                        ("created_at", _tr('Models', 'Date Ins'), True, 'date'),
                        ("updated_by", _tr('Models', 'User Update'), True, 'str'),
                        ("updated_at", _tr('Models', 'Date Update'), True, 'date'))
        # True if is a company table
        self.isCompanyTable = True
        # primary key fields, tuple or list
        self.primaryKey = ("order_line_department_id",)
        self.automaticPKey = True
        # master/detail relation {table field: reference field}
        self.foreignKey = {'order_header_id': 'order_header_id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("department_id")


class WebOrderHeaderModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
        SELECT 
            web_order_header_id, 
            date_time, 
            delivery, 
            table_num, 
            customer_name,
            covers,
            total_amount,
            processed
        FROM company.web_order_header;
        """
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, float, str, date, datetime, None = no filter
        self.columns = (("web_order_header_id", _tr('Models', 'ID'), True, 'int'),
                        ("date_time", _tr('Models', 'Date time'), True, 'datetime'),
                        ("delivery", _tr('Models', 'Delivery'), True, 'str'),
                        ("table_num", _tr('Models', 'Table'), True, 'str'),
                        ("customer_name", _tr('Models', 'Customer name'), True, 'str'),
                        ("covers", _tr('Models', 'Covers'), True, 'int'),
                        ("total_amount", _tr('Models', 'Total amount'), True, 'decimal2'),
                        ("processed", _tr('Models', 'Order processed'), True, 'bool'))
        # True if is a company table
        self.isCompanyTable = True
        self.addOrderBy('web_order_header_id ASC')
        # row id for master/detail filtering
        self.primaryKey = ("web_order_header_id",)


class WebOrderLineModel(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
        SELECT 
            web_order_line_id, 
            web_order_header_id, 
            item_id, 
            quantity, 
            price
        FROM company.web_order_line;
        """
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("web_order_line_id", _tr('Models', 'ID'), True, 'int'),
                        ("web_order_header_id", _tr('Models', 'Header ID'), True, 'int'),
                        ("item_id", _tr('Models', 'Item'), True, 'int'),
                        ("quantity", _tr('Models', 'Quantity'), True, 'decimal2'),
                        ("price", _tr('Models', 'Price'), True, 'decimal2'))
        # True if is a company table
        self.isCompanyTable = True
        # row id for master/detail filtering
        self.primaryKey = ("web_order_line_id",)
        # master/detail relation {table field: reference field}
        self.foreignKey = {'web_order_header_id': 'web_order_header_id'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("web_order_line_id")


class StatisticConfigurationModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "common.statistics_configuration"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("code", _tr('Models', 'Code'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("active", _tr('Models', 'Active'), False, 'bool'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("sql_query", _tr('Models', 'SQL Query'), False, 'str'),
                        ("sql_group_by", _tr('Models', 'SQL Group By'), False, 'str'),
                        ("report_code", _tr('Models', 'Report'), False, 'str'),
                        ("totals_row", _tr('Models', 'Totals row'), False, 'bool'),
                        ("total_label_column", _tr('Models', 'Label column'), False, 'int'),
                        ("user_ins", _tr('Models', 'User Ins'), True, 'str'),
                        ("date_ins", _tr('Models', 'Date Ins'), True, 'datetime'),
                        ("user_upd", _tr('Models', 'User Update'), True, 'str'),
                        ("date_upd", _tr('Models', 'Date Update'), True, 'datetime'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("code",)
        self.automaticPKey = False
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("sorting")


class StatisticConfigurationColumnModel(TableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.table = "common.statistics_configuration_column"
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("configuration_code", _tr('Models', 'Configuration code'), False, 'str'),
                        ("definition", _tr('Models', 'Definition'), False, 'str'),
                        ("description", _tr('Models', 'Description'), False, 'str'),
                        ("column_type", _tr('Models', 'Column type'), False, 'str'),
                        ("total_required", _tr('Models', 'Total'), False, 'bool'),
                        ("sorting", _tr('Models', 'Sorting'), False, 'int'),
                        ("user_ins", _tr('Models', 'User Ins'), True, 'str'),
                        ("date_ins", _tr('Models', 'Date Ins'), True, 'datetime'),
                        ("user_upd", _tr('Models', 'User Update'), True, 'str'),
                        ("date_upd", _tr('Models', 'Date Update'), True, 'datetime'))
        # True if is a company table
        self.isCompanyTable = False
        # primary key fields, tuple or list
        self.primaryKey = ("configuration_code", "definition")
        self.automaticPKey = False
        # master/detail relation {table field: reference field}
        self.foreignKey = {'configuration_code': 'code'}
        # sql order by clause, plain sql string without ORDER BY
        self.addOrderBy("sorting")


class StatisticSales1(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
        -- total sales by event/day/day part/department/item
        SELECT 
            sls.event AS event,
            ev.description AS event_description,
            sls.day AS day,
            it.department AS department,
            dp.description AS department_description,
            sls.item AS item,
            it.description AS item_description,
            it.has_stock_management AS stock_management,
            sls.quantity_lunch AS quantity_lunch,
            sls.quantity_dinner AS quantity_dinner,
            sls.quantity AS quantity_total,
            sls.amount_lunch AS amount_lunch,
            sls.amount_dinner AS amount_dinner,
            sls.amount AS amount_total
        FROM (
                SELECT  
                    oh.event AS event,
                    oh.stat_order_date AS day,
                    od.item AS item,
                    sum(CASE WHEN oh.stat_order_day_part = 'L' THEN od.quantity ELSE 0 END) AS quantity_lunch,
                    sum(CASE WHEN oh.stat_order_day_part = 'D' THEN od.quantity ELSE 0 END) AS quantity_dinner,
                    sum(od.quantity) AS quantity,
                    sum(CASE WHEN oh.stat_order_day_part = 'L' THEN od.amount ELSE 0 END) AS amount_lunch,
                    sum(CASE WHEN oh.stat_order_day_part = 'D' THEN od.amount ELSE 0 END) AS amount_dinner,
                    sum(od.amount) AS amount
                FROM order_detail od
                JOIN order_header oh ON od.id_header = oh.id
                GROUP BY oh.event, oh.stat_order_date, od.item
            ) sls
        JOIN event ev ON sls.event = ev.id
        JOIN item it ON sls.item = it.id
        JOIN department dp ON it.department = dp.id;
        """
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("sls.event", _tr('Models', 'Event'), True, 'int'),
                        ("ev.description", _tr('Models', 'Event description'), True, 'str'),
                        ("sls.day", _tr('Models', 'Day'), True, 'date'),
                        ("it.department", _tr('Models', 'Department'), True, 'int'),
                        ("dp.description", _tr('Models', 'Department description'), True, 'str'),
                        ("sls.item", _tr('Models', 'Item'), True, 'int'),
                        ("it.description", _tr('Models', 'Item description'), True, 'str'),
                        ("it.has_stock_management", _tr('Models', 'SC'), True, 'bool'),
                        #("it.has_unload_control", _tr('Models', 'UC'), True, 'bool'),
                        ("sls.quantity_lunch", _tr('Models', 'Quantity lunch'), True, 'int'),
                        ("sls.quantity_dinner", _tr('Models', 'Quantity dinner'), True, 'int'),
                        ("sls.quantity", _tr('Models', 'Quantity total'), True, 'int'),
                        ("sls.amount_lunch", _tr('Models', 'Amount lunch'), True, 'decimal2'),
                        ("sls.amount_dinner", _tr('Models', 'Amount dinner'), True, 'decimal2'),
                        ("sls.amount", _tr('Models', 'Amount total'), True, 'decimal2'))
        # True if is a company table
        self.isCompanyTable = True
        self.hasTotalsRow = True

    def rowCount(self, index=QModelIndex()):
        # add 1 row for totals
        return QueryModel.rowCount(self) + 1

    def data(self, index, role=Qt.DisplayRole):
        if index.row() == QueryModel.rowCount(self):  # last row
            if role == Qt.FontRole:
                font = QFont()
                font.setBold(True)
                return font
            if role == Qt.TextAlignmentRole:
                return Qt.AlignRight | Qt.AlignVCenter
            if role == Qt.DisplayRole:
                if index.column() == 6:
                    return _tr('Models', "TOTAL")
                elif 9 <= index.column() <= 14:
                    s = sum([self.dataSet[i, index.column()] for i in range(index.row())])
                    return s
        else:
            return QueryModel.data(self, index, role)


class StatisticUnloaded1(QueryModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = """
        -- total unloads by event/department/item
        SELECT su.event AS event,
            ev.description AS event_description,
            dp.id AS department,
            dp.description AS department_description,
            su.item AS item,
            it.description AS item_description,
            it.has_stock_control AS stock_control,
            it.has_unload_control AS unload_control,
            su.unloaded AS unloaded
        FROM (
	        SELECT 
                event AS event,
                item AS item,
                sum(unloaded) AS unloaded
	        FROM stock_unload
	        GROUP BY event, item
            ) su
        JOIN event ev ON su.event = ev.id
        JOIN item it ON su.item = it.id
        JOIN department dp ON it.department = dp.id;
        """
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = (("su.event", _tr('Models', 'Event'), True, 'int'),
                        ("ev.description", _tr('Models', 'Event description'), True, 'str'),
                        ("dp.id", _tr('Models', 'Department'), True, 'date'),
                        ("dp.description", _tr('Models', 'Department description'), True, 'str'),
                        ("su.item", _tr('Models', 'Item'), True, 'int'),
                        ("it.description", _tr('Models', 'Item description'), True, 'str'),
                        ("it.has_stock_control", _tr('Models', 'SC'), True, 'bool'),
                        ("it.has_unload_control", _tr('Models', 'UC'), True, 'bool'),
                        ("su.unloaded", _tr('Models', 'Unloaded'), True, 'str'))
        # True if is a company table
        self.isCompanyTable = True
        self.hasTotalsRow = True

    def rowCount(self, index=QModelIndex()):
        # add 1 row for totals
        return QueryModel.rowCount(self) + 1

    def data(self, index, role=Qt.DisplayRole):
        if index.row() == QueryModel.rowCount(self):  # last row
            if role == Qt.FontRole:
                font = QFont()
                font.setBold(True)
                return font
            if role == Qt.TextAlignmentRole:
                return Qt.AlignRight | Qt.AlignVCenter
            if role == Qt.DisplayRole:
                if index.column() == 5:
                    return _tr('Models', "TOTAL")
                elif index.column() == 8:
                    s = sum([self.dataSet[i, index.column()] for i in range(index.row())])
                    return s
        else:
            return QueryModel.data(self, index, role)


class StatisticQueryModel(QueryModel):
    "A model that fit to a dynamic sql query"

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = None
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = None
        self.hasTotalsRow = False
        self.totalsLabelRow = 0

    def setStatistic(self, code):
        "Update query and parameter for provided statistics code"
        #test = statisticsConfiguration(code)
        cd, ds, qy, gb, tr, tl = statistics_configuration(code)
        self.selectQuery = qy
        self.groupByExpression = gb
        self.hasTotalsRow = tr
        self.totalsLabelRow = tl
        self.columns = statistics_configuration_columns(code)
        self.totalsColumns = []
        for f in statistics_configuration_totals_columns(code):
            for c in self.columns:
                if c[0] == f:
                    self.totalsColumns.append(self.columns.index(c))
        self.filterCondition.clear()
        self.whereConditions.clear()
        self.havingConditions.clear()
        self.orderByExpressions.clear()

    def rowCount(self, index=QModelIndex()):
        # add 1 row for totals
        return QueryModel.rowCount(self) + (1 if self.hasTotalsRow else 0)

    def data(self, index, role=Qt.DisplayRole):
        if index.row() == QueryModel.rowCount(self):  # last row
            if role == Qt.FontRole:
                font = QFont()
                font.setBold(True)
                return font
            if role == Qt.TextAlignmentRole:
                return Qt.AlignRight | Qt.AlignVCenter
            if role == Qt.DisplayRole:
                if index.column() == self.totalsLabelRow:  # total label
                    return _tr('Models', "TOTAL")
                elif index.column() in self.totalsColumns:  # total columns
                    s = sum([self.dataSet[i, index.column()] for i in range(index.row())])
                    return s
        else:
            return QueryModel.data(self, index, role)


class Statistic(QueryModel):
    "A model that fit to a dynamic sql query"

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.selectQuery = None
        # model columns: (field, description, readonly, type), tuple of tuples
        # available types: int, bool, decimal2, str, date, datetime, None = no filter
        self.columns = None
        self.hasTotalsRow = False
        self.totalsLabelRow = 0

    def setStatistic(self, code):
        "Update query and parameter for provided statistics code"
        #test = statisticsConfiguration(code)
        cd, ds, qy, tr, tl = statistics_configuration(code)
        self.selectQuery = qy
        self.hasTotalsRow = tr
        self.totalsLabelRow = tl
        self.columns = statistics_configuration_columns(code)
        self.totalsColumns = []
        for f in statistics_configuration_totals_columns(code):
            for c in self.columns:
                if c[0] == f:
                    self.totalsColumns.append(self.columns.index(c))
        self.filterCondition.clear()
        self.whereConditions.clear()
        self.havingConditions.clear()
        self.orderByExpressions.clear()

    def rowCount(self, index=QModelIndex()):
        # add 1 row for totals
        return QueryModel.rowCount(self) + (1 if self.hasTotalsRow else 0)

    def data(self, index, role=Qt.DisplayRole):
        if index.row() == QueryModel.rowCount(self):  # last row
            if role == Qt.FontRole:
                font = QFont()
                font.setBold(True)
                return font
            if role == Qt.TextAlignmentRole:
                return Qt.AlignRight | Qt.AlignVCenter
            if role == Qt.DisplayRole:
                if index.column() == self.totalsLabelRow:  # total label
                    return _tr('Models', "TOTAL")
                elif index.column() in self.totalsColumns:  # total columns
                    s = sum([self.dataSet[i, index.column()] for i in range(index.row())])
                    return s
        else:
            return QueryModel.data(self, index, role)
        
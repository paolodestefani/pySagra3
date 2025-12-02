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

"""Application Actions

This module contains actions definitions

"""

# PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtGui import QKeySequence

# application modules
from App import APPNAME
from App import actionDefinition
from App.System.Utility import _tr

# application slots
from App.System.User import changePassword
from App.System.Help import help
from App.System.Help import faq
from App.System.About import about
from App.System.About import systemInfo
from App.System.About import aboutQt
from App.System.Preferences import preferences
from App.System.Connection import connection
from App.System.Connection import connectionHistory
from App.System.Company import company
from App.System.Profile import profile
from App.System.User import user
from App.System.Menu import menu
from App.System.Toolbar import toolbar
#from App.System.Shortcut import shortcuts
from App.System.Report import report
from App.System.Scripting import scripting
from App.System.Customization import customization
from App.CashDesk import cashDesk
from App.Printer import printers
from App.Department import departments
from App.StandTable import tables
from App.Item import items
from App.PriceList import priceList
from App.Event import events
from App.UpdateWebOrderServer import updateWebOrderServer
from App.WebOrder import webOrders
from App.OrderArchive import orderArchive
from App.StockInventory import stockInventory
from App.OrderProgress import orderProgress
from App.Settings import settings
from App.Order import orderEntry
from App.Statistics import statisticsSales, statisticsConsumption, statisticsExport
from App.StockUnload import stockUnload
from App.IncomeSummary import incomeSummary
from App.Tool import eventBasedTool
from App.Tool import deleteTool
from App.Tool import copyTool


# 0 description
# 1 slot
# 2 checkable
# 3 icon name
# 4 standard shortcut
# 5 tooltip
# 6 status tip
# 7 what's this
# 8 menu role


def createActionDictionary(mw):
    "Create the action definition dictionary trough a function for translation requirement"

    # SYSTEM ACTIONS
    actionDefinition['sys_change_company'] = (
        _tr("Action", 'Change company'),
        mw.changeCompany,
        False,
        'system_changecompany',
        QKeySequence.Open,
        _tr("Action", 'Change company'),
        _tr("Action", 'Switch to another company'),
        _tr("Action", 'Switch to another company'),
        QAction.TextHeuristicRole)

    actionDefinition['sys_change_password'] = (
        _tr("Action", 'Change password'),
        changePassword,
        False,
        'system_password',
        QKeySequence(Qt.Modifier.CTRL | Qt.Key.Key_X),
        _tr("Action", 'Change password'),
        _tr("Action", 'Change password of the current user'),
        _tr("Action", 'Change password'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_preferences'] = (
        _tr("Action", 'Preferences'),
        preferences,
        False,
        'system_preferences',
        QKeySequence.Preferences,
        _tr("Action", 'Change Theme'),
        _tr("Action", 'Change the Qt Theme used'),
        _tr("Action", 'Change Theme'),
        QAction.PreferencesRole)
    
    actionDefinition['sys_connection'] = (
        _tr("Action", 'Current connections'),
        connection,
        False,
        'system_connections',
        None,
        _tr("Action", 'Current connections'),
        _tr("Action", 'Show/Edit curent connections'),
        _tr("Action", 'Current connections'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_connection_history'] = (
        _tr("Action", 'Connections history'),
        connectionHistory,
        False,
        'system_connectionshistory',
        None,
        _tr("Action", 'Connections history'),
        _tr("Action", 'Show connections history'),
        _tr("Action", 'Connections history'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_company'] = (
        _tr("Action", 'Manage companies'),
        company,
        False,
        'system_company',
        None,
        _tr("Action", 'Manage companies'),
        _tr("Action", 'Create/drop/modify companies'),
        _tr("Action", 'Manage companies'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_profile'] = (
        _tr("Action", 'Profiles'),
        profile,
        False,
        'system_profiles',
        None,
        _tr("Action", 'Profiles management'),
        _tr("Action", 'Profiles management'),
        _tr("Action", 'Profiles management'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_user'] = (
        _tr("Action", 'Users'),
        user,
        False,
        'system_users',
        None,
        _tr("Action", 'Users management'),
        _tr("Action", 'Users management'),
        _tr("Action", 'Users management'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_menu'] = (
        _tr("Action", 'Menus'),
        menu,
        False,
        'system_menus',
        None,
        _tr("Action", 'Menus management'),
        _tr("Action", 'Menus management'),
        _tr("Action", 'Menus management'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_toolbar'] = (
        _tr("Action", 'Toolbars'),
        toolbar,
        False,
        'system_toolbars',
        None,
        _tr("Action", 'Toolbars management'),
        _tr("Action", 'Toolbars management'),
        _tr("Action", 'Toolbars management'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_report'] = (
        _tr("Action", 'Reports'),
        report,
        False,
        'system_reports',
        None,
        _tr("Action", 'Create/Edit reports'),
        _tr("Action", 'Create/Edit reports'),
        _tr("Action", 'Create/Edit reports'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_scripting'] = (
        _tr("Action", 'Python scripting'),
        scripting,
        False,
        'system_scripting',
        None,
        _tr("Action", 'Create/Edit python scripts'),
        _tr("Action", 'Create/Edit python scripts'),
        _tr("Action", 'Create/Edit python scripts'),
        QAction.TextHeuristicRole)
    
    actionDefinition['sys_customization'] = (
        _tr("Action", 'Customizations'),
        customization,
        False,
        'system_customizations',
        None,
        _tr("Action", 'Import/Export customizations'),
        _tr("Action", 'Import/Export customizations'),
        _tr("Action", 'Import/Export customizations'),
        QAction.TextHeuristicRole)

    actionDefinition['sys_quit'] = (
        _tr("Action", 'Quit'),
        mw.close,
        False,
        'system_quit',
        QKeySequence.Quit,
        _tr("Action", 'Quit'),
        _tr("Action", 'Close all windows and quit the application'),
        _tr("Action", 'Quit'),
        QAction.QuitRole)


    # EDIT ACTIONS
    actionDefinition['edit_new'] = (
        _tr("Action", 'New'),
        mw.new,
        False,
        'edit_new',
        QKeySequence.New,
        _tr("Action", 'New record'),
        _tr("Action", 'Insert new record'),
        _tr("Action", 'New record'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_save'] = (
        _tr("Action", 'Save'),
        mw.save,
        False,
        'edit_save',
        QKeySequence.Save,
        _tr("Action", 'Save record'),
        _tr("Action", 'Save record'),
        _tr("Action", 'Save record'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_delete'] = (
        _tr("Action", 'Delete'),
        mw.delete,
        False,
        'edit_delete',
        QKeySequence.Delete,
        _tr("Action", 'Delete record'),
        _tr("Action", 'Delete record'),
        _tr("Action", 'Delete record'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_reload'] = (
        _tr("Action", 'Undo/Reload'),
        mw.reload,
        False,
        'edit_reload',
        QKeySequence.Refresh,
        _tr("Action", 'Undo last change/Reload data'),
        _tr("Action", 'Undo last change/Reload data'),
        _tr("Action", 'Undo last change/Reload data'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_first'] = (
        _tr("Action", 'First'),
        mw.toFirst,
        False,
        'edit_first',
        QKeySequence.MoveToStartOfDocument,
        _tr("Action", 'Go to first record'),
        _tr("Action", 'Go to first record'),
        _tr("Action", 'Go to first record'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_previous'] = (
        _tr("Action", 'Previous'),
        mw.toPrevious,
        False,
        'edit_previous',
        QKeySequence.Back,
        _tr("Action", 'Go to previous record'),
        _tr("Action", 'Go to previous record'),
        _tr("Action", 'Go to previous record'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_counter'] = (
        _tr("Action", 'Counter'),
        None,
        False,
        None,
        None,
        _tr("Action", 'Current view record counter'),
        _tr("Action", 'Current view record counter'),
        _tr("Action", 'Current view record counter'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_next'] = (
        _tr("Action", 'Next'),
        mw.toNext,
        False,
        'edit_next',
        QKeySequence.Forward,
        _tr("Action", 'Go to next record'),
        _tr("Action", 'Go to next record'),
        _tr("Action", 'Go to next record'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_last'] = (
        _tr("Action", 'Last'),
        mw.toLast,
        False,
        'edit_last',
        QKeySequence.MoveToEndOfDocument,
        _tr("Action", 'Go to last record'),
        _tr("Action", 'Go to last record'),
        _tr("Action", 'Go to last record'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_filter'] = (
        _tr("Action", 'Filters'),
        mw.setFilters,
        False,
        'edit_filter',
        QKeySequence.Find,
        _tr("Action", 'Edit filters'),
        _tr("Action", 'Edit filters'),
        _tr("Action", 'Edit filters'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_change_view'] = (
        _tr("Action", 'Chenge view'),
        mw.changeView,
        False,
        'view_change',
        None,
        _tr("Action", 'Change view'),
        _tr("Action", 'Change view'),
        _tr("Action", 'Change view'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_print'] = (
        _tr("Action", 'Print'),
        mw.print,
        False,
        'edit_print',
        QKeySequence.Print,
        _tr("Action", 'Generate a print report'),
        _tr("Action", 'Generate a print report'),
        _tr("Action", 'Generate a print report'),
        QAction.TextHeuristicRole)

    actionDefinition['edit_export'] = (
        _tr("Action", 'Export'),
        mw.export,
        False,
        'edit_export',
        None,
        _tr("Action", 'Export data'),
        _tr("Action", 'Export data to a csv file'),
        _tr("Action", 'Export data'),
        QAction.TextHeuristicRole)

    # HELP ACTIONS
    actionDefinition['help_index'] = (
        _tr("Action", 'Help'),
        help,
        False,
        'help_contents',
        QKeySequence.HelpContents,
        _tr("Action", 'Help'),
        _tr("Action", 'Help index'),
        _tr("Action", 'Help'),
        QAction.NoRole)

    actionDefinition['help_faq'] = (
        _tr("Action", 'FAQ'),
        faq,
        False,
        'help_faq',
        None,
        _tr("Action", 'FAQ'),
        _tr("Action", 'Frequently Asked Questions'),
        _tr("Action", 'FAQ'),
        QAction.NoRole)

     # ABOUT ACTIONS
    actionDefinition['about_program'] = (
        _tr("Action", 'About {}').format(APPNAME),
        about,
        False,
        APPNAME,
        None,
        _tr("Action", 'About...'),
        _tr("Action", 'Information about {}').format(APPNAME),
        _tr("Action", 'About...'),
        QAction.AboutRole)

    actionDefinition['about_qt'] = (
        _tr("Action", 'About Qt'),
        aboutQt,
        False,
        'help_aboutqt',
        None,
        _tr("Action", 'About Qt'),
        _tr("Action", 'About Qt'),
        _tr("Action", 'About Qt'),
        QAction.AboutQtRole)

    actionDefinition['about_system_info'] = (
        _tr("Action", 'System informations'),
        systemInfo,
        False,
        'help_systeminfo',
        QKeySequence('CTRL+F1'),
        _tr("Action", 'System information'),
        _tr("Action", 'System information'),
        _tr("Action", 'System information'),
        QAction.NoRole)

    # APPLICATION SPECIFIC ACTIONS

    # file actions
    actionDefinition['app_file_setting'] = (
        _tr("Action", 'Settings'),
        settings,
        False,
        'file_settings',
        None,
        _tr("Action", 'Settings'),
        _tr("Action", 'View/Modify application settings'),
        _tr("Action", 'Settings'),
        QAction.NoRole)

    actionDefinition['app_file_cash_desk'] = (
        _tr("Action", 'Cash desk'),
        cashDesk,
        False,
        'file_cash_desks',
        None,
        _tr("Action", 'Cash desk'),
        _tr("Action", 'Manage cash desk names and parameters'),
        _tr("Action", 'Cash desk'),
        QAction.TextHeuristicRole)
    
    actionDefinition['app_file_printer'] = (
        _tr("Action", 'Printers'),
        printers,
        False,
        'file_printers',
        None,
        _tr("Action", 'Printer classes'),
        _tr("Action", 'Manage printer classes'),
        _tr("Action", 'Printer classes'),
        QAction.TextHeuristicRole)

    actionDefinition['app_file_event'] = (
        _tr("Action", 'Events'),
        events,
        False,
        'file_events',
        None,
        _tr("Action", 'Events'),
        _tr("Action", 'Events'),
        _tr("Action", 'Events'),
        QAction.TextHeuristicRole)
    
    actionDefinition['app_file_update_wo_server'] = (
        _tr("Action", 'Update W.O.Server'),
        updateWebOrderServer,
        False,
        'file_events',
        None,
        _tr("Action", 'Update W.O.Server'),
        _tr("Action", 'Update W.O.Server'),
        _tr("Action", 'Update W.O.Server'),
        QAction.TextHeuristicRole)

    actionDefinition['app_file_department'] = (
        _tr("Action", 'Departments'),
        departments,
        False,
        'file_departments',
        None,
        _tr("Action", 'Departments'),
        _tr("Action", 'Departments'),
        _tr("Action", 'Departments'),
        QAction.TextHeuristicRole)

    actionDefinition['app_file_table'] = (
        _tr("Action", 'Tables'),
        tables,
        False,
        'file_tables',
        None,
        _tr("Action", 'Tables'),
        _tr("Action", 'Tables'),
        _tr("Action", 'Tables'),
        QAction.TextHeuristicRole)

    actionDefinition['app_file_item'] = (
        _tr("Action", 'Items'),
        items,
        False,
        'file_items',
        None,
        _tr("Action", 'Items'),
        _tr("Action", 'Items'),
        _tr("Action", 'Items'),
        QAction.TextHeuristicRole)

    actionDefinition['app_file_price_list'] = (
        _tr("Action", 'Price list'),
        priceList,
        False,
        'file_prices',
        None,
        _tr("Action", 'Price list'),
        _tr("Action", 'Price list'),
        _tr("Action", 'Price list'),
        QAction.TextHeuristicRole)

    actionDefinition['app_file_order'] = (
        _tr("Action", 'Orders'),
        orderArchive,
        False,
        'file_orders',
        None,
        _tr("Action", 'Orders'),
        _tr("Action", 'Orders'),
        _tr("Action", 'Orders'),
        QAction.TextHeuristicRole)

    actionDefinition['app_file_web_order'] = (
        _tr("Action", 'Web orders'),
        webOrders,
        False,
        'file_weborders',
        None,
        _tr("Action", 'Web orders'),
        _tr("Action", 'Web orders'),
        _tr("Action", 'Web orders'),
        QAction.TextHeuristicRole)

    # activities actions
    actionDefinition['app_activity_order_entry'] = (
        _tr("Action", 'Order entry'),
        orderEntry,
        False,
        'activities_orders',
        None,
        _tr("Action", 'Order entry'),
        _tr("Action", 'Order entry'),
        _tr("Action", 'Order entry'),
        QAction.TextHeuristicRole)

    actionDefinition['app_activity_stock_inventory'] = (
        _tr("Action", 'Stock Inventory'),
        stockInventory,
        False,
        'activities_stockinventory',
        None,
        _tr("Action", 'Stock Inventory'),
        _tr("Action", 'Stock Inventory'),
        _tr("Action", 'Stock Inventory'),
        QAction.TextHeuristicRole)

    actionDefinition['app_activity_order_progress'] = (
        _tr("Action", 'Order progress'),
        orderProgress,
        False,
        'activities_orderprogress',
        None,
        _tr("Action", 'Order progress'),
        _tr("Action", 'Order progress'),
        _tr("Action", 'Order progress'),
        QAction.TextHeuristicRole)

    actionDefinition['app_activity_stock_unload'] = (
        _tr("Action", 'Stock unload'),
        stockUnload,
        False,
        'activities_stockunload',
        None,
        _tr("Action", 'Stock unload'),
        _tr("Action", 'Stock unload'),
        _tr("Action", 'Stock unload'),
        QAction.TextHeuristicRole)

    actionDefinition['app_activity_income_summary'] = (
        _tr("Action", 'Income summary'),
        incomeSummary,
        False,
        'activities_incomesummary',
        None,
        _tr("Action", 'Income summary'),
        _tr("Action", 'Income summary'),
        _tr("Action", 'Income summary'),
        QAction.TextHeuristicRole)

    # statistics
    actionDefinition['app_statistics_sales'] = (
        _tr("Action", 'Statistics sales'),
        statisticsSales,
        False,
        'activities_statistics',
        None,
        _tr("Action", 'Statistics sales'),
        _tr("Action", 'Statistics sales'),
        _tr("Action", 'Statistics sales'),
        QAction.TextHeuristicRole)

    actionDefinition['app_statistics_consumption'] = (
        _tr("Action", 'Statistics consumption'),
        statisticsConsumption,
        False,
        'activities_statistics',
        None,
        _tr("Action", 'Statistics consumption'),
        _tr("Action", 'Statistics consumption'),
        _tr("Action", 'Statistics consumption'),
        QAction.TextHeuristicRole)

    actionDefinition['app_statistics_export'] = (
        _tr("Action", 'Statistics export'),
        statisticsExport,
        False,
        'activities_statistics',
        None,
        _tr("Action", 'Statistics export'),
        _tr("Action", 'Statistics export'),
        _tr("Action", 'Statistics export'),
        QAction.TextHeuristicRole)

    # tools actions
    actionDefinition['app_tool_event_based'] = (
        _tr("Action", 'Application event based tool'),
        eventBasedTool,
        False,
        'tools_tool',
        None,
        _tr("Action", 'Application event based utilities'),
        _tr("Action", 'Application event based utilities'),
        _tr("Action", 'Application event based utilities'),
        QAction.TextHeuristicRole)

    actionDefinition['app_tool_delete'] = (
        _tr("Action", 'Delete tool'),
        deleteTool,
        False,
        'tools_tool',
        None,
        _tr("Action", 'Delete company data'),
        _tr("Action", 'Delete company data'),
        _tr("Action", 'Delete company data'),
        QAction.TextHeuristicRole)

    actionDefinition['app_tool_copy'] = (
        _tr("Action", 'Copy tool'),
        copyTool,
        False,
        'tools_tool',
        None,
        _tr("Action", 'Copy data from another company'),
        _tr("Action", 'Copy data from another company'),
        _tr("Action", 'Copy data from another company'),
        QAction.TextHeuristicRole)


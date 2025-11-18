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

"""Stock inventory

This module provides stock inventory management form and relate classes


"""

# standard library
import logging

# PySide6
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout

# application modules
from App import session
from App import currentAction
from App.Widget.Delegate import RelationDelegate
from App.Widget.Delegate import QuantityDelegate
from App.Widget.Delegate import NewStockDelegate
from App.Widget.Delegate import StockCheckDelegate
from App.Widget.Form import FormViewManager
from App.Widget.Dialog import EventFilterDialog
from App.Database.CodeDescriptionList import item_with_stock_control_cdl
from App.Database.Models import StockInventoryModel
from App.Database.Models import KitAvailabilityModel
from App.Database.Models import MenuAvailabilityModel
from App.Ui.StockInventoryWidget import Ui_StockInventoryWidget



ID, EVENT, ITEM, LOADED, UNLOADED, BALANCE, NEW_STOCK = range(7)


def stockInventory(auth):
    "Manage stock inventory"
    logging.info('Starting stock inventory Form')
    mw = session['mainwin']
    title = currentAction['app_activity_stock_inventory'].text()
    auth = currentAction['app_activity_stock_inventory'].data()
    sw = StocksInventoryForm(mw, title, auth)
    mw.addTab(title, sw)
    logging.info('Stock inventory Form added to main window')

#class StockInventoryFilterDialog(QDialog, Ui_StockInventoryFilterDialog):

    #def __init__(self, parent):
        #super().__init__(parent)
        #self.setupUi(self)
        #self.parent = parent
        ## fill event combobox
        #for i, d in event_list():
            #self.comboBoxEvent.addItem(d, i)
        #self.comboBoxEvent.setCurrentText(session['event_description'])

    #def accept(self):
        #self.parent.selectedEvent = self.comboBoxEvent.currentData()
        #self.parent.updateEventData()
        #super().accept()


class StocksInventoryForm(FormViewManager):

    def __init__(self, parent: QWidget, title: str, auth: str) -> None:
        super().__init__(parent, auth)
        model = StockInventoryModel(self)
        self.setModel(model)
        self.tabName = title
        self.helpLink = None
        # available edit status
        # NEW, SAVE, DELETE, RELOAD, FIRST, PREVIOUS, NEXT, LAST
        # FILTER, CHANGE, REPORT, EXPORT
        self.availableStatus = (True, True, True, True, False, False, False, False,
                                False, False, False, False)
        self.ui = Ui_StockInventoryWidget()
        self.ui.setupUi(self)
        self.setView(self.ui.tableViewItem)  # required for formviewmanager
        # normal item
        #self.view = self.ui..tableViewItem
        #self.ui.tableViewItem.setModel(model)
        self.ui.tableViewItem.setLayoutName('stockInventory')
        # self.ui.tableViewItem.horizontalHeader().setSectionsMovable(True)
        self.ui.tableViewItem.setItemDelegateForColumn(ITEM, RelationDelegate(self, item_with_stock_control_cdl))
        self.ui.tableViewItem.setItemDelegateForColumn(LOADED, QuantityDelegate(self))
        self.ui.tableViewItem.setItemDelegateForColumn(UNLOADED, QuantityDelegate(self))
        self.ui.tableViewItem.setItemDelegateForColumn(BALANCE, StockCheckDelegate(self))
        self.ui.tableViewItem.setItemDelegateForColumn(NEW_STOCK, NewStockDelegate(self))
        # stay on NEW_STOCK column
        #self.ui.tableViewItem.selectionModel().currentChanged.connect(self.columnChanged)
        # kit availability
        self.kitModel = KitAvailabilityModel(self)
        #self.kitModel.setParameter('event', self.ui.comboBoxevent.currentData())
        #self.kitModel.select()
        self.ui.tableViewKit.setModel(self.kitModel)
        self.ui.tableViewKit.setLayoutName('stockInventoryKit')
        self.ui.tableViewKit.setItemDelegateForColumn(2, QuantityDelegate(self))
        # menu availability
        self.menuModel = MenuAvailabilityModel(self)
        self.ui.tableViewMenu.setModel(self.menuModel)
        self.ui.tableViewMenu.setLayoutName('stockInventoryMenu')
        self.ui.tableViewMenu.setItemDelegateForColumn(2, QuantityDelegate(self))
        # select initial event, ask if current event is None
        if session['event']:
            self.selectedEvent = session['event']
            self.updateFilterConditions(session['event'])
        else:
            self.setFilters()
        # splitter
        self.ui.splitter.setStretchFactor(0, 2)

    def save(self):
        super().save()
        self.updateFilterConditions(self.selectedEvent)

    def reload(self):
        super().reload()
        self.updateFilterConditions(self.selectedEvent)

    def new(self):
        # set event on new record
        super().new()
        model = self.ui.tableViewItem.model()
        newRow = model.rowCount() - 1
        newIndex = model.index(newRow, EVENT)
        model.setData(newIndex, self.selectedEvent)
        # edit item cell
        newIndex = model.index(newRow, ITEM)
        self.ui.tableViewItem.edit(newIndex)

    #def columnChanged(self, current, previous):
        #"On column change move to next line same column if NEW_STOCK"
        ##print(previous.column(), current.column(), previous.row(), current.row())
        #if previous.column() == NEW_STOCK:
            ##print(previous.column(), current.column(), previous.row(), current.row())
            #index = self.ui.tableViewItem.model().index(previous.row() + 1, NEW_STOCK)
            #self.ui.tableViewItem.setCurrentIndex(index)
            #self.ui.tableViewItem.edit(index)

    def updateFilterConditions(self, event, eventDate=None, dayPart=None):
        "Update model of item, kit and menu on new event id"
        self.selectedEvent = event
        # stock model
        self.ui.tableViewItem.model().whereConditions = [('event = %s', event)]
        self.ui.tableViewItem.model().select()
        # kit model
        self.kitModel.setParameter('event', event)
        self.kitModel.select()
        # menu model
        self.menuModel.setParameter('event', event)
        self.menuModel.select()

    def setFilters(self):
        "Filters event and items"
        # create filter dialog if not exists
        if not hasattr(self, 'sortFilterDialog'):
            self.sortFilterDialog = EventFilterDialog(self, session['event'])
        self.sortFilterDialog.show()

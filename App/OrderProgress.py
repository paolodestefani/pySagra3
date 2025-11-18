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

"""Order progress

This module provides a dialog for manage order progress


"""

# standard library
import logging

# PySide6
from PySide6.QtCore import Qt
from PySide6.QtCore import QObject
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QTableWidgetItem

# application modules
from App import session
from App import currentAction
from App.Database.Exceptions import PyAppDBError
from App.Database.Order import get_order_header_department_details
from App.Database.Order import update_order_header_department_status
from App.Database.Setting import SettingClass
from App.Ui.OrderProgressDialog import Ui_OrderProgressDialog
from App.System.Utility import _tr



ID, NUM, DATE, TIME, DELIVERY, TABLE, CUSTOMER, DEPARTMENT, FULLFILLMENT = range(9)



def orderProgress(auth):
    "Order progress"
    logging.info('Starting order progress dialog')
    mw = session['mainwin']
    title = currentAction['app_activity_order_progress'].text()
    auth = currentAction['app_activity_order_progress'].data()
    icon = currentAction['app_activity_order_progress'].icon()
    setting = SettingClass()
    if not setting['manage_order_progress']:
        QMessageBox.warning(mw,
                            _tr('MessageDialog', 'Warning'),
                            _tr('OrderProgress', 'Order progress management is not active!\n'
                                'You need to activate it in File/Settings'))
        return
    dlg = OrderProgressDialog(mw, title, icon, auth)
    dlg.exec()
    logging.info('Order progress dialog shown')


class OrderProgressDialog(QDialog):

    def __init__(self, parent, title, icon, auth):
        super().__init__(parent)
        self.ui = Ui_OrderProgressDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        # self.labelIcon.setPixmap(icon.pixmap(100))
        # order list tablewidget
        header = [_tr('OrderProgress', "ID"),
                  _tr('OrderProgress', "Num"),
                  _tr('OrderProgress', "Date"),
                  _tr('OrderProgress', "Time"),
                  _tr('OrderProgress', "Delivery"),
                  _tr('OrderProgress', "Table"),
                  _tr('OrderProgress', "Customer"),
                  _tr('OrderProgress', "Department"),
                  _tr('OrderProgress', "Fullfillment date")]
        self.ui.tableWidgetBarcodeScans.setColumnCount(len(header))
        self.ui.tableWidgetBarcodeScans.setSortingEnabled(False)
        self.ui.tableWidgetBarcodeScans.setHorizontalHeaderLabels(header)
        self.ui.tableWidgetBarcodeScans.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableWidgetBarcodeScans.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
        self.ui.tableWidgetBarcodeScans.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidgetBarcodeScans.setAlternatingRowColors(True)
        self.ui.tableWidgetBarcodeScans.setWordWrap(False)
        # self.ui.tableWidgetBarcodeScans.hideColumn(ID)
        # signal/slot connections
        self.ui.lineEditBarcode.editingFinished.connect(self.scan)
        self.ui.pushButtonMarkUnprocessed.clicked.connect(self.markUnprocessed)
        self.ui.pushButtonClose.clicked.connect(self.close)

    def scan(self):
        "Update order header status, insert a record in scns history"
        value = self.ui.lineEditBarcode.text()
        if not value:  # could be an empty string
            return
        # convert to int
        try:
            orderId = int(value)
        except ValueError:
            QMessageBox.critical(self,
                                 _tr('MessageDialog', 'Critical'),
                                 _tr('OrderProgress', 'Unable to convert barcode string to number'))
            self.ui.lineEditBarcode.clear()
            self.ui.lineEditBarcode.setFocus()
            return
        # get order details of given order id
        result = get_order_header_department_details(orderId)
        if not result:  # no order dep fuond for that id
            QMessageBox.warning(self,
                                _tr('MessageDialog', 'Warning'),
                                _tr('OrderProgress', 'Order id not found'))
            self.ui.lineEditBarcode.clear()
            self.ui.lineEditBarcode.setFocus()
            return

        (ohid, oid, onum, odate, otime, odelivery, otable, ocustomer,
         odep, odepdesc, ofullfillmentdate) = result

        if ofullfillmentdate:  # order already processed
            if QMessageBox.question(self,
                                    _tr('MessageDialog', 'Question'),
                                    _tr('OrderProgress', 'Order already processed, process again ?'),
                                    QMessageBox.Yes | QMessageBox.No,  # butons
                                    QMessageBox.No  # default botton
                                    ) == QMessageBox.No:
                self.ui.lineEditBarcode.clear()
                self.ui.lineEditBarcode.setFocus()
                return

        self.ui.lineEditBarcode.clear()
        self.ui.lineEditBarcode.setFocus()
        # update order header department status, mark as processed order header department
        try:
            update_order_header_department_status(orderId, True)
        except PyAppDBError as er:
            mbox = QMessageBox(self)
            mbox.setIcon(QMessageBox.Critical)
            mbox.setWindowTitle(_tr("OrderProgress", "Error on update order status"))
            mbox.setText(_tr("OrderProgress", "Database error {}").format(er.code))
            mbox.setDetailedText(er.message)
            mbox.exec_()
        # insert new row in scans history
        row = self.ui.tableWidgetBarcodeScans.rowCount()
        self.ui.tableWidgetBarcodeScans.insertRow(row)
        cell = QTableWidgetItem(str(ohid))
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, ID, cell)
        cell = QTableWidgetItem(str(onum))
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, NUM, cell)
        cell = QTableWidgetItem(odate.toString())
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, DATE, cell)
        cell = QTableWidgetItem(otime.toString())
        cell.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, TIME, cell)
        cell = QTableWidgetItem(odelivery)
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        cell.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.ui.tableWidgetBarcodeScans.setItem(row, DELIVERY, cell)
        cell = QTableWidgetItem(otable)
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, TABLE, cell)
        cell = QTableWidgetItem(ocustomer)
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, CUSTOMER, cell)
        cell = QTableWidgetItem(odepdesc)
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, DEPARTMENT, cell)
        # datetime shows is current because apdated anyway even if already processed
        cell = QTableWidgetItem(QDateTime.currentDateTime().toString(Qt.DefaultLocaleShortDate))
        cell.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.ui.tableWidgetBarcodeScans.setItem(row, FULLFILLMENT, cell)
        self.ui.tableWidgetBarcodeScans.scrollToBottom()

    def markUnprocessed(self):
        "Mark as unprocessed the current selected line"
        row = self.ui.tableWidgetBarcodeScans.currentRow()
        orderId = int(self.ui.tableWidgetBarcodeScans.item(row, ID).data(Qt.EditRole))
        if orderId < 0:  # no item selected
            return
        if QMessageBox.question(self,
                                _tr('MessageDialog', 'Question'),
                                _tr('OrderProgress', 'Unmark current selected order ?'),
                                QMessageBox.Yes | QMessageBox.No,  # butons
                                QMessageBox.No  # default botton
                                ) == QMessageBox.No:
            self.ui.lineEditBarcode.setFocus()
            return
        # update order header department status, unmark order header department
        try:
            update_order_header_department_status(orderId, False)
        except PyAppDBError as er:
            mbox = QMessageBox(self)
            mbox.setIcon(QMessageBox.Critical)
            mbox.setWindowTitle(_tr("OrderProgress", "Error on update order status"))
            mbox.setText(_tr("OrderProgress", "Database error {}").format(er.code))
            mbox.setDetailedText(er.message)
            mbox.exec_()
        # delete row from tablewidget
        self.ui.tableWidgetBarcodeScans.removeRow(row)
        self.ui.lineEditBarcode.setFocus()

    def closeEvent(self, event):
        "Close dialog, ask confirmation"
        if QMessageBox.question(self,
                                _tr('MessageDialog', 'Question'),
                                _tr('OrderProgress', 'Quit order progress management ?'),
                                QMessageBox.Yes | QMessageBox.No,  # butons
                                QMessageBox.No  # default botton
                                ) == QMessageBox.Yes:
            event.accept()
        else:
            self.ui.lineEditBarcode.setFocus()
            event.ignore()

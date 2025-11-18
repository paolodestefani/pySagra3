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

"""Statistics

This module provide a print statistic launcher


"""

# standard library
import logging
import csv
import decimal

# PySide6
from PySide6.QtCore import QObject
from PySide6.QtCore import QSettings
from PySide6.QtCore import QDir
from PySide6.QtCore import QByteArray
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QTime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QFileDialog

# application modules
from App.Database.Exceptions import PyAppDBError
from App.Database.CodeDescriptionList import event_cdl
from App.Database.Statistics import load_statistic_bi_data
from App.Ui.StatisticsExportDialog import Ui_StatisticsExportDialog
from App.Widget.Dialog import PrintDialog
from App.System.Utility import _tr


def statisticsSales(auth):
    "Print statistic reports"
    logging.info('Starting statistics sales dialog')
    mw = QObject().sender().parentWidget()
    dialog = PrintDialog(mw, 'STATISTICS_SALES')
    dialog.show()
    logging.info('Statistics sales dialog shown')


def statisticsConsumption(auth):
    "Print statistic reports"
    logging.info('Starting statistics consumption dialog')
    mw = QObject().sender().parentWidget()
    dialog = PrintDialog(mw, 'STATISTICS_CONSUMPTION')
    dialog.show()
    logging.info('Statistics consumption dialog shown')


def statisticsExport():
    "Statistics export"
    logging.info('Starting statistics export dialog')
    mw = QObject().sender().parentWidget()
    auth = QObject().sender().data()
    title = QObject().sender().text()
    icon = QObject().sender().icon()
    dlg = StatisticsExportDialog(mw, title, icon, auth)
    dlg.exec_()
    logging.info('Statistics  export dialog shown')


class StatisticsExportDialog(QDialog, Ui_StatisticsExportDialog):

    def __init__(self, parent, title, icon, auth):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(title)
        for i, d in event_cdl():
            self.comboBoxFromEvent.addItem(d, i)
            self.comboBoxToEvent.addItem(d, i)
        # restore settings
        st = QSettings(self)
        if st.value("StatisticsExport/Geometry"):
            self.restoreGeometry(st.value("StatisticsExport/Geometry"))
        self.lineEditHeadersFileName.setText(st.value("StatisticsExport/HeadersFileName", ""))
        self.lineEditDetailsFileName.setText(st.value("StatisticsExport/DetailsFileName", ""))
        self.checkBoxIncludeAll.setChecked(st.value("StatisticsExport/IncludeAll", 'false') == 'true')
        self.comboBoxFromEvent.setCurrentIndex(int(st.value("StatisticsExport/FromEvent", '1')))
        self.comboBoxToEvent.setCurrentIndex(int(st.value("StatisticsExport/ToEvent", '1')))
        # signal slot connections
        self.checkBoxIncludeAll.toggled.connect(self.includeAllEvents)
        self.pushButtonSelectHeaders.clicked.connect(self.selectHeadersClicked)
        self.pushButtonSelectDetails.clicked.connect(self.selectDetailsClicked)

    def includeAllEvents(self, checked):
        if checked:
            self.comboBoxFromEvent.setCurrentIndex(-1)
            self.groupBoxFromEvent.setDisabled(True)
            self.comboBoxToEvent.setCurrentIndex(-1)
            self.groupBoxToEvent.setDisabled(True)
        else:
            self.groupBoxFromEvent.setEnabled(True)
            self.groupBoxToEvent.setEnabled(True)

    def selectHeadersClicked(self):
        if self.lineEditHeadersFileName.text():
            path = self.lineEditHeadersFileName.text()
        else:
            path = QDir.currentPath()
        fname, t = QFileDialog.getSaveFileName(self,
                                               _tr("View", "Select file name and path"),
                                               path,
                                               _tr("View", "Comma separated values (*.csv);;All files (*.*)"))
        if not fname: # clicked cancel
            return
        self.lineEditHeadersFileName.setText(fname)
        # save export path
        st = QSettings()
        st.setValue("StatisticsExport/HeadersFileName", fname)

    def selectDetailsClicked(self):
        if self.lineEditDetailsFileName.text():
            path = self.lineEditDetailsFileName.text()
        else:
            path = QDir.currentPath()
        fname, t = QFileDialog.getSaveFileName(self,
                                               _tr("View", "Select file name and path"),
                                               path,
                                               _tr("View", "Comma separated values (*.csv);;All files (*.*)"))
        if not fname: # clicked cancel
            return
        self.lineEditDetailsFileName.setText(fname)
        # save export path
        st = QSettings()
        st.setValue("StatisticsExport/DetailsFileName", fname)

    def accept(self):
        "Proceed on export data"
        if self.checkBoxIncludeAll.isChecked():
            fromEvent = 1
            toEvent = 999999
        else:
            fromEvent = int(self.comboBoxFromEvent.currentData())
            toEvent = int(self.comboBoxToEvent.currentData())
        fnameh = self.lineEditHeadersFileName.text()
        fnamed = self.lineEditDetailsFileName.text()
        try:
            for view, fn in (('bi_order_header', fnameh), ('bi_order_detail', fnamed)):
                # write to csv file
                with open(fn, 'w', encoding="utf-8", newline='') as f:
                    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for r in load_statistic_bi_data(view, fromEvent, toEvent):
                        row = []
                        for c in r:
                            if isinstance(c, QByteArray):
                                data = 'BINARY DATA'
                            elif isinstance(c, QDate):
                                data = c.toString(Qt.DefaultLocaleShortDate)
                            elif isinstance(c, QDateTime):
                                data = c.toString(Qt.DefaultLocaleShortDate)
                            elif isinstance(c, QTime):
                                data = c.toString(Qt.DefaultLocaleShortDate)
                            elif isinstance(c, bool):
                                #data = "\u2611" if data else "\u2610" # tick
                                data = "I" if c else "O" # less problem with excel
                            elif isinstance(c, (float, decimal.Decimal)):
                                data = str(c).replace(".", ",")
                            elif c is None:
                                data = ''
                            else:
                                data = str(c)
                            row.append(data)
                        writer.writerow(row)
        except PyAppDBError as er:
            QMessageBox.critical(self,
                                 _tr('MessageDialog', 'Critical'),
                                 f"Database error: {er.code}\n{er.message}")
        else:
            QMessageBox.information(self,
                                    _tr('MessageDialog', 'Information'),
                                    _tr('Utility', 'Operation completed successfully'))
        # save settings
        st = QSettings()
        st.setValue("StatisticsExport/IncludeAll", self.checkBoxIncludeAll.isChecked())
        st.setValue("StatisticsExport/FromEvent", self.comboBoxFromEvent.currentIndex())
        st.setValue("StatisticsExport/ToEvent", self.comboBoxToEvent.currentIndex())
        super().accept()


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

"""Utilities

This module contains GUI utilities for system and application modules


"""

# standard library

# PyQt5
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QPushButton



#def saveState(window):
    #"Save state and geometry of main window"
    #st = QSettings()
    #st.setValue(f"{window.__class__.__name__}Geometry", window.saveGeometry())
    #st.setValue(f"{window.__class__.__name__}State", window.saveState(1))

#def restoreState(window):
    #"Restore state and geometry of main window, if available"
    #st = QSettings()
    #if st.value(f"{window.__class__.__name__}Geometry"):
        #window.restoreGeometry(st.value(f"{window.__class__.__name__}Geometry"))
    #else: # useful default
        #window.setGeometry(50, 50, 800, 600)
        ## center windows
        #window.setGeometry(QStyle.alignedRect(Qt.LeftToRight,
                                              #Qt.AlignCenter,
                                              #window.size(),
                                              #qApp.desktop().availableGeometry()))
    #if st.value("State"):
        #window.restoreState(st.value("State"), 1)

def restoreSettings(w):
    "Restore the w widget's settings"
    n = w.objectName()
    st = QSettings()
    w.restoreGeometry(st.value(n + "/Geometry"))
    for i in w.__dict__.values():
        if isinstance(i, QLineEdit):
            i.setText(st.value(n + "/" + i.objectName(), ""))
        if isinstance(i, QComboBox):
            i.setCurrentIndex(st.value(n + "/" + i.objectName(), 0))
        if isinstance(i, QCheckBox):
            i.setChecked(False if st.value(n + "/" + i.objectName(), 'false') == 'false' else True)
        if isinstance(i, QSpinBox):
            i.setValue(st.value(n + "/" + i.objectName(), 0))
        if isinstance(i, QDateEdit):
            i.setDate(st.value(n + "/" + i.objectName(), QDate.currentDate()))
        if isinstance(i, QStackedWidget):
            i.setCurrentIndex(st.value(n + "/" + i.objectName(), 0))
        # enabled
        if isinstance(i, (QLineEdit, QComboBox, QCheckBox, QSpinBox, QGroupBox,
                          QPushButton)):
            i.setEnabled(True if st.value(n + "/" + i.objectName() + "_Enabled", 'true') == 'true' else False)

def saveSettings(w):
    "Save the w widget's settings"
    n = w.objectName()
    st = QSettings()
    st.setValue(n + "/Geometry", w.saveGeometry())
    for i in w.__dict__.values():
        if isinstance(i, QLineEdit):
            st.setValue(n + "/" + i.objectName(), i.text())
        if isinstance(i, QComboBox):
            st.setValue(n + "/" + i.objectName(), i.currentIndex())
        if isinstance(i, QCheckBox):
            st.setValue(n + "/" + i.objectName(), i.isChecked())
        if isinstance(i, QSpinBox):
            st.setValue(n + "/" + i.objectName(), i.value())
        if isinstance(i, QDateEdit):
            st.setValue(n + "/" + i.objectName(), i.date())
        if isinstance(i, QStackedWidget):
            st.setValue(n + "/" + i.objectName(), i.currentIndex())
        # enabled
        if isinstance(i, (QLineEdit, QComboBox, QCheckBox, QSpinBox, QGroupBox,
                          QPushButton)):
            st.setValue(n + "/" + i.objectName() + "_Enabled", i.isEnabled())


#def createAction(parent, text, slot=None, shortcut=None, icon=None,
                 #tooltip=None, statustip=None, checkable=False, t=None, par=None):
    #"Create a new Action"
    #action = QAction(text, parent)
    #if icon is not None:
        #action.setIcon(QIcon(":/{0}".format(icon)))
    #if shortcut is not None:
        #action.setShortcut(shortcut)
    #if tooltip is not None:
        #action.setToolTip(tooltip)
    #if statustip is not None:
        #action.setStatusTip(statustip)
    #if slot is not None:
        #if par:
            #action.triggered.connect(partial(slot, parent, t, text, par))
        #else:
            #action.triggered.connect(slot)
    #if checkable:
        #action.setCheckable(True)
    #return action

#def addActions(target, actions):
    #for action in actions:
        #if action is None:
            #target.addSeparator()
        #elif isinstance(action, QMenu):
            #target.addMenu(action)
        #else:
            #target.addAction(action)

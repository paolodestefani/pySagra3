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

# standard library
import decimal

from cryptography.fernet import Fernet

# PySide6
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox

# application modules
from App import ENCKEY
from App import session
from App.Database.Scripting import get_script


# translate function

def _tr(context: str, text: str, disambig:str|None = None) -> str:
    return QCoreApplication.translate(context, text, disambig)

def fromCurrency(val: str) -> decimal.Decimal:
    "Returns a decimal value from input (locale aware) string"
    if val:  # value come from spinboxes and model data (QVariant)
        if isinstance(val, str):
            return decimal.Decimal(session['qlocale'].toFloat(val)[0])
        else:
            return decimal.Decimal(val)
    else:
        return decimal.Decimal(0)

def toCurrency(val: decimal.Decimal) -> str:
    "Returns a string rapresentation of currency (decimal) value"
    return session['qlocale'].toCurrencyString(float(val), ' ')  # = no currency symbol


# encoding decoding password

def string_encode(token: str) -> str:
    "Cryptography Fernet"
    return Fernet(ENCKEY).encrypt(token.encode('utf-8')).decode('utf-8')

def string_decode(token: str) -> str:
    "Cryptography Fernet"
    return Fernet(ENCKEY).decrypt(token.encode('utf-8')).decode('utf-8')


# language and country list

def langCountryFlags() -> list:
    "Returns a list of languages/countries with flag icon"
    # Must use a function because QIcon() can be created only after a QApplication()
    return [#(QIcon(), None, None),
            (QIcon(':/flags/flag_italy'), 'it_IT', "Italiano / Italia"),
            (QIcon(':/flags/flag_usa'), 'en_US', "English / United States"),
            (QIcon(':/flags/flag_uk'), 'en_UK', "English / United Kingdom"),
            (QIcon(':/flags/flag_france'), 'fr_FR', "Français / France"),
            (QIcon(':/flags/flag_germany'), 'de_DE', "Deutsch / Deutschland"),
            (QIcon(':/flags/flag_russia'), 'ru_RU', "русский / Россия"),
            (QIcon(':/flags/flag_china'), 'zh_CN', "中國 / 中國"),
            (QIcon(':/flags/flag_thailand'), 'th_TH', "ไทย / ประเทศไทย")]

def langCountry() -> list:
    "Returns a list of languages/countries"
    # neew 2 function for use with relationalDelegate
    return [('it_IT', "Italiano / Italia"),
            ('en_US', "English / United States"),
            ('en_UK', "English / United Kingdom"),
            ('fr_FR', "Français / France"),
            ('de_DE', "Deutsch / Deutschland"),
            ('ru_RU', "русский / Россия"),
            ('zh_CN', "中國 / 中國"),
            ('th_TH', "ไทย / ประเทศไทย")]


# scripting management
def scriptInit(instanceReference):
    "Returns a dictionary of string command for scripting purpose"
    script = get_script(instanceReference.__class__.__name__)
    # execute init script after if any
    globalsParameters = {'session': session,
                         'self': instanceReference}
    try:
        exec(script.get(('__init__', 'A'), ''), globalsParameters)
    except Exception as er:
        QMessageBox.critical(None,
                             'Script engine',
                             f'Error executing __init__ script: \n{er}')
    return script


def scriptMethod(method):
    "Execute before/after script if any"

    def wrapper(*args, **kwargs):
        globalsParameters = {'session': session,
                             'self': args[0]}  # first argument of a method is instance reference
        # execute script before
        try:
            exec(args[0].script.get((method.__name__, 'B'), ''), globalsParameters)
        except Exception as er:
            QMessageBox.critical(None,
                                 'Script engine',
                                 f'Error executing before script: \n{er}')
        # execute script instead
        if args[0].script.get((method.__name__, 'I')):
            try:
                exec(args[0].script.get((method.__name__, 'I'), ''), globalsParameters)
            except Exception as er:
                QMessageBox.critical(None,
                                     'Script engine',
                                     f'Error executing instead script: \n{er}')
        else:
            # execute method
            method(*args, **kwargs)

        # execute script after
        try:
            exec(args[0].script.get((method.__name__, 'A'), ''), globalsParameters)
        except Exception as er:
            QMessageBox.critical(None,
                                 'Script engine',
                                 f'Error executing after script: \n{er}')

    return wrapper


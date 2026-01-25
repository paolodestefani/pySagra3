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

"""Email

Manage email


"""

# standard library
#import os
#import time
import logging
from email.message import EmailMessage
import smtplib
import ssl

from cryptography.fernet import InvalidToken

# PySide6
#from PySide6.QtCore import QCoreApplication
#from PySide6.QtCore import QSettings
#from PySide6.QtCore import QFile
#from PySide6.QtCore import QUrl
#from PySide6.QtCore import QDir
from PySide6.QtCore import Qt
#from PySide6.QtCore import QSize
#from PySide6.QtCore import QMimeDatabase
#from PySide6.QtCore import QByteArray
#from PySide6.QtCore import QIODevice
#from PySide6.QtCore import QBuffer
#from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
#from PySide6.QtCore import QTemporaryFile

#from PySide6.QtPrintSupport import QPrinter
#from PySide6.QtPrintSupport import QPrintPreviewDialog
#from PySide6.QtPrintSupport import QPrintPreviewWidget
#from PySide6.QtPrintSupport import QPrinterInfo
#from PySide6.QtPrintSupport import QPrintDialog
#from PySide6.QtGui import QCursor
#from PySide6.QtGui import QIcon
#from PySide6.QtGui import QPixmap
#from PySide6.QtGui import QFont
#from PySide6.QtGui import QDesktopServices
#from PySide6.QtGui import QPdfWriter
#from PySide6.QtGui import QPagedPaintDevice
#from PySide6.QtWidgets import QStyle
#from PySide6.QtWidgets import qApp
#from PySide6.QtWidgets import QWidget
#from PySide6.QtWidgets import QLabel
#from PySide6.QtWidgets import QDialog
#from PySide6.QtWidgets import QDialogButtonBox
#from PySide6.QtWidgets import QToolBar
#from PySide6.QtWidgets import QAction
#from PySide6.QtWidgets import QFileDialog
#from PySide6.QtWidgets import QInputDialog
#from PySide6.QtWidgets import QMessageBox
#from PySide6.QtWidgets import QCheckBox
#from PySide6.QtWidgets import QSpinBox
#from PySide6.QtWidgets import QDoubleSpinBox
#from PySide6.QtWidgets import QLineEdit
#from PySide6.QtWidgets import QDateEdit
#from PySide6.QtWidgets import QDateTimeEdit
#from PySide6.QtWidgets import QComboBox
#from PySide6.QtWidgets import QMenu
#from PySide6.QtWidgets import QApplication

# application modules
#from App import session
#from App import currentIcon
from App.System import _tr
from App.System import string_decode
#from App.Ui.MessageDialog import Ui_MessageDialog
#from App.Ui.PrintPDFDialog import Ui_PrintPDFDialog
#from App.Ui.SelectImageDialog import Ui_SelectImageDialog
#from App.Ui.PrintDialog import Ui_PrintDialog
#from App.Ui.SortFilterDialog import Ui_SortFilterDialog
#from App.Ui.EventFilterDialog import Ui_EventFilterDialog
#from App.Ui.PrintPDFDialog import Ui_PrintPDFDialog
#from App.Ui.PrintEmailDialog import Ui_PrintEmailDialog
#from App.Database.Users import user_email_list
#from App.Database.User import user_email_details
#from App.Database.Users import user_email_signature
#from App.Database.CodeDescriptionList import userEmailList
#from App.Database.CodeDescriptionList import event_list

#from App.Database.Exceptions import PyAppDBError



class EmailException(Exception):
    pass


def sendEmail(account,
              file_name,
              attachment,
              subject,
              receiver,
              carbon_copy,
              blind_cc,
              sender_copy,
              content_txt,
              content_html):
    "Send an email with attachment"
    # get all account details for selected account id
    (sender_email, reply_to, server, port, user, enc_password,
         req_auth, req_ssl, req_tls, nn) = user_email_details(account)
    try:
        password = string_decode(enc_password)
    except InvalidToken as er:
        raise EmailException(_tr("Email", "Error in encryp/decrypt password"))
    # create an email message width the attached pdf file
    message = EmailMessage()
    message["Date"] = QDateTime.currentDateTime().toString(Qt.RFC2822Date)
    message["Subject"] = subject
    message["From"] = sender_email
    if reply_to:
        message["Reply-To"] = reply_to
    message["To"] = ", ".join(receiver.split(";"))
    if carbon_copy:
        message["Cc"] = ", ".join(carbon_copy.split(";"))
    bcc = []
    if blind_cc:  # avoid empty string
        bcc += blind_cc.split(";")
    if sender_copy:
        bcc.append(sender_email)
    if bcc:
        message["Bcc"] = ", ".join(bcc)
    message.set_content(content_txt)
    message.add_alternative(content_html, subtype="html")
    message.add_attachment(attachment,
                           maintype='application',
                           subtype='octet-stream',
                           filename=file_name)
    # Create a secure SSL context
    context = ssl.create_default_context()
    try:
        if req_ssl:
            with smtplib.SMTP_SSL(server, port, context=context) as smtp:
                if req_auth:
                    smtp.login(user, password)
                smtp.send_message(message)
        else:
            with smtplib.SMTP(server, port) as smtp:
                if req_tls:
                    smtp.starttls(context=context)
                if req_auth:
                    smtp.login(user, password)
                smtp.send_message(message)
    except smtplib.SMTPException as er:
        raise EmailException(er)

    except Exception as er:
        raise EmailException(er)



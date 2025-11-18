# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderProgressDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_OrderProgressDialog(object):
    def setupUi(self, OrderProgressDialog):
        if not OrderProgressDialog.objectName():
            OrderProgressDialog.setObjectName(u"OrderProgressDialog")
        OrderProgressDialog.resize(958, 397)
        self.verticalLayout_3 = QVBoxLayout(OrderProgressDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidgetBarcodeScans = QTableWidget(OrderProgressDialog)
        self.tableWidgetBarcodeScans.setObjectName(u"tableWidgetBarcodeScans")

        self.verticalLayout_3.addWidget(self.tableWidgetBarcodeScans)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(OrderProgressDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEditBarcode = QLineEdit(self.groupBox)
        self.lineEditBarcode.setObjectName(u"lineEditBarcode")

        self.verticalLayout_2.addWidget(self.lineEditBarcode)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(108, 55, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.groupBox_2 = QGroupBox(OrderProgressDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonMarkUnprocessed = QPushButton(self.groupBox_2)
        self.pushButtonMarkUnprocessed.setObjectName(u"pushButtonMarkUnprocessed")

        self.verticalLayout.addWidget(self.pushButtonMarkUnprocessed)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalSpacer_2 = QSpacerItem(108, 55, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.groupBox_3 = QGroupBox(OrderProgressDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButtonClose = QPushButton(self.groupBox_3)
        self.pushButtonClose.setObjectName(u"pushButtonClose")

        self.verticalLayout_5.addWidget(self.pushButtonClose)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.lineEditBarcode, self.pushButtonMarkUnprocessed)
        QWidget.setTabOrder(self.pushButtonMarkUnprocessed, self.pushButtonClose)
        QWidget.setTabOrder(self.pushButtonClose, self.tableWidgetBarcodeScans)

        self.retranslateUi(OrderProgressDialog)

        QMetaObject.connectSlotsByName(OrderProgressDialog)
    # setupUi

    def retranslateUi(self, OrderProgressDialog):
        OrderProgressDialog.setWindowTitle(QCoreApplication.translate("OrderProgressDialog", u"Order progress dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("OrderProgressDialog", u"Barcode scan", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("OrderProgressDialog", u"Edit scan", None))
        self.pushButtonMarkUnprocessed.setText(QCoreApplication.translate("OrderProgressDialog", u"Mark as unprocessed", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("OrderProgressDialog", u"Close dialog", None))
        self.pushButtonClose.setText(QCoreApplication.translate("OrderProgressDialog", u"Quit", None))
    # retranslateUi


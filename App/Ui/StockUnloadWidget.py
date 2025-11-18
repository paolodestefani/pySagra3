# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StockUnloadWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from App.Widget.View import EnhancedTableView

class Ui_StockUnloadWidget(object):
    def setupUi(self, StockUnloadWidget):
        if not StockUnloadWidget.objectName():
            StockUnloadWidget.setObjectName(u"StockUnloadWidget")
        StockUnloadWidget.resize(679, 471)
        self.verticalLayout_2 = QVBoxLayout(StockUnloadWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = EnhancedTableView(StockUnloadWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxAutomaticUpdate = QCheckBox(StockUnloadWidget)
        self.checkBoxAutomaticUpdate.setObjectName(u"checkBoxAutomaticUpdate")

        self.horizontalLayout.addWidget(self.checkBoxAutomaticUpdate)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(StockUnloadWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.dateTimeEdit = QDateTimeEdit(StockUnloadWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setCurrentSectionIndex(0)

        self.horizontalLayout.addWidget(self.dateTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(StockUnloadWidget)
        self.checkBoxAutomaticUpdate.clicked["bool"].connect(self.dateTimeEdit.setEnabled)

        QMetaObject.connectSlotsByName(StockUnloadWidget)
    # setupUi

    def retranslateUi(self, StockUnloadWidget):
        StockUnloadWidget.setWindowTitle(QCoreApplication.translate("StockUnloadWidget", u"Stock unload", None))
        self.checkBoxAutomaticUpdate.setText(QCoreApplication.translate("StockUnloadWidget", u"Automatic update", None))
        self.label.setText(QCoreApplication.translate("StockUnloadWidget", u"Last update:", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("StockUnloadWidget", u"MM/dd/yyyy HH:mm", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StockInventoryWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QSizePolicy, QSplitter, QVBoxLayout, QWidget)

from App.Widget.View import EnhancedTableView

class Ui_StockInventoryWidget(object):
    def setupUi(self, StockInventoryWidget):
        if not StockInventoryWidget.objectName():
            StockInventoryWidget.setObjectName(u"StockInventoryWidget")
        StockInventoryWidget.resize(640, 413)
        self.verticalLayout_4 = QVBoxLayout(StockInventoryWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(StockInventoryWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.tableViewItem = EnhancedTableView(self.layoutWidget)
        self.tableViewItem.setObjectName(u"tableViewItem")

        self.verticalLayout_3.addWidget(self.tableViewItem)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tableViewKit = EnhancedTableView(self.layoutWidget1)
        self.tableViewKit.setObjectName(u"tableViewKit")

        self.verticalLayout.addWidget(self.tableViewKit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableViewMenu = EnhancedTableView(self.layoutWidget1)
        self.tableViewMenu.setObjectName(u"tableViewMenu")

        self.verticalLayout_2.addWidget(self.tableViewMenu)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_4.addWidget(self.splitter)


        self.retranslateUi(StockInventoryWidget)

        QMetaObject.connectSlotsByName(StockInventoryWidget)
    # setupUi

    def retranslateUi(self, StockInventoryWidget):
        StockInventoryWidget.setWindowTitle(QCoreApplication.translate("StockInventoryWidget", u"Stock inventory", None))
        self.label_4.setText(QCoreApplication.translate("StockInventoryWidget", u"Normal items stock inventory", None))
        self.label.setText(QCoreApplication.translate("StockInventoryWidget", u"Kit availability", None))
        self.label_2.setText(QCoreApplication.translate("StockInventoryWidget", u"Menu availability", None))
    # retranslateUi


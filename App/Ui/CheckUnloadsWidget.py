# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CheckUnloadsWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QVBoxLayout,
    QWidget)

from App.Widget.View import EnhancedTableView

class Ui_CheckUnloadsWidget(object):
    def setupUi(self, CheckUnloadsWidget):
        if not CheckUnloadsWidget.objectName():
            CheckUnloadsWidget.setObjectName(u"CheckUnloadsWidget")
        CheckUnloadsWidget.resize(640, 480)
        self.verticalLayout = QVBoxLayout(CheckUnloadsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = EnhancedTableView(CheckUnloadsWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(CheckUnloadsWidget)

        QMetaObject.connectSlotsByName(CheckUnloadsWidget)
    # setupUi

    def retranslateUi(self, CheckUnloadsWidget):
        CheckUnloadsWidget.setWindowTitle(QCoreApplication.translate("CheckUnloadsWidget", u"Form", None))
    # retranslateUi


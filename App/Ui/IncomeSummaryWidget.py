# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IncomeSummaryWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHeaderView, QSizePolicy,
    QVBoxLayout, QWidget)

from App.Widget.View import EnhancedTableView

class Ui_IncomeSummaryWidget(object):
    def setupUi(self, IncomeSummaryWidget):
        if not IncomeSummaryWidget.objectName():
            IncomeSummaryWidget.setObjectName(u"IncomeSummaryWidget")
        IncomeSummaryWidget.resize(640, 480)
        self.verticalLayout = QVBoxLayout(IncomeSummaryWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = EnhancedTableView(IncomeSummaryWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.checkBoxDetail = QCheckBox(IncomeSummaryWidget)
        self.checkBoxDetail.setObjectName(u"checkBoxDetail")
        self.checkBoxDetail.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.verticalLayout.addWidget(self.checkBoxDetail)


        self.retranslateUi(IncomeSummaryWidget)

        QMetaObject.connectSlotsByName(IncomeSummaryWidget)
    # setupUi

    def retranslateUi(self, IncomeSummaryWidget):
        IncomeSummaryWidget.setWindowTitle(QCoreApplication.translate("IncomeSummaryWidget", u"Income summary", None))
        self.checkBoxDetail.setText(QCoreApplication.translate("IncomeSummaryWidget", u"Show daily detail", None))
    # retranslateUi


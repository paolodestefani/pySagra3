# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StatisticsViewerWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from App.Widget.View import EnhancedTableView

class Ui_StatisticsViewerWidget(object):
    def setupUi(self, StatisticsViewerWidget):
        if not StatisticsViewerWidget.objectName():
            StatisticsViewerWidget.setObjectName(u"StatisticsViewerWidget")
        StatisticsViewerWidget.resize(778, 474)
        self.verticalLayout_3 = QVBoxLayout(StatisticsViewerWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(StatisticsViewerWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBoxConfiguration = QComboBox(self.groupBox)
        self.comboBoxConfiguration.setObjectName(u"comboBoxConfiguration")

        self.verticalLayout.addWidget(self.comboBoxConfiguration)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(StatisticsViewerWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButtonExecute = QPushButton(self.groupBox_2)
        self.pushButtonExecute.setObjectName(u"pushButtonExecute")

        self.verticalLayout_2.addWidget(self.pushButtonExecute)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tableViewViewer = EnhancedTableView(StatisticsViewerWidget)
        self.tableViewViewer.setObjectName(u"tableViewViewer")

        self.verticalLayout_3.addWidget(self.tableViewViewer)


        self.retranslateUi(StatisticsViewerWidget)

        QMetaObject.connectSlotsByName(StatisticsViewerWidget)
    # setupUi

    def retranslateUi(self, StatisticsViewerWidget):
        StatisticsViewerWidget.setWindowTitle(QCoreApplication.translate("StatisticsViewerWidget", u"Statistics Viewer", None))
        self.groupBox.setTitle(QCoreApplication.translate("StatisticsViewerWidget", u"Configuration", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("StatisticsViewerWidget", u"Execute", None))
        self.pushButtonExecute.setText(QCoreApplication.translate("StatisticsViewerWidget", u"GO", None))
    # retranslateUi


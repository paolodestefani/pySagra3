# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShortcutsWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from App.Widget.View import EnhancedTableView

class Ui_ShortcutsWidget(object):
    def setupUi(self, ShortcutsWidget):
        if not ShortcutsWidget.objectName():
            ShortcutsWidget.setObjectName(u"ShortcutsWidget")
        ShortcutsWidget.resize(1033, 785)
        self.verticalLayout_6 = QVBoxLayout(ShortcutsWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(ShortcutsWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout = QVBoxLayout(self.page1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.page1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditCode = QLineEdit(self.groupBox_3)
        self.lineEditCode.setObjectName(u"lineEditCode")
        self.lineEditCode.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEditCode)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.checkBoxSystem = QCheckBox(self.page1)
        self.checkBoxSystem.setObjectName(u"checkBoxSystem")
        self.checkBoxSystem.setCheckable(True)

        self.verticalLayout_5.addWidget(self.checkBoxSystem)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.page1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonFillActions = QPushButton(self.groupBox_2)
        self.pushButtonFillActions.setObjectName(u"pushButtonFillActions")

        self.horizontalLayout.addWidget(self.pushButtonFillActions)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.page1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonDuplicate = QPushButton(self.groupBox_5)
        self.pushButtonDuplicate.setObjectName(u"pushButtonDuplicate")

        self.horizontalLayout_4.addWidget(self.pushButtonDuplicate)


        self.verticalLayout_5.addWidget(self.groupBox_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.page1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEditDescription = QLineEdit(self.groupBox_4)
        self.lineEditDescription.setObjectName(u"lineEditDescription")

        self.horizontalLayout_3.addWidget(self.lineEditDescription)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.tableViewKeySequence = EnhancedTableView(self.page1)
        self.tableViewKeySequence.setObjectName(u"tableViewKeySequence")

        self.verticalLayout_3.addWidget(self.tableViewKeySequence)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_4 = QVBoxLayout(self.page2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableView = EnhancedTableView(self.page2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        QWidget.setTabOrder(self.lineEditCode, self.lineEditDescription)
        QWidget.setTabOrder(self.lineEditDescription, self.checkBoxSystem)
        QWidget.setTabOrder(self.checkBoxSystem, self.pushButtonFillActions)
        QWidget.setTabOrder(self.pushButtonFillActions, self.tableViewKeySequence)
        QWidget.setTabOrder(self.tableViewKeySequence, self.tableView)

        self.retranslateUi(ShortcutsWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ShortcutsWidget)
    # setupUi

    def retranslateUi(self, ShortcutsWidget):
        ShortcutsWidget.setWindowTitle(QCoreApplication.translate("ShortcutsWidget", u"Shortcuts", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ShortcutsWidget", u"Code", None))
        self.checkBoxSystem.setText(QCoreApplication.translate("ShortcutsWidget", u"System shortcut scheme", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ShortcutsWidget", u"Actions", None))
        self.pushButtonFillActions.setText(QCoreApplication.translate("ShortcutsWidget", u"Fill actions", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ShortcutsWidget", u"Shortcuts management", None))
        self.pushButtonDuplicate.setText(QCoreApplication.translate("ShortcutsWidget", u"Duplicate", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ShortcutsWidget", u"Description", None))
    # retranslateUi


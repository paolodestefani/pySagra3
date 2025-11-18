# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderDialog0.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QDialog, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_OrderDialog0(object):
    def setupUi(self, OrderDialog0):
        if not OrderDialog0.objectName():
            OrderDialog0.setObjectName(u"OrderDialog0")
        OrderDialog0.setWindowModality(Qt.WindowModality.NonModal)
        OrderDialog0.resize(1151, 568)
        font = QFont()
        font.setPointSize(10)
        OrderDialog0.setFont(font)
        OrderDialog0.setSizeGripEnabled(True)
        self.verticalLayout_15 = QVBoxLayout(OrderDialog0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_4 = QGroupBox(OrderDialog0)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButtonTable = QRadioButton(self.groupBox_4)
        self.radioButtonTable.setObjectName(u"radioButtonTable")
        self.radioButtonTable.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButtonTable)

        self.radioButtonTakeAway = QRadioButton(self.groupBox_4)
        self.radioButtonTakeAway.setObjectName(u"radioButtonTakeAway")

        self.horizontalLayout_2.addWidget(self.radioButtonTakeAway)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(OrderDialog0)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEditTable = QLineEdit(self.groupBox_6)
        self.lineEditTable.setObjectName(u"lineEditTable")

        self.verticalLayout_8.addWidget(self.lineEditTable)


        self.horizontalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(OrderDialog0)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.spinBoxCovers = QSpinBox(self.groupBox_7)
        self.spinBoxCovers.setObjectName(u"spinBoxCovers")
        self.spinBoxCovers.setMinimum(0)
        self.spinBoxCovers.setMaximum(999)

        self.verticalLayout_9.addWidget(self.spinBoxCovers)


        self.horizontalLayout_4.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(OrderDialog0)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lineEditCustomerName = QLineEdit(self.groupBox_8)
        self.lineEditCustomerName.setObjectName(u"lineEditCustomerName")

        self.verticalLayout_10.addWidget(self.lineEditCustomerName)


        self.horizontalLayout_4.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(OrderDialog0)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lineEditCustomerContact = QLineEdit(self.groupBox_9)
        self.lineEditCustomerContact.setObjectName(u"lineEditCustomerContact")

        self.verticalLayout_17.addWidget(self.lineEditCustomerContact)


        self.horizontalLayout_4.addWidget(self.groupBox_9)

        self.groupBoxWebOrderFlag = QGroupBox(OrderDialog0)
        self.groupBoxWebOrderFlag.setObjectName(u"groupBoxWebOrderFlag")
        self.groupBoxWebOrderFlag.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBoxWebOrderFlag.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBoxWebOrderFlag.setFlat(True)
        self.verticalLayout_18 = QVBoxLayout(self.groupBoxWebOrderFlag)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.checkBoxWebOrder = QCheckBox(self.groupBoxWebOrderFlag)
        self.checkBoxWebOrder.setObjectName(u"checkBoxWebOrder")
        self.checkBoxWebOrder.setEnabled(True)
        self.checkBoxWebOrder.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_18.addWidget(self.checkBoxWebOrder)


        self.horizontalLayout_4.addWidget(self.groupBoxWebOrderFlag)

        self.groupBox_5 = QGroupBox(OrderDialog0)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEditBarCode = QLineEdit(self.groupBox_5)
        self.lineEditBarCode.setObjectName(u"lineEditBarCode")

        self.verticalLayout_11.addWidget(self.lineEditBarCode)


        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.pushButtonTablesSwitch = QPushButton(OrderDialog0)
        self.pushButtonTablesSwitch.setObjectName(u"pushButtonTablesSwitch")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTablesSwitch.sizePolicy().hasHeightForWidth())
        self.pushButtonTablesSwitch.setSizePolicy(sizePolicy)
        self.pushButtonTablesSwitch.setMinimumSize(QSize(120, 0))
        self.pushButtonTablesSwitch.setStyleSheet(u"text-align: left")
        self.pushButtonTablesSwitch.setIconSize(QSize(48, 48))

        self.horizontalLayout_4.addWidget(self.pushButtonTablesSwitch)

        self.lcdNumberTime = QLCDNumber(OrderDialog0)
        self.lcdNumberTime.setObjectName(u"lcdNumberTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lcdNumberTime.sizePolicy().hasHeightForWidth())
        self.lcdNumberTime.setSizePolicy(sizePolicy1)
        self.lcdNumberTime.setMinimumSize(QSize(250, 0))
        self.lcdNumberTime.setFrameShape(QFrame.Shape.NoFrame)
        self.lcdNumberTime.setSmallDecimalPoint(False)
        self.lcdNumberTime.setDigitCount(17)
        self.lcdNumberTime.setMode(QLCDNumber.Mode.Dec)
        self.lcdNumberTime.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumberTime.setProperty(u"value", 12345678901234568.000000000000000)

        self.horizontalLayout_4.addWidget(self.lcdNumberTime)


        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.stackedWidgetTableOrder = QStackedWidget(OrderDialog0)
        self.stackedWidgetTableOrder.setObjectName(u"stackedWidgetTableOrder")
        self.Order = QWidget()
        self.Order.setObjectName(u"Order")
        self.verticalLayout_12 = QVBoxLayout(self.Order)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidgetList = QTabWidget(self.Order)
        self.tabWidgetList.setObjectName(u"tabWidgetList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidgetList.sizePolicy().hasHeightForWidth())
        self.tabWidgetList.setSizePolicy(sizePolicy2)
        self.tabWidgetList.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.tabWidgetList.setFont(font1)
        self.tabWidgetList.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidgetList.setElideMode(Qt.TextElideMode.ElideRight)
        self.tabWidgetList.setTabsClosable(False)

        self.verticalLayout_2.addWidget(self.tabWidgetList)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonVariants = QPushButton(self.Order)
        self.pushButtonVariants.setObjectName(u"pushButtonVariants")
        self.pushButtonVariants.setIconSize(QSize(24, 24))
        self.pushButtonVariants.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButtonVariants)

        self.pushButtonShowLevel = QPushButton(self.Order)
        self.pushButtonShowLevel.setObjectName(u"pushButtonShowLevel")
        self.pushButtonShowLevel.setIconSize(QSize(24, 24))
        self.pushButtonShowLevel.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButtonShowLevel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.labelCashDeskDescription = QLabel(self.Order)
        self.labelCashDeskDescription.setObjectName(u"labelCashDeskDescription")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.labelCashDeskDescription.setFont(font2)
        self.labelCashDeskDescription.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelCashDeskDescription)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.groupBox = QGroupBox(self.Order)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton1 = QRadioButton(self.groupBox)
        self.radioButton1.setObjectName(u"radioButton1")
        self.radioButton1.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton1)

        self.radioButton5 = QRadioButton(self.groupBox)
        self.radioButton5.setObjectName(u"radioButton5")

        self.horizontalLayout.addWidget(self.radioButton5)

        self.radioButton10 = QRadioButton(self.groupBox)
        self.radioButton10.setObjectName(u"radioButton10")

        self.horizontalLayout.addWidget(self.radioButton10)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidgetOrder = QTableWidget(self.Order)
        self.tabWidgetOrder.setObjectName(u"tabWidgetOrder")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidgetOrder.sizePolicy().hasHeightForWidth())
        self.tabWidgetOrder.setSizePolicy(sizePolicy3)
        self.tabWidgetOrder.setMinimumSize(QSize(478, 0))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(11)
        self.tabWidgetOrder.setFont(font3)
        self.tabWidgetOrder.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabWidgetOrder.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tabWidgetOrder.setAutoScroll(False)
        self.tabWidgetOrder.setAutoScrollMargin(16)
        self.tabWidgetOrder.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabWidgetOrder.setAlternatingRowColors(True)
        self.tabWidgetOrder.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabWidgetOrder.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabWidgetOrder.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.tabWidgetOrder.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tabWidgetOrder.setRowCount(0)
        self.tabWidgetOrder.setColumnCount(0)
        self.tabWidgetOrder.horizontalHeader().setDefaultSectionSize(150)
        self.tabWidgetOrder.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.tabWidgetOrder)

        self.groupBox_2 = QGroupBox(self.Order)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setMinimumSize(QSize(478, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonDepartmentNote1 = QPushButton(self.groupBox_2)
        self.pushButtonDepartmentNote1.setObjectName(u"pushButtonDepartmentNote1")
        self.pushButtonDepartmentNote1.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButtonDepartmentNote1.sizePolicy().hasHeightForWidth())
        self.pushButtonDepartmentNote1.setSizePolicy(sizePolicy5)
        self.pushButtonDepartmentNote1.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.pushButtonDepartmentNote1)

        self.pushButtonDepartmentNote2 = QPushButton(self.groupBox_2)
        self.pushButtonDepartmentNote2.setObjectName(u"pushButtonDepartmentNote2")
        self.pushButtonDepartmentNote2.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.pushButtonDepartmentNote2.sizePolicy().hasHeightForWidth())
        self.pushButtonDepartmentNote2.setSizePolicy(sizePolicy5)
        self.pushButtonDepartmentNote2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.pushButtonDepartmentNote2)

        self.pushButtonDepartmentNote3 = QPushButton(self.groupBox_2)
        self.pushButtonDepartmentNote3.setObjectName(u"pushButtonDepartmentNote3")
        self.pushButtonDepartmentNote3.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.pushButtonDepartmentNote3.sizePolicy().hasHeightForWidth())
        self.pushButtonDepartmentNote3.setSizePolicy(sizePolicy5)
        self.pushButtonDepartmentNote3.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.pushButtonDepartmentNote3)

        self.pushButtonDepartmentNote4 = QPushButton(self.groupBox_2)
        self.pushButtonDepartmentNote4.setObjectName(u"pushButtonDepartmentNote4")
        self.pushButtonDepartmentNote4.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.pushButtonDepartmentNote4.sizePolicy().hasHeightForWidth())
        self.pushButtonDepartmentNote4.setSizePolicy(sizePolicy5)
        self.pushButtonDepartmentNote4.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.pushButtonDepartmentNote4)

        self.pushButtonDepartmentNote5 = QPushButton(self.groupBox_2)
        self.pushButtonDepartmentNote5.setObjectName(u"pushButtonDepartmentNote5")
        self.pushButtonDepartmentNote5.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.pushButtonDepartmentNote5.sizePolicy().hasHeightForWidth())
        self.pushButtonDepartmentNote5.setSizePolicy(sizePolicy5)
        self.pushButtonDepartmentNote5.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.pushButtonDepartmentNote5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.Order)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy4.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy4)
        self.groupBox_3.setMinimumSize(QSize(478, 0))
        self.groupBox_3.setMaximumSize(QSize(478, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBoxSubTotal = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxSubTotal.setObjectName(u"doubleSpinBoxSubTotal")
        self.doubleSpinBoxSubTotal.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.doubleSpinBoxSubTotal.setFrame(True)
        self.doubleSpinBoxSubTotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBoxSubTotal.setReadOnly(True)
        self.doubleSpinBoxSubTotal.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBoxSubTotal.setProperty(u"showGroupSeparator", True)
        self.doubleSpinBoxSubTotal.setMaximum(9999.989999999999782)

        self.gridLayout.addWidget(self.doubleSpinBoxSubTotal, 1, 0, 1, 1)

        self.doubleSpinBoxDiscount = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxDiscount.setObjectName(u"doubleSpinBoxDiscount")
        self.doubleSpinBoxDiscount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBoxDiscount.setProperty(u"showGroupSeparator", True)
        self.doubleSpinBoxDiscount.setMaximum(9999.989999999999782)

        self.gridLayout.addWidget(self.doubleSpinBoxDiscount, 1, 1, 1, 1)

        self.doubleSpinBoxTotal = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxTotal.setObjectName(u"doubleSpinBoxTotal")
        self.doubleSpinBoxTotal.setFont(font1)
        self.doubleSpinBoxTotal.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.doubleSpinBoxTotal.setFrame(True)
        self.doubleSpinBoxTotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBoxTotal.setReadOnly(True)
        self.doubleSpinBoxTotal.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBoxTotal.setProperty(u"showGroupSeparator", True)
        self.doubleSpinBoxTotal.setMaximum(9999.989999999999782)

        self.gridLayout.addWidget(self.doubleSpinBoxTotal, 1, 2, 1, 1)

        self.checkBoxElectronicPayment = QCheckBox(self.groupBox_3)
        self.checkBoxElectronicPayment.setObjectName(u"checkBoxElectronicPayment")

        self.gridLayout.addWidget(self.checkBoxElectronicPayment, 1, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonConfirm = QPushButton(self.groupBox_3)
        self.pushButtonConfirm.setObjectName(u"pushButtonConfirm")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButtonConfirm.sizePolicy().hasHeightForWidth())
        self.pushButtonConfirm.setSizePolicy(sizePolicy7)
        self.pushButtonConfirm.setMinimumSize(QSize(150, 0))
        self.pushButtonConfirm.setFont(font5)
        self.pushButtonConfirm.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButtonConfirm)

        self.pushButtonCancel = QPushButton(self.groupBox_3)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        sizePolicy7.setHeightForWidth(self.pushButtonCancel.sizePolicy().hasHeightForWidth())
        self.pushButtonCancel.setSizePolicy(sizePolicy7)
        self.pushButtonCancel.setMinimumSize(QSize(120, 0))
        font6 = QFont()
        font6.setPointSize(12)
        self.pushButtonCancel.setFont(font6)
        self.pushButtonCancel.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButtonCancel)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.doubleSpinBoxCash = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxCash.setObjectName(u"doubleSpinBoxCash")
        self.doubleSpinBoxCash.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBoxCash.setProperty(u"showGroupSeparator", True)
        self.doubleSpinBoxCash.setMaximum(9999.989999999999782)

        self.gridLayout_2.addWidget(self.doubleSpinBoxCash, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.doubleSpinBoxChange = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxChange.setObjectName(u"doubleSpinBoxChange")
        self.doubleSpinBoxChange.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBoxChange.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBoxChange.setProperty(u"showGroupSeparator", True)
        self.doubleSpinBoxChange.setMaximum(9999.989999999999782)

        self.gridLayout_2.addWidget(self.doubleSpinBoxChange, 1, 1, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addWidget(self.groupBox_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.stackedWidgetTableOrder.addWidget(self.Order)
        self.Tables = QWidget()
        self.Tables.setObjectName(u"Tables")
        self.verticalLayout_7 = QVBoxLayout(self.Tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.Tables)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 74, 16))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frameTables = QFrame(self.scrollAreaWidgetContents)
        self.frameTables.setObjectName(u"frameTables")
        self.frameTables.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTables.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_13.addWidget(self.frameTables)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.stackedWidgetTableOrder.addWidget(self.Tables)

        self.verticalLayout_14.addWidget(self.stackedWidgetTableOrder)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        QWidget.setTabOrder(self.lineEditTable, self.spinBoxCovers)
        QWidget.setTabOrder(self.spinBoxCovers, self.lineEditCustomerName)
        QWidget.setTabOrder(self.lineEditCustomerName, self.tabWidgetList)
        QWidget.setTabOrder(self.tabWidgetList, self.tabWidgetOrder)
        QWidget.setTabOrder(self.tabWidgetOrder, self.pushButtonVariants)
        QWidget.setTabOrder(self.pushButtonVariants, self.pushButtonShowLevel)
        QWidget.setTabOrder(self.pushButtonShowLevel, self.radioButton1)
        QWidget.setTabOrder(self.radioButton1, self.radioButton5)
        QWidget.setTabOrder(self.radioButton5, self.radioButton10)
        QWidget.setTabOrder(self.radioButton10, self.pushButtonDepartmentNote1)
        QWidget.setTabOrder(self.pushButtonDepartmentNote1, self.pushButtonDepartmentNote2)
        QWidget.setTabOrder(self.pushButtonDepartmentNote2, self.pushButtonDepartmentNote3)
        QWidget.setTabOrder(self.pushButtonDepartmentNote3, self.pushButtonDepartmentNote4)
        QWidget.setTabOrder(self.pushButtonDepartmentNote4, self.pushButtonDepartmentNote5)
        QWidget.setTabOrder(self.pushButtonDepartmentNote5, self.pushButtonConfirm)
        QWidget.setTabOrder(self.pushButtonConfirm, self.pushButtonCancel)
        QWidget.setTabOrder(self.pushButtonCancel, self.radioButtonTable)
        QWidget.setTabOrder(self.radioButtonTable, self.radioButtonTakeAway)

        self.retranslateUi(OrderDialog0)

        self.stackedWidgetTableOrder.setCurrentIndex(0)
        self.tabWidgetList.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(OrderDialog0)
    # setupUi

    def retranslateUi(self, OrderDialog0):
        OrderDialog0.setWindowTitle(QCoreApplication.translate("OrderDialog0", u"Order dialog", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("OrderDialog0", u"Deliver to", None))
        self.radioButtonTable.setText(QCoreApplication.translate("OrderDialog0", u"Table", None))
        self.radioButtonTakeAway.setText(QCoreApplication.translate("OrderDialog0", u"Take-away", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("OrderDialog0", u"Table number", None))
        self.lineEditTable.setInputMask("")
        self.groupBox_7.setTitle(QCoreApplication.translate("OrderDialog0", u"Covers", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("OrderDialog0", u"Customer name", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("OrderDialog0", u"Customer contact", None))
        self.groupBoxWebOrderFlag.setTitle(QCoreApplication.translate("OrderDialog0", u"WO", None))
#if QT_CONFIG(tooltip)
        self.checkBoxWebOrder.setToolTip(QCoreApplication.translate("OrderDialog0", u"Checked if this order was imported from an web order QRC or number", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxWebOrder.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("OrderDialog0", u"Web order input", None))
#if QT_CONFIG(tooltip)
        self.lineEditBarCode.setToolTip(QCoreApplication.translate("OrderDialog0", u"Press Ctrl+F11 to set focus here", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lcdNumberTime.setToolTip(QCoreApplication.translate("OrderDialog0", u"Press Ctrl+F12 to change date and time", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonVariants.setText(QCoreApplication.translate("OrderDialog0", u"Choose variants", None))
        self.pushButtonShowLevel.setText(QCoreApplication.translate("OrderDialog0", u"Show stock", None))
        self.labelCashDeskDescription.setText(QCoreApplication.translate("OrderDialog0", u"Cash description", None))
        self.groupBox.setTitle(QCoreApplication.translate("OrderDialog0", u"Quantity", None))
        self.radioButton1.setText(QCoreApplication.translate("OrderDialog0", u"1", None))
        self.radioButton5.setText(QCoreApplication.translate("OrderDialog0", u"5", None))
        self.radioButton10.setText(QCoreApplication.translate("OrderDialog0", u"10", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("OrderDialog0", u"Department notes", None))
        self.pushButtonDepartmentNote1.setText("")
        self.pushButtonDepartmentNote2.setText("")
        self.pushButtonDepartmentNote3.setText("")
        self.pushButtonDepartmentNote4.setText("")
        self.pushButtonDepartmentNote5.setText("")
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("OrderDialog0", u"Amount", None))
        self.label.setText(QCoreApplication.translate("OrderDialog0", u"Discount", None))
        self.label_7.setText(QCoreApplication.translate("OrderDialog0", u"Total", None))
        self.label_5.setText(QCoreApplication.translate("OrderDialog0", u"Elect. Paym.", None))
        self.checkBoxElectronicPayment.setText("")
        self.pushButtonConfirm.setText(QCoreApplication.translate("OrderDialog0", u"Confirm", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("OrderDialog0", u"Cancel", None))
        self.label_9.setText(QCoreApplication.translate("OrderDialog0", u"Cash", None))
        self.label_10.setText(QCoreApplication.translate("OrderDialog0", u"Change", None))
    # retranslateUi


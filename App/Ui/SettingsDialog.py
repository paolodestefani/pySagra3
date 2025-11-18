# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFontComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

from App.Widget.Control import RelationalComboBox

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        SettingsDialog.resize(764, 750)
        self.verticalLayout_17 = QVBoxLayout(SettingsDialog)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tabWidget = QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_6 = QVBoxLayout(self.tab1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_6 = QGroupBox(self.tab1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)

        self.verticalSliderLunch = QSlider(self.groupBox_6)
        self.verticalSliderLunch.setObjectName(u"verticalSliderLunch")
        self.verticalSliderLunch.setMinimum(0)
        self.verticalSliderLunch.setMaximum(24)
        self.verticalSliderLunch.setSingleStep(1)
        self.verticalSliderLunch.setPageStep(8)
        self.verticalSliderLunch.setValue(11)
        self.verticalSliderLunch.setTracking(True)
        self.verticalSliderLunch.setOrientation(Qt.Orientation.Vertical)
        self.verticalSliderLunch.setInvertedAppearance(False)
        self.verticalSliderLunch.setInvertedControls(False)
        self.verticalSliderLunch.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.verticalSliderLunch.setTickInterval(1)

        self.gridLayout_3.addWidget(self.verticalSliderLunch, 1, 0, 1, 1)

        self.verticalSliderDinner = QSlider(self.groupBox_6)
        self.verticalSliderDinner.setObjectName(u"verticalSliderDinner")
        self.verticalSliderDinner.setMaximum(24)
        self.verticalSliderDinner.setPageStep(8)
        self.verticalSliderDinner.setValue(18)
        self.verticalSliderDinner.setOrientation(Qt.Orientation.Vertical)
        self.verticalSliderDinner.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.verticalSliderDinner.setTickInterval(1)

        self.gridLayout_3.addWidget(self.verticalSliderDinner, 1, 1, 1, 1)

        self.spinBoxLunch = QSpinBox(self.groupBox_6)
        self.spinBoxLunch.setObjectName(u"spinBoxLunch")
        self.spinBoxLunch.setMaximum(24)
        self.spinBoxLunch.setValue(11)

        self.gridLayout_3.addWidget(self.spinBoxLunch, 2, 0, 1, 1)

        self.spinBoxDinner = QSpinBox(self.groupBox_6)
        self.spinBoxDinner.setObjectName(u"spinBoxDinner")
        self.spinBoxDinner.setMaximum(24)
        self.spinBoxDinner.setValue(18)

        self.gridLayout_3.addWidget(self.spinBoxDinner, 2, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_3)


        self.horizontalLayout_9.addWidget(self.groupBox_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_7 = QGroupBox(self.tab1)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBoxOrderUI = QComboBox(self.groupBox_7)
        self.comboBoxOrderUI.setObjectName(u"comboBoxOrderUI")

        self.verticalLayout_3.addWidget(self.comboBoxOrderUI)


        self.horizontalLayout_8.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.tab1)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBoxTabPosition = QComboBox(self.groupBox_8)
        self.comboBoxTabPosition.setObjectName(u"comboBoxTabPosition")

        self.verticalLayout_4.addWidget(self.comboBoxTabPosition)


        self.horizontalLayout_8.addWidget(self.groupBox_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_11 = QGroupBox(self.tab1)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.radioButtonTable = QRadioButton(self.groupBox_11)
        self.radioButtonTable.setObjectName(u"radioButtonTable")
        self.radioButtonTable.setChecked(True)

        self.horizontalLayout_15.addWidget(self.radioButtonTable)

        self.radioButtonTakeaway = QRadioButton(self.groupBox_11)
        self.radioButtonTakeaway.setObjectName(u"radioButtonTakeaway")

        self.horizontalLayout_15.addWidget(self.radioButtonTakeaway)


        self.verticalLayout_25.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_5.addWidget(self.groupBox_11)

        self.groupBox_9 = QGroupBox(self.tab1)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButtonCash = QRadioButton(self.groupBox_9)
        self.radioButtonCash.setObjectName(u"radioButtonCash")
        self.radioButtonCash.setChecked(True)

        self.horizontalLayout_7.addWidget(self.radioButtonCash)

        self.radioButtonElectronic = QRadioButton(self.groupBox_9)
        self.radioButtonElectronic.setObjectName(u"radioButtonElectronic")

        self.horizontalLayout_7.addWidget(self.radioButtonElectronic)


        self.verticalLayout_23.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_5.addWidget(self.groupBox_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.checkBoxUseTableList = QCheckBox(self.tab1)
        self.checkBoxUseTableList.setObjectName(u"checkBoxUseTableList")

        self.verticalLayout_5.addWidget(self.checkBoxUseTableList)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spinBoxOrderListFontSize = QSpinBox(self.groupBox)
        self.spinBoxOrderListFontSize.setObjectName(u"spinBoxOrderListFontSize")
        self.spinBoxOrderListFontSize.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.spinBoxOrderListFontSize, 4, 1, 1, 1)

        self.spinBoxOrderListColumns = QSpinBox(self.groupBox)
        self.spinBoxOrderListColumns.setObjectName(u"spinBoxOrderListColumns")
        self.spinBoxOrderListColumns.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.spinBoxOrderListColumns, 1, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.fontComboBoxOrderList = QFontComboBox(self.groupBox)
        self.fontComboBoxOrderList.setObjectName(u"fontComboBoxOrderList")

        self.gridLayout_5.addWidget(self.fontComboBoxOrderList, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.spinBoxOrderListRows = QSpinBox(self.groupBox)
        self.spinBoxOrderListRows.setObjectName(u"spinBoxOrderListRows")
        self.spinBoxOrderListRows.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.spinBoxOrderListRows, 0, 1, 1, 1)

        self.spinBoxOrderListSpacing = QSpinBox(self.groupBox)
        self.spinBoxOrderListSpacing.setObjectName(u"spinBoxOrderListSpacing")
        self.spinBoxOrderListSpacing.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.spinBoxOrderListSpacing, 2, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_5)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.tab1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 3, 0, 1, 1)

        self.spinBoxTableListRows = QSpinBox(self.groupBox_3)
        self.spinBoxTableListRows.setObjectName(u"spinBoxTableListRows")
        self.spinBoxTableListRows.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.spinBoxTableListRows, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)

        self.spinBoxTableListColumns = QSpinBox(self.groupBox_3)
        self.spinBoxTableListColumns.setObjectName(u"spinBoxTableListColumns")
        self.spinBoxTableListColumns.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.spinBoxTableListColumns, 1, 1, 1, 1)

        self.spinBoxTableListSpacing = QSpinBox(self.groupBox_3)
        self.spinBoxTableListSpacing.setObjectName(u"spinBoxTableListSpacing")
        self.spinBoxTableListSpacing.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.spinBoxTableListSpacing, 2, 1, 1, 1)

        self.fontComboBoxTableList = QFontComboBox(self.groupBox_3)
        self.fontComboBoxTableList.setObjectName(u"fontComboBoxTableList")

        self.gridLayout_6.addWidget(self.fontComboBoxTableList, 3, 1, 1, 1)

        self.spinBoxTableListFontSize = QSpinBox(self.groupBox_3)
        self.spinBoxTableListFontSize.setObjectName(u"spinBoxTableListFontSize")
        self.spinBoxTableListFontSize.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.spinBoxTableListFontSize, 4, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 4, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_6)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(self.tab1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelRed_2 = QLabel(self.groupBox_2)
        self.labelRed_2.setObjectName(u"labelRed_2")
        font = QFont()
        font.setBold(False)
        self.labelRed_2.setFont(font)
        self.labelRed_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelRed_2, 0, 1, 1, 1)

        self.pushButtonWB = QPushButton(self.groupBox_2)
        self.pushButtonWB.setObjectName(u"pushButtonWB")

        self.gridLayout_4.addWidget(self.pushButtonWB, 2, 2, 1, 1)

        self.pushButtonExampleNL = QPushButton(self.groupBox_2)
        self.pushButtonExampleNL.setObjectName(u"pushButtonExampleNL")

        self.gridLayout_4.addWidget(self.pushButtonExampleNL, 1, 4, 1, 1)

        self.spinBoxWarningLevel = QSpinBox(self.groupBox_2)
        self.spinBoxWarningLevel.setObjectName(u"spinBoxWarningLevel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxWarningLevel.sizePolicy().hasHeightForWidth())
        self.spinBoxWarningLevel.setSizePolicy(sizePolicy)
        self.spinBoxWarningLevel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spinBoxWarningLevel.setMinimum(2)
        self.spinBoxWarningLevel.setValue(10)

        self.gridLayout_4.addWidget(self.spinBoxWarningLevel, 2, 1, 1, 1)

        self.labelRed_3 = QLabel(self.groupBox_2)
        self.labelRed_3.setObjectName(u"labelRed_3")
        self.labelRed_3.setFont(font)
        self.labelRed_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelRed_3, 0, 4, 1, 1)

        self.pushButtonCB = QPushButton(self.groupBox_2)
        self.pushButtonCB.setObjectName(u"pushButtonCB")

        self.gridLayout_4.addWidget(self.pushButtonCB, 3, 2, 1, 1)

        self.labelYellow_2 = QLabel(self.groupBox_2)
        self.labelYellow_2.setObjectName(u"labelYellow_2")
        self.labelYellow_2.setFont(font)

        self.gridLayout_4.addWidget(self.labelYellow_2, 1, 0, 1, 1)

        self.pushButtonCT = QPushButton(self.groupBox_2)
        self.pushButtonCT.setObjectName(u"pushButtonCT")

        self.gridLayout_4.addWidget(self.pushButtonCT, 3, 3, 1, 1)

        self.pushButtonWT = QPushButton(self.groupBox_2)
        self.pushButtonWT.setObjectName(u"pushButtonWT")

        self.gridLayout_4.addWidget(self.pushButtonWT, 2, 3, 1, 1)

        self.pushButtonExampleWL = QPushButton(self.groupBox_2)
        self.pushButtonExampleWL.setObjectName(u"pushButtonExampleWL")

        self.gridLayout_4.addWidget(self.pushButtonExampleWL, 2, 4, 1, 1)

        self.labelYellow_4 = QLabel(self.groupBox_2)
        self.labelYellow_4.setObjectName(u"labelYellow_4")
        self.labelYellow_4.setFont(font)

        self.gridLayout_4.addWidget(self.labelYellow_4, 3, 0, 1, 1)

        self.pushButtonNB = QPushButton(self.groupBox_2)
        self.pushButtonNB.setObjectName(u"pushButtonNB")

        self.gridLayout_4.addWidget(self.pushButtonNB, 1, 2, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 4, 0, 1, 1)

        self.pushButtonExampleCL = QPushButton(self.groupBox_2)
        self.pushButtonExampleCL.setObjectName(u"pushButtonExampleCL")

        self.gridLayout_4.addWidget(self.pushButtonExampleCL, 3, 4, 1, 1)

        self.pushButtonExampleDL = QPushButton(self.groupBox_2)
        self.pushButtonExampleDL.setObjectName(u"pushButtonExampleDL")

        self.gridLayout_4.addWidget(self.pushButtonExampleDL, 4, 4, 1, 1)

        self.labelRed = QLabel(self.groupBox_2)
        self.labelRed.setObjectName(u"labelRed")
        self.labelRed.setFont(font)
        self.labelRed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelRed, 0, 3, 1, 1)

        self.spinBoxCriticalLevel = QSpinBox(self.groupBox_2)
        self.spinBoxCriticalLevel.setObjectName(u"spinBoxCriticalLevel")
        sizePolicy.setHeightForWidth(self.spinBoxCriticalLevel.sizePolicy().hasHeightForWidth())
        self.spinBoxCriticalLevel.setSizePolicy(sizePolicy)
        self.spinBoxCriticalLevel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spinBoxCriticalLevel.setMinimum(1)
        self.spinBoxCriticalLevel.setValue(5)

        self.gridLayout_4.addWidget(self.spinBoxCriticalLevel, 3, 1, 1, 1)

        self.pushButtonNT = QPushButton(self.groupBox_2)
        self.pushButtonNT.setObjectName(u"pushButtonNT")

        self.gridLayout_4.addWidget(self.pushButtonNT, 1, 3, 1, 1)

        self.labelYellow_3 = QLabel(self.groupBox_2)
        self.labelYellow_3.setObjectName(u"labelYellow_3")
        self.labelYellow_3.setFont(font)

        self.gridLayout_4.addWidget(self.labelYellow_3, 2, 0, 1, 1)

        self.pushButtonDT = QPushButton(self.groupBox_2)
        self.pushButtonDT.setObjectName(u"pushButtonDT")

        self.gridLayout_4.addWidget(self.pushButtonDT, 4, 3, 1, 1)

        self.labelYellow = QLabel(self.groupBox_2)
        self.labelYellow.setObjectName(u"labelYellow")
        self.labelYellow.setFont(font)
        self.labelYellow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelYellow, 0, 2, 1, 1)

        self.pushButtonDB = QPushButton(self.groupBox_2)
        self.pushButtonDB.setObjectName(u"pushButtonDB")

        self.gridLayout_4.addWidget(self.pushButtonDB, 4, 2, 1, 1)

        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_22, 1, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_23, 4, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnStretch(4, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_20 = QVBoxLayout(self.tab2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_4 = QGroupBox(self.tab2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelCopy_4 = QLabel(self.groupBox_4)
        self.labelCopy_4.setObjectName(u"labelCopy_4")

        self.gridLayout.addWidget(self.labelCopy_4, 0, 2, 1, 1)

        self.labelCopy = QLabel(self.groupBox_4)
        self.labelCopy.setObjectName(u"labelCopy")

        self.gridLayout.addWidget(self.labelCopy, 0, 1, 1, 1)

        self.labelCopy_3 = QLabel(self.groupBox_4)
        self.labelCopy_3.setObjectName(u"labelCopy_3")

        self.gridLayout.addWidget(self.labelCopy_3, 0, 3, 1, 1)

        self.labelCopy_2 = QLabel(self.groupBox_4)
        self.labelCopy_2.setObjectName(u"labelCopy_2")

        self.gridLayout.addWidget(self.labelCopy_2, 0, 0, 1, 1)

        self.comboBoxCustomerPrinter = RelationalComboBox(self.groupBox_4)
        self.comboBoxCustomerPrinter.setObjectName(u"comboBoxCustomerPrinter")
        self.comboBoxCustomerPrinter.setEnabled(False)

        self.gridLayout.addWidget(self.comboBoxCustomerPrinter, 1, 3, 1, 1)

        self.spinBoxCustomerCopies = QSpinBox(self.groupBox_4)
        self.spinBoxCustomerCopies.setObjectName(u"spinBoxCustomerCopies")
        self.spinBoxCustomerCopies.setEnabled(False)
        self.spinBoxCustomerCopies.setMinimum(1)

        self.gridLayout.addWidget(self.spinBoxCustomerCopies, 1, 1, 1, 1)

        self.comboBoxCustomerReport = RelationalComboBox(self.groupBox_4)
        self.comboBoxCustomerReport.setObjectName(u"comboBoxCustomerReport")
        self.comboBoxCustomerReport.setEnabled(False)

        self.gridLayout.addWidget(self.comboBoxCustomerReport, 1, 2, 1, 1)

        self.checkBoxCustomerCopy = QCheckBox(self.groupBox_4)
        self.checkBoxCustomerCopy.setObjectName(u"checkBoxCustomerCopy")
        self.checkBoxCustomerCopy.setChecked(False)

        self.gridLayout.addWidget(self.checkBoxCustomerCopy, 1, 0, 1, 1)

        self.spinBoxCoverCopies = QSpinBox(self.groupBox_4)
        self.spinBoxCoverCopies.setObjectName(u"spinBoxCoverCopies")
        self.spinBoxCoverCopies.setEnabled(False)
        self.spinBoxCoverCopies.setMinimum(1)

        self.gridLayout.addWidget(self.spinBoxCoverCopies, 7, 1, 1, 1)

        self.comboBoxCoverReport = RelationalComboBox(self.groupBox_4)
        self.comboBoxCoverReport.setObjectName(u"comboBoxCoverReport")
        self.comboBoxCoverReport.setEnabled(False)

        self.gridLayout.addWidget(self.comboBoxCoverReport, 7, 2, 1, 1)

        self.comboBoxDepartmentReport = RelationalComboBox(self.groupBox_4)
        self.comboBoxDepartmentReport.setObjectName(u"comboBoxDepartmentReport")
        self.comboBoxDepartmentReport.setEnabled(False)

        self.gridLayout.addWidget(self.comboBoxDepartmentReport, 3, 2, 1, 1)

        self.checkBoxDepartmentCopy = QCheckBox(self.groupBox_4)
        self.checkBoxDepartmentCopy.setObjectName(u"checkBoxDepartmentCopy")
        self.checkBoxDepartmentCopy.setChecked(False)

        self.gridLayout.addWidget(self.checkBoxDepartmentCopy, 3, 0, 1, 1)

        self.checkBoxCoverCopy = QCheckBox(self.groupBox_4)
        self.checkBoxCoverCopy.setObjectName(u"checkBoxCoverCopy")
        self.checkBoxCoverCopy.setChecked(False)

        self.gridLayout.addWidget(self.checkBoxCoverCopy, 7, 0, 1, 1)

        self.spinBoxDepartmentCopies = QSpinBox(self.groupBox_4)
        self.spinBoxDepartmentCopies.setObjectName(u"spinBoxDepartmentCopies")
        self.spinBoxDepartmentCopies.setEnabled(False)
        self.spinBoxDepartmentCopies.setMinimum(1)

        self.gridLayout.addWidget(self.spinBoxDepartmentCopies, 3, 1, 1, 1)

        self.comboBoxCoverPrinter = RelationalComboBox(self.groupBox_4)
        self.comboBoxCoverPrinter.setObjectName(u"comboBoxCoverPrinter")
        self.comboBoxCoverPrinter.setEnabled(False)

        self.gridLayout.addWidget(self.comboBoxCoverPrinter, 7, 3, 1, 1)

        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_19.addWidget(self.groupBox_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_20 = QLabel(self.tab2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.spinBoxMaxCovers = QSpinBox(self.tab2)
        self.spinBoxMaxCovers.setObjectName(u"spinBoxMaxCovers")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBoxMaxCovers.sizePolicy().hasHeightForWidth())
        self.spinBoxMaxCovers.setSizePolicy(sizePolicy1)
        self.spinBoxMaxCovers.setMinimum(0)
        self.spinBoxMaxCovers.setMaximum(999)
        self.spinBoxMaxCovers.setValue(0)

        self.horizontalLayout_6.addWidget(self.spinBoxMaxCovers)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.checkBoxOrderProgress = QCheckBox(self.tab2)
        self.checkBoxOrderProgress.setObjectName(u"checkBoxOrderProgress")

        self.horizontalLayout_6.addWidget(self.checkBoxOrderProgress)


        self.verticalLayout_19.addLayout(self.horizontalLayout_6)

        self.groupBox_5 = QGroupBox(self.tab2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBoxShowInventory = QCheckBox(self.groupBox_5)
        self.checkBoxShowInventory.setObjectName(u"checkBoxShowInventory")

        self.verticalLayout_8.addWidget(self.checkBoxShowInventory)

        self.checkBoxAutoVariants = QCheckBox(self.groupBox_5)
        self.checkBoxAutoVariants.setObjectName(u"checkBoxAutoVariants")

        self.verticalLayout_8.addWidget(self.checkBoxAutoVariants)

        self.checkBoxMandatoryTableNumber = QCheckBox(self.groupBox_5)
        self.checkBoxMandatoryTableNumber.setObjectName(u"checkBoxMandatoryTableNumber")

        self.verticalLayout_8.addWidget(self.checkBoxMandatoryTableNumber)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxInactivity = QCheckBox(self.groupBox_5)
        self.checkBoxInactivity.setObjectName(u"checkBoxInactivity")

        self.horizontalLayout.addWidget(self.checkBoxInactivity)

        self.spinBoxInactivityTime = QSpinBox(self.groupBox_5)
        self.spinBoxInactivityTime.setObjectName(u"spinBoxInactivityTime")
        self.spinBoxInactivityTime.setEnabled(False)
        self.spinBoxInactivityTime.setMinimum(30)
        self.spinBoxInactivityTime.setMaximum(1200)

        self.horizontalLayout.addWidget(self.spinBoxInactivityTime)

        self.labelInactivity = QLabel(self.groupBox_5)
        self.labelInactivity.setObjectName(u"labelInactivity")
        self.labelInactivity.setEnabled(False)

        self.horizontalLayout.addWidget(self.labelInactivity)


        self.verticalLayout_8.addLayout(self.horizontalLayout)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_19.addWidget(self.groupBox_5)

        self.verticalSpacer = QSpacerItem(380, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.verticalLayout_18 = QVBoxLayout(self.tab3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.groupBoxAutomaticUpdate = QGroupBox(self.tab3)
        self.groupBoxAutomaticUpdate.setObjectName(u"groupBoxAutomaticUpdate")
        self.groupBoxAutomaticUpdate.setCheckable(True)
        self.groupBoxAutomaticUpdate.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBoxAutomaticUpdate)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.groupBoxAutomaticUpdate)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.spinBoxAutomaticUpdateInterval = QSpinBox(self.groupBoxAutomaticUpdate)
        self.spinBoxAutomaticUpdateInterval.setObjectName(u"spinBoxAutomaticUpdateInterval")

        self.horizontalLayout_4.addWidget(self.spinBoxAutomaticUpdateInterval)

        self.label_19 = QLabel(self.groupBoxAutomaticUpdate)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_4.addWidget(self.label_19)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_4)


        self.verticalLayout_16.addWidget(self.groupBoxAutomaticUpdate)

        self.groupBoxStockUnloadReport = QGroupBox(self.tab3)
        self.groupBoxStockUnloadReport.setObjectName(u"groupBoxStockUnloadReport")
        self.groupBoxStockUnloadReport.setCheckable(True)
        self.groupBoxStockUnloadReport.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.groupBoxStockUnloadReport)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.groupBoxStockUnloadReport)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.spinBoxOrdersStartLevel = QSpinBox(self.groupBoxStockUnloadReport)
        self.spinBoxOrdersStartLevel.setObjectName(u"spinBoxOrdersStartLevel")
        sizePolicy1.setHeightForWidth(self.spinBoxOrdersStartLevel.sizePolicy().hasHeightForWidth())
        self.spinBoxOrdersStartLevel.setSizePolicy(sizePolicy1)
        self.spinBoxOrdersStartLevel.setMinimum(1)
        self.spinBoxOrdersStartLevel.setMaximum(1000)

        self.horizontalLayout_2.addWidget(self.spinBoxOrdersStartLevel)

        self.label_11 = QLabel(self.groupBoxStockUnloadReport)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.spinBoxOrdersNextLevel = QSpinBox(self.groupBoxStockUnloadReport)
        self.spinBoxOrdersNextLevel.setObjectName(u"spinBoxOrdersNextLevel")
        sizePolicy1.setHeightForWidth(self.spinBoxOrdersNextLevel.sizePolicy().hasHeightForWidth())
        self.spinBoxOrdersNextLevel.setSizePolicy(sizePolicy1)
        self.spinBoxOrdersNextLevel.setMinimum(1)
        self.spinBoxOrdersNextLevel.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.spinBoxOrdersNextLevel)

        self.label_12 = QLabel(self.groupBoxStockUnloadReport)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.groupBoxStockUnloadReport)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)

        self.labelCopy_5 = QLabel(self.groupBoxStockUnloadReport)
        self.labelCopy_5.setObjectName(u"labelCopy_5")

        self.gridLayout_2.addWidget(self.labelCopy_5, 0, 0, 1, 1)

        self.comboBoxStockUnloadReport = RelationalComboBox(self.groupBoxStockUnloadReport)
        self.comboBoxStockUnloadReport.setObjectName(u"comboBoxStockUnloadReport")

        self.gridLayout_2.addWidget(self.comboBoxStockUnloadReport, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBoxStockUnloadReport)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.comboBoxStockUnloadPrinterClass = RelationalComboBox(self.groupBoxStockUnloadReport)
        self.comboBoxStockUnloadPrinterClass.setObjectName(u"comboBoxStockUnloadPrinterClass")

        self.gridLayout_2.addWidget(self.comboBoxStockUnloadPrinterClass, 1, 2, 1, 1)

        self.spinBoxStockUnloadCopies = QSpinBox(self.groupBoxStockUnloadReport)
        self.spinBoxStockUnloadCopies.setObjectName(u"spinBoxStockUnloadCopies")
        self.spinBoxStockUnloadCopies.setMinimum(1)

        self.gridLayout_2.addWidget(self.spinBoxStockUnloadCopies, 1, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.verticalLayout_12.addLayout(self.gridLayout_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.verticalLayout_16.addWidget(self.groupBoxStockUnloadReport)

        self.verticalSpacer_3 = QSpacerItem(20, 98, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)


        self.verticalLayout_18.addLayout(self.verticalLayout_16)

        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.verticalLayout_22 = QVBoxLayout(self.tab4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_25 = QLabel(self.tab4)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 0, 3, 1, 1)

        self.lineEditCurrencySymbol = QLineEdit(self.tab4)
        self.lineEditCurrencySymbol.setObjectName(u"lineEditCurrencySymbol")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditCurrencySymbol.sizePolicy().hasHeightForWidth())
        self.lineEditCurrencySymbol.setSizePolicy(sizePolicy2)
        self.lineEditCurrencySymbol.setMaximumSize(QSize(100, 16777215))
        self.lineEditCurrencySymbol.setMaxLength(3)

        self.gridLayout_7.addWidget(self.lineEditCurrencySymbol, 0, 4, 1, 1)

        self.label_24 = QLabel(self.tab4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_7.addWidget(self.label_24, 0, 0, 1, 1)

        self.spinBoxQuantityDecimals = QSpinBox(self.tab4)
        self.spinBoxQuantityDecimals.setObjectName(u"spinBoxQuantityDecimals")
        self.spinBoxQuantityDecimals.setMaximum(2)

        self.gridLayout_7.addWidget(self.spinBoxQuantityDecimals, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 516, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab4, "")

        self.verticalLayout_13.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_13.addWidget(self.buttonBox)


        self.verticalLayout_17.addLayout(self.verticalLayout_13)

#if QT_CONFIG(shortcut)
        self.labelCopy_4.setBuddy(self.spinBoxCustomerCopies)
        self.labelCopy.setBuddy(self.spinBoxCustomerCopies)
        self.labelCopy_3.setBuddy(self.spinBoxCustomerCopies)
        self.labelCopy_2.setBuddy(self.spinBoxCustomerCopies)
        self.labelCopy_5.setBuddy(self.spinBoxCustomerCopies)
        self.label_25.setBuddy(self.lineEditCurrencySymbol)
        self.label_24.setBuddy(self.spinBoxQuantityDecimals)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        self.checkBoxCustomerCopy.clicked["bool"].connect(self.spinBoxCustomerCopies.setEnabled)
        self.checkBoxCoverCopy.clicked["bool"].connect(self.spinBoxCoverCopies.setEnabled)
        self.checkBoxDepartmentCopy.clicked["bool"].connect(self.spinBoxDepartmentCopies.setEnabled)
        self.verticalSliderLunch.valueChanged.connect(self.spinBoxLunch.setValue)
        self.verticalSliderDinner.valueChanged.connect(self.spinBoxDinner.setValue)
        self.checkBoxCustomerCopy.clicked["bool"].connect(self.comboBoxCustomerReport.setEnabled)
        self.checkBoxCoverCopy.clicked["bool"].connect(self.comboBoxCoverReport.setEnabled)
        self.checkBoxCustomerCopy.clicked["bool"].connect(self.comboBoxCustomerPrinter.setEnabled)
        self.checkBoxCoverCopy.clicked["bool"].connect(self.comboBoxCoverPrinter.setEnabled)
        self.checkBoxDepartmentCopy.clicked["bool"].connect(self.comboBoxDepartmentReport.setEnabled)
        self.checkBoxInactivity.clicked["bool"].connect(self.spinBoxInactivityTime.setEnabled)
        self.checkBoxInactivity.clicked["bool"].connect(self.labelInactivity.setEnabled)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("SettingsDialog", u"Lunch / Dinner start time", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Lunch", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Dinner", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("SettingsDialog", u"Order entry user interface", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("SettingsDialog", u"Department tab position", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("SettingsDialog", u"Default delivery", None))
        self.radioButtonTable.setText(QCoreApplication.translate("SettingsDialog", u"Table", None))
        self.radioButtonTakeaway.setText(QCoreApplication.translate("SettingsDialog", u"Takeaway", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("SettingsDialog", u"Default payment", None))
        self.radioButtonCash.setText(QCoreApplication.translate("SettingsDialog", u"Cash", None))
        self.radioButtonElectronic.setText(QCoreApplication.translate("SettingsDialog", u"Electronic", None))
        self.checkBoxUseTableList.setText(QCoreApplication.translate("SettingsDialog", u"Use table list", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Order list base geometry", None))
        self.label_13.setText(QCoreApplication.translate("SettingsDialog", u"Spacing", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Columns", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Rows", None))
        self.label_17.setText(QCoreApplication.translate("SettingsDialog", u"Font size", None))
        self.label_15.setText(QCoreApplication.translate("SettingsDialog", u"Font", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SettingsDialog", u"Table list base geometry", None))
        self.label_16.setText(QCoreApplication.translate("SettingsDialog", u"Font", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Rows", None))
        self.label_14.setText(QCoreApplication.translate("SettingsDialog", u"Spacing", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Columns", None))
        self.label_18.setText(QCoreApplication.translate("SettingsDialog", u"Font size", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsDialog", u"Visual alarm for stock level", None))
        self.labelRed_2.setText(QCoreApplication.translate("SettingsDialog", u"Stock level", None))
        self.pushButtonWB.setText("")
        self.pushButtonExampleNL.setText(QCoreApplication.translate("SettingsDialog", u"Normal", None))
        self.spinBoxWarningLevel.setPrefix("")
        self.labelRed_3.setText(QCoreApplication.translate("SettingsDialog", u"Example", None))
        self.pushButtonCB.setText("")
        self.labelYellow_2.setText(QCoreApplication.translate("SettingsDialog", u"Normal (default)", None))
        self.pushButtonCT.setText("")
        self.pushButtonWT.setText("")
        self.pushButtonExampleWL.setText(QCoreApplication.translate("SettingsDialog", u"Warning", None))
        self.labelYellow_4.setText(QCoreApplication.translate("SettingsDialog", u"Critical", None))
        self.pushButtonNB.setText("")
        self.label_21.setText(QCoreApplication.translate("SettingsDialog", u"Out of stock", None))
        self.pushButtonExampleCL.setText(QCoreApplication.translate("SettingsDialog", u"Critical", None))
        self.pushButtonExampleDL.setText(QCoreApplication.translate("SettingsDialog", u"Disabled", None))
        self.labelRed.setText(QCoreApplication.translate("SettingsDialog", u"Text color", None))
        self.pushButtonNT.setText("")
        self.labelYellow_3.setText(QCoreApplication.translate("SettingsDialog", u"Warning", None))
        self.pushButtonDT.setText("")
        self.labelYellow.setText(QCoreApplication.translate("SettingsDialog", u"Background color", None))
        self.pushButtonDB.setText("")
        self.label_22.setText(QCoreApplication.translate("SettingsDialog", u"> warning", None))
        self.label_23.setText(QCoreApplication.translate("SettingsDialog", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("SettingsDialog", u"Order entry", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SettingsDialog", u"Order printing settings", None))
        self.labelCopy_4.setText(QCoreApplication.translate("SettingsDialog", u"Report", None))
        self.labelCopy.setText(QCoreApplication.translate("SettingsDialog", u"# Copies", None))
        self.labelCopy_3.setText(QCoreApplication.translate("SettingsDialog", u"Printer class", None))
        self.labelCopy_2.setText(QCoreApplication.translate("SettingsDialog", u"Print", None))
        self.checkBoxCustomerCopy.setText(QCoreApplication.translate("SettingsDialog", u"Customer", None))
        self.checkBoxDepartmentCopy.setText(QCoreApplication.translate("SettingsDialog", u"Department", None))
        self.checkBoxCoverCopy.setText(QCoreApplication.translate("SettingsDialog", u"Cover", None))
        self.label_20.setText(QCoreApplication.translate("SettingsDialog", u"Max covers value", None))
        self.checkBoxOrderProgress.setText(QCoreApplication.translate("SettingsDialog", u"Manage order progress", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SettingsDialog", u"Form control", None))
        self.checkBoxShowInventory.setText(QCoreApplication.translate("SettingsDialog", u"Always show inventory", None))
        self.checkBoxAutoVariants.setText(QCoreApplication.translate("SettingsDialog", u"Automatic variants", None))
        self.checkBoxMandatoryTableNumber.setText(QCoreApplication.translate("SettingsDialog", u"Mandatory table number", None))
        self.checkBoxInactivity.setText(QCoreApplication.translate("SettingsDialog", u"Inactivity check after", None))
        self.labelInactivity.setText(QCoreApplication.translate("SettingsDialog", u"Seconds", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("SettingsDialog", u"Order print and control", None))
        self.groupBoxAutomaticUpdate.setTitle(QCoreApplication.translate("SettingsDialog", u"Stock unload automatic update", None))
        self.label_7.setText(QCoreApplication.translate("SettingsDialog", u"Update view after", None))
        self.label_19.setText(QCoreApplication.translate("SettingsDialog", u"seconds", None))
        self.groupBoxStockUnloadReport.setTitle(QCoreApplication.translate("SettingsDialog", u"Print stock unload report", None))
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"First print after", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDialog", u"orders then every", None))
        self.label_12.setText(QCoreApplication.translate("SettingsDialog", u"orders", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Report", None))
        self.labelCopy_5.setText(QCoreApplication.translate("SettingsDialog", u"# Copies", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"Printer class", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("SettingsDialog", u"Control report and view", None))
        self.label_25.setText(QCoreApplication.translate("SettingsDialog", u"Currency symbol", None))
        self.label_24.setText(QCoreApplication.translate("SettingsDialog", u"Decimal places for quantity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("SettingsDialog", u"Other", None))
    # retranslateUi


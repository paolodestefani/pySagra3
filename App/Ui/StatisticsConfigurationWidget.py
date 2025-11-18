# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StatisticsConfigurationWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFontComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

from App.Widget.Control import RelationalComboBox
from App.Widget.View import EnhancedTableView

class Ui_StatisticsConfigurationWidget(object):
    def setupUi(self, StatisticsConfigurationWidget):
        if not StatisticsConfigurationWidget.objectName():
            StatisticsConfigurationWidget.setObjectName(u"StatisticsConfigurationWidget")
        StatisticsConfigurationWidget.resize(1033, 653)
        self.verticalLayout_6 = QVBoxLayout(StatisticsConfigurationWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(StatisticsConfigurationWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.form = QWidget()
        self.form.setObjectName(u"form")
        self.verticalLayout_14 = QVBoxLayout(self.form)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_8 = QGroupBox(self.form)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lineEditCode = QLineEdit(self.groupBox_8)
        self.lineEditCode.setObjectName(u"lineEditCode")

        self.verticalLayout_8.addWidget(self.lineEditCode)


        self.horizontalLayout_4.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEditDescription = QLineEdit(self.groupBox_5)
        self.lineEditDescription.setObjectName(u"lineEditDescription")

        self.verticalLayout_12.addWidget(self.lineEditDescription)


        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.groupBox = QGroupBox(self.form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.comboBoxReport = RelationalComboBox(self.groupBox)
        self.comboBoxReport.setObjectName(u"comboBoxReport")

        self.verticalLayout_13.addWidget(self.comboBoxReport)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBoxTotalRow = QGroupBox(self.form)
        self.groupBoxTotalRow.setObjectName(u"groupBoxTotalRow")
        self.groupBoxTotalRow.setCheckable(True)
        self.groupBoxTotalRow.setChecked(True)
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxTotalRow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBoxTotalRow)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.spinBoxTotalsLabelColumn = QSpinBox(self.groupBoxTotalRow)
        self.spinBoxTotalsLabelColumn.setObjectName(u"spinBoxTotalsLabelColumn")
        self.spinBoxTotalsLabelColumn.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.spinBoxTotalsLabelColumn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.groupBoxTotalRow)

        self.groupBox_2 = QGroupBox(self.form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.spinBoxSorting = QSpinBox(self.groupBox_2)
        self.spinBoxSorting.setObjectName(u"spinBoxSorting")

        self.verticalLayout_10.addWidget(self.spinBoxSorting)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.checkBoxActive = QCheckBox(self.groupBox_4)
        self.checkBoxActive.setObjectName(u"checkBoxActive")

        self.verticalLayout_11.addWidget(self.checkBoxActive)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_6 = QGroupBox(self.form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textEditSqlQuery = QPlainTextEdit(self.groupBox_6)
        self.textEditSqlQuery.setObjectName(u"textEditSqlQuery")
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(10)
        self.textEditSqlQuery.setFont(font)

        self.verticalLayout_7.addWidget(self.textEditSqlQuery)


        self.verticalLayout_9.addWidget(self.groupBox_6)

        self.groupBox_3 = QGroupBox(self.form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEditGroupBy = QLineEdit(self.groupBox_3)
        self.lineEditGroupBy.setObjectName(u"lineEditGroupBy")

        self.verticalLayout_4.addWidget(self.lineEditGroupBy)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.verticalLayout_9.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.groupBox_7 = QGroupBox(self.form)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableViewColumns = EnhancedTableView(self.groupBox_7)
        self.tableViewColumns.setObjectName(u"tableViewColumns")

        self.verticalLayout_2.addWidget(self.tableViewColumns)


        self.horizontalLayout_2.addWidget(self.groupBox_7)


        self.verticalLayout_14.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.form)
        self.view = QWidget()
        self.view.setObjectName(u"view")
        self.verticalLayout = QVBoxLayout(self.view)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = EnhancedTableView(self.view)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.view)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(StatisticsConfigurationWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.fontComboBox = QFontComboBox(StatisticsConfigurationWidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setEditable(True)
        self.fontComboBox.setMaxVisibleItems(20)
        self.fontComboBox.setFontFilters(QFontComboBox.MonospacedFonts)
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(8)
        self.fontComboBox.setCurrentFont(font1)

        self.horizontalLayout.addWidget(self.fontComboBox)

        self.spinBoxFontSize = QSpinBox(StatisticsConfigurationWidget)
        self.spinBoxFontSize.setObjectName(u"spinBoxFontSize")

        self.horizontalLayout.addWidget(self.spinBoxFontSize)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonDownload = QPushButton(StatisticsConfigurationWidget)
        self.pushButtonDownload.setObjectName(u"pushButtonDownload")

        self.horizontalLayout.addWidget(self.pushButtonDownload)

        self.pushButtonUpload = QPushButton(StatisticsConfigurationWidget)
        self.pushButtonUpload.setObjectName(u"pushButtonUpload")

        self.horizontalLayout.addWidget(self.pushButtonUpload)

        self.pushButtonDownloadAll = QPushButton(StatisticsConfigurationWidget)
        self.pushButtonDownloadAll.setObjectName(u"pushButtonDownloadAll")

        self.horizontalLayout.addWidget(self.pushButtonDownloadAll)

        self.pushButtonUploadAll = QPushButton(StatisticsConfigurationWidget)
        self.pushButtonUploadAll.setObjectName(u"pushButtonUploadAll")

        self.horizontalLayout.addWidget(self.pushButtonUploadAll)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        QWidget.setTabOrder(self.fontComboBox, self.spinBoxFontSize)
        QWidget.setTabOrder(self.spinBoxFontSize, self.pushButtonDownload)
        QWidget.setTabOrder(self.pushButtonDownload, self.pushButtonUpload)
        QWidget.setTabOrder(self.pushButtonUpload, self.pushButtonDownloadAll)
        QWidget.setTabOrder(self.pushButtonDownloadAll, self.pushButtonUploadAll)
        QWidget.setTabOrder(self.pushButtonUploadAll, self.tableView)

        self.retranslateUi(StatisticsConfigurationWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StatisticsConfigurationWidget)
    # setupUi

    def retranslateUi(self, StatisticsConfigurationWidget):
        StatisticsConfigurationWidget.setWindowTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Report", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Code", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Configuration", None))
        self.groupBox.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Report", None))
        self.groupBoxTotalRow.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Totals row", None))
        self.label.setText(QCoreApplication.translate("StatisticsConfigurationWidget", u"\"TOTAL\" label column", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Sorting", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Active", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Sql query", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Sql group by fileds", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("StatisticsConfigurationWidget", u"Columns", None))
        self.label_5.setText(QCoreApplication.translate("StatisticsConfigurationWidget", u"Font", None))
        self.pushButtonDownload.setText(QCoreApplication.translate("StatisticsConfigurationWidget", u"Download ...", None))
        self.pushButtonUpload.setText(QCoreApplication.translate("StatisticsConfigurationWidget", u"Upload ...", None))
        self.pushButtonDownloadAll.setText(QCoreApplication.translate("StatisticsConfigurationWidget", u"Download all scripts...", None))
        self.pushButtonUploadAll.setText(QCoreApplication.translate("StatisticsConfigurationWidget", u"Upload all scripts ...", None))
    # retranslateUi


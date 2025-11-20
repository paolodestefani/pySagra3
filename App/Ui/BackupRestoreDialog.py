# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BackupRestoreDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QGroupBox, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_BackupRestoreDialog(object):
    def setupUi(self, BackupRestoreDialog):
        if not BackupRestoreDialog.objectName():
            BackupRestoreDialog.setObjectName(u"BackupRestoreDialog")
        BackupRestoreDialog.setWindowModality(Qt.ApplicationModal)
        BackupRestoreDialog.resize(573, 471)
        self.verticalLayout_6 = QVBoxLayout(BackupRestoreDialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(BackupRestoreDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(False)
        self.backup = QWidget()
        self.backup.setObjectName(u"backup")
        self.verticalLayout = QVBoxLayout(self.backup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.backup)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backup_filename_edit = QLineEdit(self.groupBox_2)
        self.backup_filename_edit.setObjectName(u"backup_filename_edit")
        self.backup_filename_edit.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.backup_filename_edit)

        self.backup_file_push = QPushButton(self.groupBox_2)
        self.backup_file_push.setObjectName(u"backup_file_push")

        self.horizontalLayout_2.addWidget(self.backup_file_push)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.companies_groupbox = QGroupBox(self.backup)
        self.companies_groupbox.setObjectName(u"companies_groupbox")
        self.verticalLayout_3 = QVBoxLayout(self.companies_groupbox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.company_current_rb = QRadioButton(self.companies_groupbox)
        self.company_current_rb.setObjectName(u"company_current_rb")

        self.horizontalLayout.addWidget(self.company_current_rb)

        self.companies_all_rb = QRadioButton(self.companies_groupbox)
        self.companies_all_rb.setObjectName(u"companies_all_rb")

        self.horizontalLayout.addWidget(self.companies_all_rb)

        self.companies_select = QRadioButton(self.companies_groupbox)
        self.companies_select.setObjectName(u"companies_select")

        self.horizontalLayout.addWidget(self.companies_select)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.companies_list = QListWidget(self.companies_groupbox)
        self.companies_list.setObjectName(u"companies_list")
        self.companies_list.setEnabled(True)
        self.companies_list.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_3.addWidget(self.companies_list)


        self.verticalLayout.addWidget(self.companies_groupbox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.common_data_check = QCheckBox(self.backup)
        self.common_data_check.setObjectName(u"common_data_check")
        self.common_data_check.setChecked(False)

        self.horizontalLayout_3.addWidget(self.common_data_check)

        self.system_data_check = QCheckBox(self.backup)
        self.system_data_check.setObjectName(u"system_data_check")

        self.horizontalLayout_3.addWidget(self.system_data_check)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.backup_push = QPushButton(self.backup)
        self.backup_push.setObjectName(u"backup_push")

        self.horizontalLayout_6.addWidget(self.backup_push)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.backup, "")
        self.restore = QWidget()
        self.restore.setObjectName(u"restore")
        self.verticalLayout_8 = QVBoxLayout(self.restore)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_3 = QGroupBox(self.restore)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.restore_filename_edit = QLineEdit(self.groupBox_3)
        self.restore_filename_edit.setObjectName(u"restore_filename_edit")
        self.restore_filename_edit.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.restore_filename_edit)

        self.restore_file_push = QPushButton(self.groupBox_3)
        self.restore_file_push.setObjectName(u"restore_file_push")

        self.horizontalLayout_4.addWidget(self.restore_file_push)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.restore)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.content_list = QListWidget(self.groupBox)
        self.content_list.setObjectName(u"content_list")

        self.verticalLayout_7.addWidget(self.content_list)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.restore_push = QPushButton(self.restore)
        self.restore_push.setObjectName(u"restore_push")

        self.horizontalLayout_7.addWidget(self.restore_push)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.restore, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.buttonBox = QDialogButtonBox(BackupRestoreDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.horizontalLayout_5.addWidget(self.buttonBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.retranslateUi(BackupRestoreDialog)
        self.buttonBox.rejected.connect(BackupRestoreDialog.reject)
        self.buttonBox.accepted.connect(BackupRestoreDialog.accept)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BackupRestoreDialog)
    # setupUi

    def retranslateUi(self, BackupRestoreDialog):
        BackupRestoreDialog.setWindowTitle(QCoreApplication.translate("BackupRestoreDialog", u"Backup/Restore", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("BackupRestoreDialog", u"Backup to file", None))
        self.backup_file_push.setText(QCoreApplication.translate("BackupRestoreDialog", u"Open ...", None))
        self.companies_groupbox.setTitle(QCoreApplication.translate("BackupRestoreDialog", u"Companies", None))
        self.company_current_rb.setText(QCoreApplication.translate("BackupRestoreDialog", u"Current", None))
        self.companies_all_rb.setText(QCoreApplication.translate("BackupRestoreDialog", u"All", None))
        self.companies_select.setText(QCoreApplication.translate("BackupRestoreDialog", u"Select", None))
        self.common_data_check.setText(QCoreApplication.translate("BackupRestoreDialog", u"Include common data", None))
        self.system_data_check.setText(QCoreApplication.translate("BackupRestoreDialog", u"Include system data", None))
        self.backup_push.setText(QCoreApplication.translate("BackupRestoreDialog", u"Backup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.backup), QCoreApplication.translate("BackupRestoreDialog", u"Backup", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("BackupRestoreDialog", u"Restore from file", None))
        self.restore_file_push.setText(QCoreApplication.translate("BackupRestoreDialog", u"Open ...", None))
        self.groupBox.setTitle(QCoreApplication.translate("BackupRestoreDialog", u"File content", None))
        self.restore_push.setText(QCoreApplication.translate("BackupRestoreDialog", u"Restore", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.restore), QCoreApplication.translate("BackupRestoreDialog", u"Restore", None))
    # retranslateUi


cd "App\Ui\"
REM create lib ui modules
"c:\windows\system32\forfiles.exe" /P "C:\PyWare\SMS\App\Ui" /M *.ui /c "cmd /c c:\Python310\Scripts\pyside6-uic -o @fname.py @file"
pause



cd "..\.."
REM resources only for login
"c:\Python310\scripts\pyside6-rcc" resources.qrc -o resources_rc.py 

REM translations without pro file login sources and form
"c:\Python310\Scripts\pyside6-lupdate" ^
	App\System\Login.py ^
	App\Ui\LoginDialog.ui ^
	-tr-function-alias translate+=_tr -noobsolete -ts login_it.ts 

REM translations without pro file SMS sources and forms
"c:\Python310\Scripts\pyside6-lupdate" ^
	SMS.py ^
	App\System\Activation.py ^
	App\System\BackupRestore.py ^
	App\System\Command.py ^
	App\System\Company.py ^
	App\System\Connections.py ^
	App\System\Constant.py ^
	App\System\Customization.py ^
	App\System\FreeField.py ^
	App\System\Help.py ^
	App\System\ImportExport.py ^
	App\System\ItemModelConfiguration.py ^
	App\System\Mainwindow.py ^
	App\System\Menu.py ^
	App\System\Preferences.py ^
	App\System\Profile.py ^
	App\System\Report.py ^
	App\System\Scripting.py ^
	App\System\SendMessage.py ^
	App\System\Shortcut.py ^
	App\System\User.py ^
	App\System\Utility.py ^
	App\Widget\Control.py ^
	App\Widget\Delegate.py ^
	App\Widget\Dialog.py ^
	App\Widget\Form.py ^
	App\Widget\Utility.py ^
	App\Widget\View.py ^
	^
	App\Ui\AccountingReasonWidget.ui ^
	App\Ui\AccountPOstingsWidget.ui ^
	App\Ui\ActivationDialog.ui ^
	App\Ui\BackupRestoreDialog.ui ^
	App\Ui\BankWidget.ui ^
	App\Ui\ChangeCompanyDialog.ui ^
	App\Ui\ChangePasswordDialog.ui ^
	App\Ui\COATemplateWidget.ui ^
	App\Ui\COAWidget.ui ^
	App\Ui\CompanyDefaultWidget.ui ^
	App\Ui\CompanyWidget.ui ^
	App\Ui\ConnectionsHistoryWidget.ui ^
	App\Ui\ConnectionsWidget.ui ^
	App\Ui\CustomizationDialog.ui ^
	App\Ui\DuplicateDialog.ui ^
	App\Ui\FreeFieldsWidget.ui ^
	App\Ui\HelpDialog.ui ^
	App\Ui\ImportExportDialog.ui ^
	App\Ui\ItemModelConfigurationWidget.ui ^
	App\Ui\JournalEntryWidget.ui ^
	App\Ui\LookUpDialog.ui ^
	App\Ui\MainWindow.ui ^
	App\Ui\MasterDataWidget.ui ^
	App\Ui\MenuWidget.ui ^
	App\Ui\MessageDialog.ui ^
	App\Ui\MessageWidget.ui ^
	App\Ui\NewCompanyDialog.ui ^
	App\Ui\PaymentWidget.ui ^
	App\Ui\PreferencesDialog.ui ^
	App\Ui\PrintDialog.ui ^
	App\Ui\PrintEmailDialog.ui ^
	App\Ui\PrintPDFDialog.ui ^
	App\Ui\ProfileWidget.ui ^
	App\Ui\ReportWidget.ui ^
	App\Ui\ScriptingWidget.ui ^
	App\Ui\SelectImageDialog.ui ^
	App\Ui\SendMessageDialog.ui ^
	App\Ui\SettingDialog.ui ^
	App\Ui\ShortcutWidget.ui ^
	App\Ui\SortFilterDialog.ui ^
	App\Ui\SystemInfoDialog.ui ^
	App\Ui\UserWidget.ui ^
	App\Ui\VatWidget.ui ^
	App\Ui\ViewSettingsDialog.ui ^
	-tr-function-alias translate+=_tr -noobsolete -ts SMS_it.ts 

pause

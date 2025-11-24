REM move to projec root
cd C:\pyWare\pySagra3

REM activate virtual env
CALL "C:\PyWare\.venv\pyside6psycopg\Scripts\activate.bat"

REM create lib ui modules
"c:\windows\system32\forfiles.exe" /P "App\Ui" /M *.ui /c "cmd /c pyside6-uic -o @fname.py @file"

REM resources
pyside6-rcc resources.qrc -o resources_rc.py 

REM translations without pro file login sources and form
pyside6-lupdate ^
	App\System\Login.py ^
	App\Ui\LoginDialog.ui ^
	-tr-function-alias translate+=_tr -noobsolete -ts login_it.ts 
    
pyside6-lrelease translation\ts\login_it.ts -qm translation\login_it.qm

REM translations without pro file SMS sources and forms
pyside6-lupdate ^
	pySagra.py ^
	App/System/Connection.py ^
	App/System/Customization.py ^
	App/System/Help.py ^
	App/System/Mainwindow.py ^
	App/System/Menu.py ^
	App/System/Preferences.py ^
	App/System/Profile.py ^
	App/System/Report.py ^
	App/System/Scripting.py ^
	App/System/User.py ^
	App/System/Utility.py ^
	App/Widget/Control.py ^
	App/Widget/Delegate.py ^
	App/Widget/Dialog.py ^
	App/Widget/Form.py ^
	-tr-function-alias translate+=_tr -noobsolete -ts ts/pySagra_it.ts 
    
pyside6-lrelease translation\ts\pySagra_it.ts -qm translation\pySagra_it.qm


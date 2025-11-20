#!/bin/zsh

# move to projec root
cd /Users/paolo/Development/pySagra3

# activate virtual env
source /Users/paolo/Development/venv/pyside-ppg/bin/activate

# create lib ui modules
for filename in App/Ui/*.ui; do
    pyside6-uic -o "${filename%.*}".py "$filename"
done

# resources
pyside6-rcc resources.qrc -o resources_rc.py 

# transaltion for login dialog
pyside6-lupdate \
	App/System/Login.py \
	App/Ui/LoginDialog.ui \
	-tr-function-alias translate+=_tr -noobsolete -ts translation/ts/login_it.ts 
	
pyside6-lrelease translation/ts/login_it.ts -qm translation/login_it.qm

# translations without pro file, sources and forms
pyside6-lupdate	\
	pySagra.py \
	App/System/Connection.py \
	App/System/Customization.py \
	App/System/Help.py \
	App/System/Mainwindow.py \
	App/System/Menu.py \
	App/System/Preferences.py \
	App/System/Profile.py \
	App/System/Report.py \
	App/System/Scripting.py \
	App/System/User.py \
	App/System/Utility.py \
	App/Widget/Control.py \
	App/Widget/Delegate.py \
	App/Widget/Dialog.py \
	App/Widget/Form.py \
	-tr-function-alias translate+=_tr -noobsolete -ts translation/ts/pySagra_it.ts 

pyside6-lrelease translation/ts/pySagra_it.ts -qm translation/pySagra_it.qm

# exit from venv
deactivate


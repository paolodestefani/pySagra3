#!/bin/zsh

# move to projec root
cd /Users/paolo/Development/pySagra3

# activate virtual env
source /Users/paolo/Development/venv/pyside-ppg/bin/activate

#pyinstaller --clean --onedir --icon pySagra.ico --paths "C:\Python37-32\Lib\site-packages\PyQt5\Qt\bin" --windowed pySagra.py
pyinstaller --clean \
	--onedir \
	--icon pySagra.icns \
	--windowed \
	--exclude-module PySide6.QtDBus \
	--exclude-module PySide6.QtQml \
	--exclude-module PySide6.QtQuick \
	pySagra.py

# exit from venv
deactivate

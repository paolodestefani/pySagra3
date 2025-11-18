REM creazione pacchetto per pySagra 2.0

REM utilizzo di un virtual enviroment

REM CD \PyWare\.venv\pyqt5psycopg2\Scripts\Activate.bat

REM CD \PyWare\pySagra\2.0

REM creazione pacchetto su file unico
REM pyinstaller -w -F --icon pySagra.ico --paths "C:\Python35-32\Lib\site-packages\PyQt5\Qt\bin" --windowed pySagra.py

REM creazione pacchetto su directory
REM pyinstaller --clean --onedir --icon pySagra.ico --paths "C:\Python37-32\Lib\site-packages\PyQt5\Qt\bin" --windowed pySagra.py
pyinstaller --clean ^
	--onedir ^
	--icon pySagra.ico ^
	--windowed ^
	--exclude-module PyQt5.QtDBus ^
	--exclude-module PyQt5.QtQml ^
	--exclude-module PyQt5.QtQuick ^
	pySagra.py
	

pause

REM Deactivate.bat


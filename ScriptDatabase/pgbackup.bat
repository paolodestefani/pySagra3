REM @ECHO OFF

REM *******************************************************************
REM * Backup di un DB PostgreSQL in formato custom                    *
REM * Per il Restore è necessario aver già riallineato gli utenti     *
REM * sul server di ripristino                                        *
REM *******************************************************************

SET BACKUP_DIR="C:\pySagraBackup"
SET SERVER=localhost
SET PORT=5432
SET DATABASE1=bidasio
SET DATABASE2=nervesa
SET DATABASE3=csc
SET DATABASE4=anpi
SET USER=postgres
SET PGPASSWORD=postgres
SET BACKUPPER="c:\Program Files\PostgreSQL\10\bin\pg_dump.exe"

REM Start
%BACKUPPER% -h %SERVER% -p %PORT% -U %USER% -F c -f %BACKUP_DIR%\%DATABASE1%.backup %DATABASE1%
%BACKUPPER% -h %SERVER% -p %PORT% -U %USER% -F c -f %BACKUP_DIR%\%DATABASE2%.backup %DATABASE2%
%BACKUPPER% -h %SERVER% -p %PORT% -U %USER% -F c -f %BACKUP_DIR%\%DATABASE3%.backup %DATABASE3%
%BACKUPPER% -h %SERVER% -p %PORT% -U %USER% -F c -f %BACKUP_DIR%\%DATABASE4%.backup %DATABASE4%

xcopy /Y %BACKUP_DIR%\*.backup "\\192.168.0.26\pySagraBackup"

REM pause
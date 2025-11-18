@ECHO OFF

REM *******************************************************************
REM * Restore di un DB PostgreSQL da file in formato custom           *
REM * Per il Restore è necessario aver già riallineato gli utenti     *
REM * sul server di ripristino                                        *
REM *******************************************************************

SET BACKUP_DIR="C:\pySagraBackup"
SET SERVER=192.168.0.25
SET PORT=5432
SET DATABASE=bidasio
SET USER=postgres
SET PGPASSWORD=postgres
SET RESTORER="c:\Program Files\PostgreSQL\10\bin\pg_restore.exe"

REM Start
%RESTORER% -h %SERVER% -p %PORT% -U %USER% -d %DATABASE% -c %BACKUP_DIR%\%DATABASE%.backup 
pause
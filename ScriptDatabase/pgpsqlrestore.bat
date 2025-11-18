@ECHO OFF

REM *******************************************************************
REM * Restore di un DB PostgreSQL da file in formato PLAIN            *
REM * Per il Restore è necessario aver già riallineato gli utenti     *
REM * sul server di ripristino                                        *
REM *******************************************************************

SET BACKUPFILE="C:\"
SET SERVER=localhost
SET PORT=5432
SET DATABASE=bidasio
SET PGUSER=postgres
SET PGPASSWORD=postgres
SET PSQL="c:\Program Files\PostgreSQL\9.3\bin\psql.exe"

REM Start
%PSQL% -h %SERVER% -p %PORT% -U %USER% -d %DATABASE% -w %DATABASE% < %BACKUPFILE%
pause
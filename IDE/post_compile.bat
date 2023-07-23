@echo off

SET %A%=%ERRORLEVEL%

:begin
python setup.py build
IF %A% LSS 1 GOTO ERROR
explorer build
exit
:error
cls
echo.
echo *Build Failed*
timeout /t /25
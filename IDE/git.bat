@echo off
:first
cd "C:\Katana Git\cloned\"
for /f "delims=" %%x in (dire.ini) do set url=%%x
git clone %url%
explorer %cd%

	
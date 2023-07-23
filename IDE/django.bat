@echo off
set dir=%1

if "debug\launched.dat" not exist goto first
if "debug\launched.dat" exist goto begin
{
    :first
        cd "%dir%"
        echo launched_prompt=0 > "debug\launched.dat"
        pip install django
        django-admin startproject main .
        python manage.py startapp properties
    :begin
        cd "%dir%"
        django-admin startproject main .
        python manage.py startapp properties
}
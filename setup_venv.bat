:: setup file for creating separate virtual enviroment for Project

@echo off
==============================================

:: check if virtual enviroment exists else create it
if exist venv\Scripts\activate.bat (
    echo virtual enviroment `venv` already exists
) else (
      echo creating virtual enviroment `venv`
      python -m venv venv
      if %errorlevel% neq 0 exit /b %errorlevel%
   )

===============================================
echo activating `venv`
call venv\Scripts\activate.bat
if %errorlevel% neq 0 exit /b %errorlevel%

===============================================
echo Installing required libraries in venv
pip install -r requirements.txt
if %errorlevel% neq 0 exit /b %errorlevel%

echo Succeed in creacting venv 
echo start project using `run` script

================================================
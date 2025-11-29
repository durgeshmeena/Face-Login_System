@echo off
if not exist "data\db" mkdir "data\db"
"C:\Program Files\MongoDB\Server\8.2\bin\mongod.exe" --dbpath="data\db"
pause

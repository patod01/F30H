@echo off
:: Run it from app's root folder.

:: configuracion de entorno virtual
if not exist .venv\Scripts\python.exe (
     echo Installanding Piton...
     python -m venv .venv
     .venv\Scripts\activate.bat
     python -m pip install --upgrade pip
     pip install --no-cache-dir -r settings\req.txt
     deactivate
     echo.
     echo escrit de instalacion terminado!!
     pause>nul
) else (
     title F30H
     echo Arrancando app...
     .venv\Scripts\python.exe app.py
)

:ned

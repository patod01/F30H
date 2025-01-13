@echo off
:: Run it JUST from the app's root folder.

goto :test
:main
python pedales\win\port.py
set /p port=< settings\__prt.txt

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
     start http://localhost:%port%
     .venv\Scripts\python.exe app.py
)

goto :ned

:test
if not exist app.py (
     echo Run this from the same folder `app.py` is in!
     echo Press a key...
     pause>nul
     goto :ned
)
goto :main

:ned

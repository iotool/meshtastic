@echo off

rem Bluetooth ID of your meshtastic-logger
set BLEADDR="XX:XX:XX:XX:XX:XX"

:start
cls
echo %date:~-4%-%date:~3,2%-%date:~0,2% %time:~0,2%:%time:~3,2%:%time:~6,2%

echo "1) export - from meshtastic"
call C:\Users\XXXX\python-3-12-meshtastic\Scripts\activate.bat
set PYTHONIOENCODING=utf-8
set PYTHONLEGACYWINDOWSSTDIO=utf-8
meshtastic --ble-scan
start "custom" /B meshtastic --ble %BLEADDR% --info > meshtastic-thingspeak-info.txt 2>&1
timeout /t 150
taskkill /IM meshtastic.exe /F

echo "2) parse - with python"
python meshtastic-thingspeak-parse.py

echo "3) upload - to thingspeak"
call meshtastic-thingspeak-upload.cmd

echo "4) wait - restart 15 Minuten (inkl. 150 timeout)"
for /L %%a in (750,-5,1) do (
  echo Start in ... %%a Sekunden
  ping -n 5 127.0.0.1 > nul
)
goto start

pause

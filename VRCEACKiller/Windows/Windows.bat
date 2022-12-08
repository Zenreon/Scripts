@echo off
:: Start VRC When init from steam, sleep for EAC init
"%~dp0"launch.exe
ping -n 61 127.0.0.1 > nul
:: Check if VRC is running
tasklist /fi "ImageName eq VRChat.exe" /fo csv 2>NUL | find /I "VRChat.exe">NUL
:: Wait 60sec then kill EAC
if "%ERRORLEVEL%"=="0" (ping -n 6 127.0.0.1 > nul) else (echo VRChat is not running.)
if "%ERRORLEVEL%"=="0" (taskkill /f /im EasyAntiCheat_EOS.exe)

exit

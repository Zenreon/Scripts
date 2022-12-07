@echo off
:: Get Admin
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
:: Get admin End
Set "VRC = VRchat.exe"
echo %VRC%
:: Start VRC When init from steam, sleep for EAC init
START start_protected_game1.exe
ping -n 61 127.0.0.1 > nul
:: Check if VRC is running
tasklist /fi "ImageName eq VRChat.exe" /fo csv 2>NUL | find /I "VRChat.exe">NUL
:: output, then kill EAC if no error (ping used as a quick "sleep" hack)
if "%ERRORLEVEL%"=="0" (ping -n 6 127.0.0.1 > nul) else (echo VRChat is not running.)
if "%ERRORLEVEL%"=="0" (taskkill /f /im EasyAntiCheat_EOS.exe)


PAUSE
exit
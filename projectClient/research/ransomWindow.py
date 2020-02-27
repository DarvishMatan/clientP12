import tkinter as tk


def exb():
    pass


def waitingwindow():
    wa = tk.Tk()
    # this removes the maximize button
    wa.state('zoomed')
    wa.overrideredirect(1)
    wa.title('Defensive-Blocks')
    wa.protocol("WM_DELETE_WINDOW", exb)
    wa.protocol("WM_MINIMIZE_WINDOW", exb)
    x = wa.winfo_screenwidth()
    y = wa.winfo_screenheight()
    wa.geometry("%dx%d" % (x, y))
    lb1 = tk.Label(wa, text="FUCK YOU BITCH\n", font=("Arial Bold", 70), pady=200, fg="RED")
    lb1.pack()
    wa.mainloop()


waitingwindow()
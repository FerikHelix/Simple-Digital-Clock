# Simple digital clock apps made with tkinter
# Author : Ferik Bagas Wardana

import tkinter
from datetime import datetime

def Draw():
    global time_label
    time_now = datetime.now().strftime('%I.%M.%S %p')
    time_label = tkinter.Label(
        text=time_now,
        foreground='white',
        background='black',
        font=('Calibri', 50)
    )
    time_label.pack()

def Update_time():
    global time_label
    time_now = datetime.now().strftime('%I.%M.%S %p')
    time_label.configure(text=time_now)
    tk.after(1000, Update_time)

tk = tkinter.Tk()
tk.title('Simple Digital Clock')
Draw()
Update_time()
tk.mainloop()

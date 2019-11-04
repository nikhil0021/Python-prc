from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime


def clock_time():
    time_cur = datetime.datetime.now()
    time_cur = (time_cur.strftime("%H:%M:%S"))
    text.set(time_cur)
    root.after(1000, clock_time)


root = Tk()
root.title("Digital clock")
root.attributes("-fullscreen", True)
root.configure(background="black")
root.after(1000, clock_time)

fnt = font.Font(family="Amaze", size=120, weight="bold")
text = StringVar()
lbl = ttk.Label(root, textvariable=text, font=fnt, foreground="dark red", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

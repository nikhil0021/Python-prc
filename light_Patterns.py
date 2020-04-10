from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
colour = ["red", "blue", "green", "yellow"]


def pat_1():
    for i in range(36):
        for j in range(4):
            label[i].configure(background=colour[j])
            win_root.update()
            win_root.after(1000)


def pat_2():
    return


def quit_win():
    win_root.destroy()


win_root = Tk()
win_root.title("Light Pattern")

fnt = font.Font(family="Allegro BT", size=20, weight="normal")
lab1 = tk.Label(win_root, text="Welcome to mine show!!", font=fnt)
lab1.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

label = []
for i in range(1, 7):
    for j in range(1, 7):
        L = ttk.Label(win_root, width=5, borderwidth=2, relief="groove")
        L.grid(row=i, column=j - 1, sticky="NSEW")
        label.append(L)

btn_pat1 = Button(win_root, text="First pattern", command=pat_1).grid(row=9, column=0, columnspan=3, sticky="n e s w")
btn_pat2 = Button(win_root, text="Second pattern", command=pat_2).grid(row=9, column=3, columnspan=3, sticky="n e s w")
win_root.mainloop()

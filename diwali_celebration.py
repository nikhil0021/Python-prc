from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
import random


def random_pos(a):
    b = 1
    try:
        while a == 1:
            num = random.randint(1, 36)
            win_root.after(100, img_change(num, b))
            b = num
            win_root.update()
    except RuntimeError:
        pass


def img_change(new, old):
    img1 = tk.PhotoImage(file="bulb_close_1.gif")
    img2 = tk.PhotoImage(file="bulb_open_1.gif")
    label[old-1].configure(image=img1)
    label[old-1].image = img1
    label[new-1].configure(image=img2)
    label[new-1].image = img2


def quit_win():
    win_root.destroy()


win_root = Tk()
win_root.title("Diwali Celebration")

fnt = font.Font(family="Allegro BT", size=20, weight="normal")
lab1 = tk.Label(win_root, text="Enjoy mine randomness!!", font=fnt)
lab1.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

logo = tk.PhotoImage(file="bulb_close_1.gif")
label = []
for i in range(1, 7):
    for j in range(1, 7):
        L = ttk.Label(win_root, image=logo, width=5, borderwidth=2, relief="groove")
        L.grid(row=i, column=j - 1, sticky="NSEW")
        label.append(L)

btn_start = Button(win_root, text="start me", command=lambda: random_pos(1)).grid(row=9, column=0, columnspan=3
                                                                                  , sticky="n e s w")
btn_stop = Button(win_root, text="Stop!!", command=quit_win).grid(row=9, column=3, columnspan=3, sticky="n e s w")
win_root.mainloop()

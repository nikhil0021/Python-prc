from tkinter import *
from tkinter import ttk
from tkinter import font


def rem_vow():
    new_str = ""
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    sentence = string.get()
    for letter in sentence:
        if letter not in vowels:
            new_str += letter
    txt.set(new_str)


win_root = Tk()
win_root.title("Vowel Remover")
fnt = font.Font(family="Amaze", size=20, weight="bold")
lab_inp = ttk.Label(win_root, text="Enter your String to remove vowels", font=fnt)
lab_inp.grid(row=0, column=0, columnspan=3)
string = Entry(win_root, width=45, borderwidth=5)
string.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
magic = Button(win_root, text="Click me!!", command=rem_vow)
magic.grid(row=2, column=1)
txt = StringVar()
lab_op = ttk.Label(win_root, textvariable=txt, font="cambria")
lab_op.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
win_root.mainloop()

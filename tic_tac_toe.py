from tkinter import *
from tkinter import ttk
import tkinter.font as font
import os
import sys
import tkinter.messagebox
a = 0


def click(n):
    global a
    if a % 2 == 0:
        chance = "X"
    else:
        chance = "O"
    button_lis[n-1].configure(state=DISABLED, text=chance, relief=SUNKEN)
    a += 1
    check_res(a)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def check_res(a):
    if (button_lis[0]['text'] == 'X' and button_lis[1]['text'] == 'X' and button_lis[2]['text'] == 'X' or
            button_lis[3]['text'] == 'X' and button_lis[4]['text'] == 'X' and button_lis[5]['text'] == 'X' or
            button_lis[6]['text'] == 'X' and button_lis[7]['text'] == 'X' and button_lis[8]['text'] == 'X' or
            button_lis[0]['text'] == 'X' and button_lis[4]['text'] == 'X' and button_lis[8]['text'] == 'X' or
            button_lis[2]['text'] == 'X' and button_lis[4]['text'] == 'X' and button_lis[6]['text'] == 'X' or
            button_lis[0]['text'] == 'X' and button_lis[1]['text'] == 'X' and button_lis[2]['text'] == 'X' or
            button_lis[0]['text'] == 'X' and button_lis[3]['text'] == 'X' and button_lis[6]['text'] == 'X' or
            button_lis[1]['text'] == 'X' and button_lis[4]['text'] == 'X' and button_lis[7]['text'] == 'X' or
            button_lis[6]['text'] == 'X' and button_lis[5]['text'] == 'X' and button_lis[8]['text'] == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player A Won the match")
        if tkinter.messagebox.askretrycancel("Congratulations Player A", "Do you wanna Play again!!"):
            restart_program()
            # os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        else:
            win_root.destroy()

    elif (button_lis[0]['text'] == 'O' and button_lis[1]['text'] == 'O' and button_lis[2]['text'] == 'O' or
            button_lis[3]['text'] == 'O' and button_lis[4]['text'] == 'O' and button_lis[5]['text'] == 'O' or
            button_lis[6]['text'] == 'O' and button_lis[7]['text'] == 'O' and button_lis[8]['text'] == 'O' or
            button_lis[0]['text'] == 'O' and button_lis[4]['text'] == 'O' and button_lis[8]['text'] == 'O' or
            button_lis[2]['text'] == 'O' and button_lis[4]['text'] == 'O' and button_lis[6]['text'] == 'O' or
            button_lis[0]['text'] == 'O' and button_lis[1]['text'] == 'O' and button_lis[2]['text'] == 'O' or
            button_lis[0]['text'] == 'O' and button_lis[3]['text'] == 'O' and button_lis[6]['text'] == 'O' or
            button_lis[1]['text'] == 'O' and button_lis[4]['text'] == 'O' and button_lis[7]['text'] == 'O' or
            button_lis[6]['text'] == 'O' and button_lis[5]['text'] == 'O' and button_lis[8]['text'] == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player B won the match")
        if tkinter.messagebox.askretrycancel("Congratulations Player B", "Do you wanna Play again!!"):
            restart_program()
            # os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        else:
            win_root.destroy()

    elif a == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        if tkinter.messagebox.askretrycancel("Oopss!!!", "Do you wanna Play again!!"):
            restart_program()
            # os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        else:
            win_root.destroy()


win_root = Tk()
win_root.title("Tic Tac Toe")
fnt = font.Font(family="Times new roman", size=20, weight="bold")
lab_0 = ttk.Label(win_root, text="Player 1: X", font=fnt).grid(row=0, column=0, columnspan=3)
lab_1 = ttk.Label(win_root, text="Player 2: O", font=fnt).grid(row=1, column=0, columnspan=3)

button_lis = []
count = 1
for i in range(3):
    for j in range(3):
        btn = Button(win_root, height=3, width=5, command=lambda c=count: click(c))
        btn['font'] = fnt
        btn.grid(row=i+2, column=j)
        button_lis.append(btn)
        count += 1

win_root.mainloop()

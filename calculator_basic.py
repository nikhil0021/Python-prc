from tkinter import *

win_root = Tk()
win_root.title("My first calculator")

inp = Entry(win_root, width=45, borderwidth=5)
inp.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def show(number):
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, str(current) + str(number))


def add():
    num = inp.get()
    global f_num
    global sign
    sign = "add"
    f_num = int(num)
    inp.delete(0, END)


def sub():
    num = inp.get()
    global f_num
    global sign
    sign = "sub"
    f_num = int(num)
    inp.delete(0, END)


def mul():
    num = inp.get()
    global f_num
    global sign
    sign = "mul"
    f_num = int(num)
    inp.delete(0, END)


def div():
    num = inp.get()
    global f_num
    global sign
    sign = "div"
    f_num = int(num)
    inp.delete(0, END)


def eq():
    s_num = inp.get()
    inp.delete(0, END)
    if sign == "add":
        inp.insert(0, f_num + int(s_num))
    if sign == "sub":
        inp.insert(0, f_num - int(s_num))
    if sign == "div":
        inp.insert(0, f_num / int(s_num))
    if sign == "mul":
        inp.insert(0, f_num * int(s_num))


def clear():
    inp.delete(0, END)


but_1 = Button(win_root, padx=40, pady=20, text="1", command=lambda: show(1))
but_2 = Button(win_root, padx=40, pady=20, text="2", command=lambda: show(2))
but_3 = Button(win_root, padx=40, pady=20, text="3", command=lambda: show(3))
but_4 = Button(win_root, padx=40, pady=20, text="4", command=lambda: show(4))
but_5 = Button(win_root, padx=40, pady=20, text="5", command=lambda: show(5))
but_6 = Button(win_root, padx=40, pady=20, text="6", command=lambda: show(6))
but_7 = Button(win_root, padx=40, pady=20, text="7", command=lambda: show(7))
but_8 = Button(win_root, padx=40, pady=20, text="8", command=lambda: show(8))
but_9 = Button(win_root, padx=40, pady=20, text="9", command=lambda: show(9))
but_0 = Button(win_root, padx=40, pady=20, text="0", command=lambda: show(0))
but_add = Button(win_root, padx=39, pady=20, text="+", command=add)
but_sub = Button(win_root, padx=40, pady=20, text="-", command=sub)
but_div = Button(win_root, padx=40, pady=20, text="/", command=div)
but_mul = Button(win_root, padx=40, pady=20, text="*", command=mul)
but_equal = Button(win_root, padx=90, pady=20, text="=", command=eq)
but_clear = Button(win_root, padx=80, pady=20, text="clear", command=clear)


but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)

but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)

but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)

but_0.grid(row=4, column=0)
but_add.grid(row=5, column=0)
but_sub.grid(row=6, column=0)
but_div.grid(row=6, column=1)
but_mul.grid(row=6, column=2)
but_equal.grid(row=4, column=1, columnspan=2)
but_clear.grid(row=5, column=1, columnspan=2)


win_root.mainloop()

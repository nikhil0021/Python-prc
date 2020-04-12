from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import random

global res
file = open("TypingSpeedQues.txt", "r")
quesarr = file.read().split(";")


def randomstr():
    a = random.randint(0, len(quesarr))
    quesstr = quesarr[a]
    return quesstr


def starttest():
    arrques = randomstr()
    lab_ques.configure(text=arrques)
    lab_ques.update()
    global starttime
    starttime = currtime()
    return True


def currtime():
    time_cur = time.time()
    return time_cur


def stoptest():
    global stoptime
    stoptime = currtime()
    result()
    return True


def correctword():
    mainword = lab_ques.cget("text")
    answer = usr_inp.get()
    lab_ques.configure(text="Test finished")
    wordlength = len(answer)
    count = 0
    if wordlength > len(mainword):
        rang = len(mainword)
    else:
        rang = wordlength
    for i in range(rang):
        if mainword[i] == answer[i]:
            count = count + 1
    return wordlength, count


def result():
    timediff = stoptime - starttime
    correctwrd = list(correctword())
    usr_inp.delete(0, "end")
    res = "Your speed is {0} character/second and you're {1}% accurate.".format(round((correctwrd[1] / timediff), 2),
                                                                                round((correctwrd[1] / correctwrd[0]) * 100,2))
    res_lab.configure(text=res)
    res_lab.update()
    return True


root = Tk()
root.title("Typing Speed Master")
fnt = font.Font(family="Times new roman", size=20, weight="bold")
lab_0 = ttk.Label(root, text="Typing Master", font=fnt)
lab_0.grid(row=0, column=0, columnspan=6)
ques = "Press Start Button to start Test!!!"
lab_ques = ttk.Label(root, text=ques)
lab_ques.grid(row=1, column=0, columnspan=6)
usr_inp = Entry(root, width=50, borderwidth=5)
usr_inp.grid(row=4, column=0, columnspan=6)
Start_btn = ttk.Button(root, text="Start Test", command=starttest).grid(row=6, column=0, columnspan=3)
Stop_btn = ttk.Button(root, text="Stop Test", command=stoptest).grid(row=6, column=4, columnspan=3)
res_lab = ttk.Label(root, text=" ")
res_lab.grid(row=8, column=0, columnspan=6)
root.mainloop()

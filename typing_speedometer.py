from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import random

global res

arr = ['''"Do not go where the path may lead, go instead where there is no path and leave a trail." -Ralph Waldo 
Emerson''', '''"Your time is limited, so don't waste it living someone else's life. Don't be trapped by 
dogma – which is living with the results of other people's thinking." -Steve Jobs''',
       '''"The greatest glory in living lies not in never falling, but in rising every time we fall." -Nelson Mandela
''', '''"The way to get started is to quit talking and begin doing." -Walt Disney''', '''"If life were predictable it 
would cease to be life, and be without flavor." -Eleanor Roosevelt''', '''"If you look at what you have in life, 
you'll always have more. If you look at what you don't have in life, you'll never have enough." -Oprah Winfrey''',
       '''"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success." 
       -James Cameron''', '''"Life is what happens when you're busy making other plans." -John Lennon''', '''"The 
       best and most beautiful things in the world cannot be seen or even touched - they must be felt with the 
       heart." -Helen Keller''', '''"You have brains in your head. You have feet in your shoes. You can steer 
       yourself any direction you choose." -Dr. Seuss''']


def randomstr():
    a = random.randint(0, 9)
    quesstr = arr[a]
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
    print("mainword:", mainword)
    print("answer:", answer)
    wordlength = len(answer)
    count = 0
    for i in range(wordlength):
        if mainword[i] == answer[i]:
            count = count + 1
    return wordlength, count


def result():
    timediff = stoptime - starttime
    correctwrd = list(correctword())
    usr_inp.delete(0, "end")
    print("timediff:", timediff)
    print("correctwrd1", correctwrd[0])
    print("correctwrd2", correctwrd[1])
    res = "Your speed is {0} character/second and you're {1}% accurate.".format((correctwrd[1] // timediff),
                                                                                (correctwrd[1] // correctwrd[0]) * 100)
    res_lab.configure(text=res)
    res_lab.update()
    return True


root = Tk()
root.title("Typing Speed Master")
root.configure(background="black")
fnt = font.Font(family="Times new roman", size=20, weight="bold")
lab_0 = ttk.Label(root, text="Typing Master", font=fnt)
lab_0.grid(row=0, column=0, columnspan=5)
ques = "Press Start Button to start Test!!!"
lab_ques = ttk.Label(root, text=ques)
lab_ques.grid(row=1, column=0, columnspan=6)
usr_inp = Entry(root, width=45, borderwidth=5)
usr_inp.grid(row=4, column=0, columnspan=6)
Start_btn = ttk.Button(root, text="Start Test", command=starttest).grid(row=6, column=0, columnspan=3)
Stop_btn = ttk.Button(root, text="Stop Test", command=stoptest).grid(row=6, column=4, columnspan=3)
res_lab = ttk.Label(root, text=" ")
res_lab.grid(row=8, column=0, columnspan=6)
root.mainloop()

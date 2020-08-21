from tkinter import *
import random


def add_button():
    if int(num.get()) % 4 == 3:
        Button(root, text='hello' + str(num.get()), bg='red', command=lambda: add_button()).pack(side=LEFT)
    elif int(num.get()) % 4 == 2:
        Button(root, text='hello' + str(num.get()), bg='red', command=lambda: add_button()).pack(side=RIGHT)
    elif int(num.get()) % 4 == 1:
        Button(root, text='hello' + str(num.get()), bg='red', command=lambda: add_button()).pack(side=TOP)
    else:
        Button(root, text='hello' + str(num.get()), bg='red', command=lambda: add_button()).pack(side=BOTTOM)
    num.set(int(num.get())+1)


root = Tk()

# root.maxsize(width=400, height=400)

num = StringVar(master=root, name='num', value='0')

Button(root, text='hello', bg='red', command=lambda: add_button()).pack(side=LEFT)

root.mainloop()


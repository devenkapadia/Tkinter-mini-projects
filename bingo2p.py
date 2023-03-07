from tkinter import *
import random
import tkinter.messagebox as tmsg
import time
from Bingo_SinglePlayer import *

def click(t,b):
    b['text'] = "Apply"
    t.destroy()
    t.update()
    t.mainloop()


root = Tk()
b = Button(root,text="Submit", command=lambda : click(root,b))
b.pack()
root.mainloop()
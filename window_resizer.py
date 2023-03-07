from tkinter import *

root = Tk()
root.geometry("250x100")

def resize(event):
    root.geometry(f"{widthVal.get()}x{heightVal.get()}")


Label(root, text="Windows Resizer", font="comicsansms 13 bold").grid(row=1,column=2)

#Text for our form
width = Label(root, text="Width").grid(row=2,column=1)
height = Label(root, text="Height").grid(row=3,column=1)

widthVal= StringVar()
heightVal= StringVar()

widthEntry = Entry(root,textvariable=widthVal).grid(row=2,column=2)
heightEntry = Entry(root,textvariable=heightVal).grid(row=3,column=2)

btn = Button(root,text="Apply")
btn.grid(row=4,column=2)
btn.bind('<Button-1>', resize)
root.mainloop()


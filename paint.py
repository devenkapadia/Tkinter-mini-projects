from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter as tk
from PIL import ImageTk, Image

root = Tk()
root.title("Paint- by Deven")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False,False)

current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=True)
    current_x,current_y = work.x,work.y

def addRect(work):
    global current_x,current_y
    canvas.create_rectangle((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color)
    current_x,current_y = work.x,work.y

def show_color(new_color):
    global color
    color=new_color

def new_canvas():
    canvas.delete('all')
    pallete()


# logo
logo = PhotoImage(file="paint.png")
root.iconphoto(False,logo)

c_box = PhotoImage(file="color section.png")
Label(root,image=c_box,bg="#f2f3f5").place(x=10,y=20)

image = Image.open('erasor.png')
image = image.resize((35,35),Image.ANTIALIAS)
eraser = ImageTk.PhotoImage(image)
erbtn = Button(root, image=eraser,height=30,width=30, bg="#ffffff")
erbtn.bind('<Button-1>',lambda x: show_color('white'))
erbtn.place(x=30,y=400)
btn = Button(root, text="clear",height=2,width=4, bg="#ffffff",command=new_canvas)
btn.place(x=30,y=440)

colors = Canvas(root,bg="#ffffff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

def pallete():

    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))
    id = colors.create_rectangle((10,40,30,60),fill="grey")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('grey'))
    id = colors.create_rectangle((10,70,30,90),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))
    id = colors.create_rectangle((10,100,30,120),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))
    id = colors.create_rectangle((10,130,30,150),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))
    id = colors.create_rectangle((10,160,30,180),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))
    id = colors.create_rectangle((10,190,30,210),fill="pink")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('pink'))
    id = colors.create_rectangle((10,220,30,240),fill="orange")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))
    id = colors.create_rectangle((10,250,30,270),fill="purple")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))

pallete()

canvas = Canvas(root, width=930,height=500,bg="white",cursor="hand2")
canvas.place(x=100,y=10)
canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>',addLine)

current_val = tk.DoubleVar()
def get_current_value():
    return '{:f}'.format(current_val.get())

def slider_change(event):
    value_label.config(text=get_current_value())

slider = Scale(root,from_=0,to=100,orient='horizontal',command=slider_change,variable=current_val, tickinterval=20)
slider.set(10)
slider.place(x=27,y=530)


value_label = Label(root,text=get_current_value())
# value_label.place(x=27,y=550)


root.mainloop()
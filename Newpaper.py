from tkinter import *
from PIL import Image, ImageTk
root = Tk()


# widthxheight
root.geometry("1300x750")
root.minsize(1300,750)
root.maxsize(1300,750)
root.title("The times of India")

frame0 = Frame(root)
frame0.pack(side="top",fill=X,padx=8,pady=8)
label=Label(frame0,text="Date : 16-06-2022, Day : Thursday\nVisit: www.timesofindia.com",font="comicsansms 13",fg="dark grey",bg="grey",borderwidth=5,relief=RIDGE)
label.pack(side=BOTTOM,fill=X)
label0=Label(frame0,text="The Times of India",font="comicsansms 20",bg="grey",fg="black",borderwidth=5,relief=RIDGE)
label0.pack(side=TOP,fill=X)


frame1=Frame(root)
frame1.pack(side=TOP,fill=X)
label1=Label(frame1,text="Cricket News: Headlines",font="comicsansms 15 bold",borderwidth=5,relief=SUNKEN,bg="light blue")
label1.pack(side=TOP,fill=X,padx=8,pady=8)


frame2=Frame(root)
frame2.pack(anchor="nw")
img1 = Image.open("news1.jpg")
photo1 = ImageTk.PhotoImage(img1)
img1 = Label(frame2,image=photo1,borderwidth=5,relief=GROOVE)
img1.pack(side=LEFT,padx=15,pady=10)

image1=Label(frame2,borderwidth=5,relief=GROOVE)
image1.pack(anchor="nw",side=LEFT,padx=15,pady=10)
label2=Label(frame2,text="I have to keep developing my skills : Harshal Patel\n\nHarshal Patel only came into the bowl the 13th over, till then Chennai Super Kings had\n a good start and Devon Conway was going pretty well from one end. But as soon as Patel came into the bowl\n he ensured that the batter at the other end doesn’t get free deliveries to hit boundaries.",font="comicsansms 15",bg="yellow",borderwidth=5,relief=GROOVE)
label2.pack(anchor="ne",side=LEFT,padx=15,pady=10)

frame3=Frame(root)
frame3.pack(anchor="ne",side=TOP)
img2 = Image.open("new3.jpg")
photo2 = ImageTk.PhotoImage(img2)
img2 = Label(frame3,image=photo2,borderwidth=5,relief=GROOVE)
img2.pack(side=RIGHT,padx=15,pady=10)
#
# photo2=PhotoImage(file="news2.jpg")
# image2=Label(frame3,image=photo2,borderwidth=5,relief=GROOVE)
# image2=Label(frame3,borderwidth=5,relief=GROOVE)
# image2.pack(side=RIGHT,padx=15,pady=10)
# label0=Label(frame3,text="Rahul Tripathi gets his maidem team call",font="comicsansms 15",bg="grey",fg="black",borderwidth=5,relief=RIDGE)
# label0.pack(side=TOP,fill=X)
label3=Label(frame3,text="Rahul Tripathi gets his maidem team call\n\nThe squad, that features a maiden call-up for Rahul Tripathi and a return for Sanju Samson,\n is conspicuous by the absence of India's Test team regulars who'll directly fly to England\n to prepare for the rescheduled fifth Test at Edgbaston.",font="comicsansms 15",bg="orange",borderwidth=5,relief=GROOVE)
label3.pack(side=LEFT)

frame4=Frame(root)
frame4.pack(anchor="nw",side=TOP)
img3 = Image.open("news2.jpg")
photo3 = ImageTk.PhotoImage(img3)
img3 = Label(frame4,image=photo3,borderwidth=5,relief=GROOVE)
img3.pack(side=LEFT,padx=15,pady=10)
# photo3=PhotoImage(file="comp.png")
# image3=Label(frame4,image=photo3,borderwidth=5,relief=GROOVE)
image3=Label(frame4,borderwidth=5,relief=GROOVE)
image3.pack(side=LEFT,padx=15,pady=10)
# label0=Label(frame4,text="India's must win match: IND vs SA 4th T20i",font="comicsansms 15",bg="grey",fg="black",borderwidth=5,relief=RIDGE)
# label0.pack(side=TOP,fill=X)
label4=Label(frame4,text="India's must win match: IND vs SA 4th T20i\n\nIndia will once again play a do-or-die clash in Rajkot after winning the 3rd T20\n on Tuesday.With the series still in South Africa’s favour at 2-1, Rishabh Pant will bank on a flat surface at Rajkot\n to level the series.",font="comicsansms 15",bg="green",borderwidth=5,relief=GROOVE)
label4.pack(side=RIGHT,padx=15,pady=10)

root.mainloop()
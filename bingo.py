from tkinter import *
import random
import tkinter.messagebox as tmsg
import time
from Bingo_SinglePlayer import *


u = [[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# sbar = Label()
u_score = 0
c_score = 0
buttonList = []
c = createMat()

def playGame():
    game = Tk()
    game.eval("tk::PlaceWindow . center")
    game.title("Bingo")
    game.iconbitmap('bingo.ico')
    # game.geometry("500x400+450+300")
    f1 = Frame(game,bg="grey",pady=10)
    lbl1 = Label(f1,text="Instructions :",bg="light blue",font="Helvetica 20 bold",pady=5)
    lbl1.pack()
    str = "1. Enter number in the range of 1-25\n2. When you enter number that number will be removed from all player's matrix\n3. When all numbers of your matrix's row, column or diagonal is 0 you will get a point\n4. When you get 5 points you will win"
    rules = Label(f1,text=str,bg="pink",font="TimesNewRoman 15",justify="left")
    rules.pack(pady=8,padx=14)

    Label(f1,text="Click here to start the game : ",font="Helvetica 18 bold",bg="blue",fg="white").pack(pady=10, padx=22)
    btn = Button(f1, bg="light green", font=("Helvetica", 15), text="Generate my board",
                 command=lambda: randomBoard(game))
    btn.pack()
    f1.pack()
    game.mainloop()

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
def hiddenWork(no):
    time.sleep(2)
    global num
    num.remove(no)
    x = random.choice(num)
    num.remove(x)
    remove(x, c)
    remove(x, u)
    crossNum(x)
    print("\n")
    print(np.array(u))
    print("\n")
    print(np.array(c))
    # global c
    # n=0
    # for i in range(len(c)):
    #     for j in range(len(c)):
    #         if (c[i][j] != 0):
    #             n = c[i][j]
    #             c[i][j]=0
    #             remove(n,c)
    #             remove(n,u)
    #             break
    #         elif (c[j][i] != 0):
    #             n = c[j][i]
    #             c[j][i] = 0
    #             remove(n, c)
    #             remove(n, u)
    #             break
    #         else:
    #             n = c[i][i]
    #             c[i][i]=0
    #             remove(n, c)
    #             remove(n, u)
    #             break
    #     crossNum(n)
    #     break

def crossNum(n):
    # time.sleep(2)
    for i in range(len(buttonList)):
        if buttonList[i]["text"] == n:
            buttonList[i]["text"] = "X"
            buttonList[i].config(bg="grey")

def b_click(t,b):
    n = b["text"]
    global c
    if n != "X":
        b["text"] = "X"
        b.config(bg="grey")
        t.update()
        remove(n, u)
        remove(n, c)
        hiddenWork(n)
    else:
        tmsg.showinfo("Bingo", "This number is already crossed")

    global c_score
    global u_score
    c_score = scrCal(c)
    print(c_score)
    u_score = scrCal(u)
    print(u_score)
    if (u_score > 0 or c_score > 0):
        Bingo(u_score)
        Bingo(c_score)

    if(u_score>=5 or c_score>=5):
        ending(t)


def ending(t):
    t.destroy()
    end = Tk()
    end.eval("tk::PlaceWindow . center")
    # end.geometry("300x200"
    f1 = Frame(end, bg="grey")

    if (u_score >= 5 and c_score < 5):
        print("You won")
        Label(f1, text="Congratulations!!! You won", font="Helvetica 15", pady=10, padx=10, bg="light green").pack(
            pady=10)

    if (c_score >= 5 and u_score < 5):
        print("Pc won")
        Label(f1, text="Ooohh ohhh sorryy You lost!! PC won", font="Helvetica 15", pady=10, padx=10, bg="Red").pack(
            pady=10)
        Label(f1, text="You can still try again", font="Helvetica 15", pady=10, padx=10, bg="light grey").pack(pady=10)

    if (c_score >= 5 and u_score >= 5):
            print("Draw")
            Label(f1, text="Its a tie!! Both played very well", font="Helvetica 15", pady=10, padx=10, bg="Pink").pack(
                pady=10)
            Label(f1, text="You can still try again", font="Helvetica 15", pady=10, padx=10, bg="light grey").pack(pady=10)

    end.title("Good game")
    Label(f1, text="Do you wanna play agian: ", font="Helvetica 15").pack(pady=18, padx=22)
    btn = Button(f1, bg="light grey", font=("Helvetica", 12), text="Yes, lets play",
                 command=lambda : randomBoard(end))
    btn.pack()
    btn2 = Button(f1, bg="light grey", font=("Helvetica", 12), text="No no i am tired",
                  command=exit)

    btn2.pack(pady=15)
    f1.pack(fill=BOTH)
    end.mainloop()

def randomBoard(tk):
    tk.destroy()
    root = Tk()
    root.eval("tk::PlaceWindow . center")
    root.title('Bingo- by Deven')
    root.iconbitmap('bingo.ico')
    # root.geometry("529x600")
    hgt = 2
    wdt = 4
    color = "light blue"

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b1))

    b2 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b2))

    b3 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b4))

    b5 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b5))

    b6 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b7))

    b8 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b8))

    b9 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                command=lambda: b_click(root, b9))

    b10 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b10))

    b11 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b11))

    b12 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b12))

    b13 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b13))

    b14 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b14))

    b15 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b15))

    b16 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b16))

    b17 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b17))

    b18 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b18))

    b19 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b19))

    b20 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b20))

    b21 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b21))

    b22 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b22))

    b23 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b23))

    b24 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b24))

    b25 = Button(root, text=" ", font=("Helvetica", 20), height=hgt, width=wdt, bg=color,
                 command=lambda: b_click(root, b25))

    random.shuffle(l)
    global buttonList
    buttonList = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]
    for i in range(25):
        buttonList[i]["text"]=l[i]

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)
    b5.grid(row=0, column=4)

    b6.grid(row=1, column=0)
    b7.grid(row=1, column=1)
    b8.grid(row=1, column=2)
    b9.grid(row=1, column=3)
    b10.grid(row=1, column=4)

    b11.grid(row=2, column=0)
    b12.grid(row=2, column=1)
    b13.grid(row=2, column=2)
    b14.grid(row=2, column=3)
    b15.grid(row=2, column=4)

    b16.grid(row=3, column=0)
    b17.grid(row=3, column=1)
    b18.grid(row=3, column=2)
    b19.grid(row=3, column=3)
    b20.grid(row=3, column=4)

    b21.grid(row=4, column=0)
    b22.grid(row=4, column=1)
    b23.grid(row=4, column=2)
    b24.grid(row=4, column=3)
    b25.grid(row=4, column=4)

    global u
    k=0
    for i in range(len(u)):
        for j in range(len(u)):
            u[i][j] = l[k]
            k = k+1
    print(np.array(u))

playGame()
from Bingo_SinglePlayer import *
import numpy as np
import os
import time

class game:
    score = 0
    mat = []
    name = "name"
    def __init__(self,n):
        score = 0
        self.score = score
        mat = createMat()
        self.mat = mat 
        mat = np.array(mat)
        name = input(f"Enter name of player {n}: ").capitalize()
        self.name = name
        print(f"{name}'s matrix is\n {mat}")

print("Instructions :\n1. Enter number in the range of 1-25\n2. When you enter number that number will be removed from all player's matrix\n3. When all numbers of your matrix's row, column or diagonal is 0 you will get a point")
print("4. When you get 5 points you will win\n\n")

while(True):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    time.sleep(2)
    os.system("cls")
    print("Do you wanna play with Computer or with friends ?\nEnter 1 to play with Computer\nEnter 2 to play with friends\nEnter 3 to exit")
    try:
        while(True):
            mode = int(input("Enter game mode: ") )
            if(mode!=1 and mode!=2 and mode!=3):
                print("Enter valid game mode")
            else:
                break
    except:
        print("Enter valid interger") 
        continue
    if mode==1:
        main()
    elif mode==3:
        break
    else:
        os.system("cls")
        print("Starting a Multiplayer Game!!")
        play('start.wav')
        while(True):
            try:
                n_p = int(input("Enter no. of players :: "))
                os.system("cls")
                break
            except:
                print("Enter valid integer")
                continue
        players = []
        for i in range(n_p):
            p = game(i+1)
            time.sleep(1)
            players.append(p)
            os.system("cls")
        k=0
        i=0
        while(True):
            while (k == 0):
                while(True):
                    try:
                        print(np.array(players[i].mat))
                        # print(players[i].score)
                        print(f"\n{players[i].name}:", end=" ")
                        Bingo(players[i].score)
                        num = int(input(f"{players[i].name} Enter number: "))
                        if (str(num).lower()=='e'):
                            exit()
                        if num in nums:
                            nums.remove(num)
                            break
                        else:
                            if (num <= 25):
                                print("\nNumber is already enterd by you or Friend")
                            else:
                                print("\nEnter valid number")
                        continue
                    except:
                        print("Enter valid integer")
                        continue

                for j in range(n_p):
                    remove(num, players[j].mat)
                    playPop(players[j].name,num)
                    players[j].score = scrCal(players[j].mat)
                    # print(np.array(players[j].mat))
                    # time.sleep(2)
                    if players[j].score >= 5:
                        print(f"{players[j].name} won!!!!!")
                        k = k + 1
                        play('clap.wav')

                time.sleep(1)

                os.system("cls")
                i = i + 1
                if (i == n_p):
                    i = 0  

            print("\n")
            print("Do you wanna play again ?\nEnter 'Yes' to play again with computer and 'No' for main menu")
            while (True):
                end = input().lower()
                if end in ["yes", "no"]:
                    break
                else:
                    print("Please enter 'Yes' if you wanna play again\nOr 'No' if you wanna exit the game")
                    continue
            if end == "yes":
                os.system("cls")
                continue
            elif end == "no":
                os.system("cls")
                break




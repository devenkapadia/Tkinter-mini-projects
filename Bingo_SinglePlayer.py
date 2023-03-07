import random
import time
import os
import numpy as np
# from PlayingAudio import play

# Creatig a matrix
def createMat():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    list = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    # list = np.zeros((5,5))
    # list = np.empty((5,5))
    for i in range(len(list)):
        for j in range(len(list)):
            list[i][j] = b = random.choice(num)
            num.remove(b)
    return list

# Removing element from the list
def remove(n, list):
    j = 0
    while (j < 5):
        a = list[j]
        i = 0
        while (i < 5):
            if a[i] == n:
                a[i] = a[i] - int(a[i])
            i = i + 1
        j = j + 1


# checking the matrix
def scrCal(list):
    c1 = 0
    c2 = 0
    c3 = 0
    score = 0
    # row score
    l0 = [0, 0, 0, 0, 0]
    for item in list:
        if item == l0:
            score = score + 1
    # print(score)
    i = 0
    while(i < 5):
        j = 0
        c1 = 0
        while(j < 5):
            # column
            if(list[j][i] == 0):
                c1 = c1+1
            # diagonal
            if(list[i][j] == 0 and i == j):
                c2 = c2+1
            if(list[i][j] == 0 and i+j == 4):
                c3 = c3+1
            j = j+1
        if(c1 == 5):
            score = score + 1
        i = i+1
    # print(c2)

    if(c2 == 5):
        score = score + 1
    if(c3 == 5):
        score = score + 1
    # print(score)
    return score


def Bingo(scr):
    if(scr == 1):
        return "B"
    if(scr == 2):
        return "BI"
    if(scr == 3):
        return "BIN"
    if(scr == 4):
        return "BING"
    if(scr == 5):
        return "BINGO"

    # print(scr)
    if(scr != 5):
        scr = 0


def playPop(name, num):
    print(f"Removing {num} from {name}'s matrix")
    # play('pop.wav')


# if __name__ == '__main__':
# print("Instructions :\n1. Enetr number in the range of 1-25\n2. When you enter number that number will be removed from all player's matrix\n3. When all numbers of your matrix's row, column or diagonal is 0 you will get a point")
# print("4. When you get 5 points you will win\n\n")
# time.sleep(5)

def main():
    # print("Do you wanna play with Computer or with friend ?\nEnter 1 to play with Computer\nEnter 2 to play with Friend")
    # while (True):
    #     ply = int(input())
    #     if ply in [1, 2]:
    #         break
    #     else:
    #         print("Please select proper game mode")
    #         continue
    # if ply == 1:
    print("Starting game with computer")
    # play('start.wav')
    player_1 = str(input("Enter your Name: ")).capitalize()
    player_2 = "Computer"
    # elif ply == 2:
    # print("Strting game with friend")
    #     player_1 = str(input("Enter 1st player's name: ")).capitalize()
    #     player_2 = str(input("Enter 2nd player's name: ")).capitalize()
    b1 = createMat()
    b2 = createMat()
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    i = 0

    # Game starts
    while(True):
        while (True):
            os.system("cls")
            # print(*b2,sep= "\n")
            if i % 2 == 0:
                while (True):
                    try:
                        a = np.array(b1)
                        print(a)
                        x = int(input(f"{player_1} enter number: "))
                        if x in num:
                            break
                        else:
                            if(x <= 25):
                                print("\nNumber is already enterd by you or computer")
                            else:
                                print("\nEnter valid number")
                    except:
                        print("Enter valid integer\n")
                        continue
                num.remove(x)
            else:
                # if ply == 1:
                print("Computer is entering number")
                time.sleep(2)
                x = random.choice(num)
                num.remove(x)
                # elif ply == 2:
                #     a = np.array(b2)
                #     print(a)
                #     print("\n")
                #     while (True):
                #         x = int(input(f"\n{player_2} enter number: "))
                #         if x in num:
                #             break
                #         else:
                #             if(x <= 25):
                #                 print("\nNumber is already enterd by you or Friend")
                #             else:
                #                 print("\nEnter valid number")
                #     num.remove(x)
            i = i + 1
            remove(x, b1)
            playPop(player_1, x)
            remove(x, b2)
            playPop(player_2, x)
            score_1 = scrCal(b1)
            score_2 = scrCal(b2)
            # time.sleep(2)
            if(score_1 > 0 or score_2 > 0):
                print(f"\n{player_1}:", end=" ")
                Bingo(score_1)
                print(f"{player_2}:", end=" ")
                Bingo(score_2)
                time.sleep(2)

            if (score_1 >= 5 and score_2 < 5):
                print(f"{player_1} wins!!")
                # play('clap.wav')
                print(f"Better luck next time {player_2}")
                break
            if (score_2 >= 5 and score_1 < 5):
                print(f"{player_2} wins!!")
                # play('clap.wav')
                print(f"Better luck next time {player_1}")
                break
            else:
                time.sleep(0.5)
                continue

        time.sleep(2)
        print("\n")
        print("Do you wanna play again ?\nEnter 'Yes' to play again with computer and 'No' for main menu")
        while(True):
            end = input().lower()
            if end in ["yes", "no"]:
                break
            else:
                print(
                    "Please enter 'Yes' if you wanna play again\nOr 'No' for main menu")
                continue
        if end == "yes":
            os.system("cls")
            continue
        elif end == "no":
            os.system("cls")
            break

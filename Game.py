from tkinter import Label,Button,Tk
from tkinter.messagebox import showinfo,askokcancel
from itertools import permutations
import os
import sys

y=""
x=2

player1 = []
player2 = []

def restartgame():
    global player1,player2,x
    
    b1.config(command= lambda : operate(b1, 1), text=".")
    b2.config(command= lambda : operate(b2, 2), text=".")
    b3.config(command= lambda : operate(b3, 3), text=".")
    b4.config(command= lambda : operate(b4, 4), text=".")
    b5.config(command= lambda : operate(b5, 5), text=".")
    b6.config(command= lambda : operate(b6, 6), text=".")
    b7.config(command= lambda : operate(b7, 7), text=".")
    b8.config(command= lambda : operate(b8, 8), text=".")
    b9.config(command= lambda : operate(b9, 9), text=".")
    
    player1 = []
    player2 = []
    x = 2
    
    
def checkwin(player1,player2):
     
    pattern1 = permutations([1,2,3])
    pattern2 = permutations([4,5,6])
    pattern3 = permutations([7,8,9])
    pattern4 = permutations([1,4,7])
    pattern5 = permutations([2,5,8])
    pattern6 = permutations([3,6,9])
    pattern7 = permutations([1,5,9])
    pattern8 = permutations([3,5,7])
     
 
    for i in pattern1,pattern2,pattern3,pattern4,pattern5,pattern6,pattern7,pattern8:
        for j in list(i):
            play_1 = all(elem in player1 for elem in j)
            play_2 = all(elem in player2 for elem in j)
            if play_1 == True:
                showinfo("HURRAY!!!!!!!", "player 1 win")
                if askokcancel("Restart Game", "Do You Want to Play Again"):
                    restartgame()
                break
            elif play_2 == True:
                showinfo("HURRAY!!!!!!!", "player 2 win")
                if askokcancel("Restart Game", "Do You Want to Play Again"):
                    restartgame()
                break
            else:
                pass
             
            
             
        
def operate(button, Number):
    global x
    global player1,player2
    
    if x % 2 == 0:
        player1.append(Number)
        button.config(text="X")

    else:
        player2.append(Number)
        button.config(text="O")
        
        
    x += 1
    button.config(command= lambda : None)
    checkwin(player1, player2)
    
    

root = Tk()

LPlayer = Label(root, text="PLAYER 1 :- X", font="Arial 12")
LPlayer.grid(row=0,column=1)

LPlayer2 = Label(root, text="PLAYER 2 : O", font="Arial 12")
LPlayer2.grid(row=0,column=2)

b1 = Button(root, text=".", width=3, font="Arial 50")
b2 = Button(root, text=".", width=3, font="Arial 50")
b3 = Button(root, text=".", width=3, font="Arial 50")
b4 = Button(root, text=".", width=3, font="Arial 50")
b5 = Button(root, text=".", width=3, font="Arial 50")
b6 = Button(root, text=".", width=3, font="Arial 50")
b7 = Button(root, text=".", width=3, font="Arial 50")
b8 = Button(root, text=".", width=3, font="Arial 50")
b9 = Button(root, text=".", width=3, font="Arial 50")

b1.config(command= lambda : operate(b1, 1))
b2.config(command= lambda : operate(b2, 2))
b3.config(command= lambda : operate(b3, 3))
b4.config(command= lambda : operate(b4, 4))
b5.config(command= lambda : operate(b5, 5))
b6.config(command= lambda : operate(b6, 6))
b7.config(command= lambda : operate(b7, 7))
b8.config(command= lambda : operate(b8, 8))
b9.config(command= lambda : operate(b9, 9))

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

root.mainloop()
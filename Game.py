from tkinter import Tk,Label,Frame,Entry,Button,LEFT
from tkinter.messagebox import showinfo,askyesno,showwarning

root = Tk()
root.title("Tic Tac Toe")
root.config(bg="White")

switch = 2
player1 = []
player2 = []
players = []
allbutton = []

title = Label(root,text="TIC TAC TOE",font="Jokerman 30", bg="White", fg="Brown")
title.pack(pady=10)

for i in range(2):
        con = Frame(root, bg="White")
        con.pack()
        temp = "Player " + str(i+1) + " : "
        l = Label(con,text=temp, bg="White", font="Arial 10 bold")
        l.pack(side=LEFT, padx=5, pady=10)
        e = Entry(con)
        e.pack(side=LEFT, padx=5)
        players.append(e)
   
current = Label(root, text="Current Turn : X", bg="White", font="Arial 10")
current.pack(padx = 5, pady = 5)

btncintainermain = Frame(root, bg="White")
for i in range(3):
    row = Frame(btncintainermain,bg="White")
    for j in range(3):
        btn = Button(row,text=".",font="Arial 50", width=3, fg="Red")
        btn.pack(side=LEFT, padx=2, pady=2)
        allbutton.append(btn)
    row.pack()
btncintainermain.pack(padx=10, pady=10)

allbutton[0].config(command= lambda : operate(allbutton[0],1))
allbutton[1].config(command= lambda : operate(allbutton[1],2))
allbutton[2].config(command= lambda : operate(allbutton[2],3))
allbutton[3].config(command= lambda : operate(allbutton[3],4))
allbutton[4].config(command= lambda : operate(allbutton[4],5))
allbutton[5].config(command= lambda : operate(allbutton[5],6))
allbutton[6].config(command= lambda : operate(allbutton[6],7))
allbutton[7].config(command= lambda : operate(allbutton[7],8))
allbutton[8].config(command= lambda : operate(allbutton[8],9))

root.withdraw()
root.update_idletasks()   
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()

def operate(b,number):
    global switch,player1,player2,players  
    msg = "No one Wins!!! Try Again"  
    if not (players[0].get() and players[1].get()):
        showwarning("Warning", "Warning No Names Provided")    
    b.config(command= lambda : None)
    winpattern = [
        [1,2,3],
        [4,5,5],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
        ]   
    if switch%2==0:
        b.config(text="X")
        player1.append(number)
        current.config(text="Current Turn : O :") 
        for i in winpattern:
            play1win = all(elem in player1 for elem in i)
            if play1win:
                if not players[0].get():
                    msg = "Player 1 win"
                else:
                    msg = players[0].get() + " win"
                over(msg)
                return 
    else:
        b.config(text="O")
        player2.append(number)
        current.config(text="Current Turn : X :")
        for i in winpattern:
            play2win = all(elem in player2 for elem in i)
            if play2win:
                if not players[1].get():
                    msg = "Player 2 win"
                else:
                    msg = players[1].get() + " win"
                over(msg)
                return
    switch += 1
    if switch == 11:
        over(msg)
        
def over(msg):
    global root
    showinfo("Game Over", msg)
    if askyesno("Game Over", "Play Again"):
        restart()
    else:
        root.destroy()
        
def restart():
    global player1,player2,allbutton,switch
    player1 = []
    player2 = []    
    switch = 2   
    for b in allbutton:
        b.config(text=".")  
    allbutton[0].config(command= lambda : operate(allbutton[0],1))
    allbutton[1].config(command= lambda : operate(allbutton[1],2))
    allbutton[2].config(command= lambda : operate(allbutton[2],3))
    allbutton[3].config(command= lambda : operate(allbutton[3],4))
    allbutton[4].config(command= lambda : operate(allbutton[4],5))
    allbutton[5].config(command= lambda : operate(allbutton[5],6))
    allbutton[6].config(command= lambda : operate(allbutton[6],7))
    allbutton[7].config(command= lambda : operate(allbutton[7],8))
    allbutton[8].config(command= lambda : operate(allbutton[8],9))
    
root.mainloop()

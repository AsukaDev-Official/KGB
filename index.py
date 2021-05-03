#!/usr/bin/env python3
#asukadev
"""
this is free source code game rock paper scissors
using tkinter python.
"""

from tkinter import *
import random

root = Tk()
root.title("Game Kertas Gunting Batu")
width = 620
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="light Blue")

#================================IMAGES========================================
blank_img=PhotoImage(file="images/blank.png")
player_rock=PhotoImage(file="images/player_rock.png")
sm_player_rock=player_rock.subsample(3, 3)
player_paper=PhotoImage(file="images/player_paper.png")
sm_player_paper=player_paper.subsample(3, 3)
player_scissor=PhotoImage(file="images/player_scissor.png")
sm_player_scissor= player_scissor.subsample(3, 3)
com_rock=PhotoImage(file="images/com_rock.png")
com_paper=PhotoImage(file="images/com_paper.png")
com_scissor=PhotoImage(file="images/com_scissor.png")



#===============================METHODS========================================
def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()
 
def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()
    
def Scissor():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess()

def MatchProcess():
    com_choice = random.randint(1,3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()
        
    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        CompututerScissor()

def ComputerRock():
    if player_choice == 1:
        lbl_status.config(text="Game Seri")
    elif player_choice == 2:
        lbl_status.config(text="Player Menang")
    elif player_choice == 3:
        lbl_status.config(text="Computer Menang")
           
def ComputerPaper():
    if player_choice == 1:
        lbl_status.config(text="Computer Menang")
    elif player_choice == 2:
        lbl_status.config(text="Game Seri")
    elif player_choice == 3:
        lbl_status.config(text="Player Menany")
    
def CompututerScissor():
    if player_choice == 1:
        lbl_status.config(text="Player Menang")
    elif player_choice == 2:
        lbl_status.config(text="Computer Menang")
    elif player_choice == 3:
        lbl_status.config(text="Game Seri")

def ExitApp():
    root.destroy()
    exit()

#===============================LABEL WIDGET=========================================
player_img = Label(root,image=blank_img)
comp_img = Label(root,image=blank_img)
lbl_player = Label(root,text="PLAYER")
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="Light Blue")
lbl_computer = Label(root,text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="Light Blue")
lbl_status=Label(root, text="", font=('arial', 10))
lbl_status.config(bg="Light Blue")
player_img.grid(row=2,column=1, padx=30, pady=20)
comp_img.grid(row=2,column=3, padx=50, pady=20)
lbl_status.grid(row=3, column=2)



#===============================BUTTON WIDGET===================================
rock = Button(root, text="Batu", command=Rock)
paper = Button(root, text="Kertas", command=Paper)
scissor = Button(root, text="Gunting", command=Scissor)
btn_quit = Button(root, text="Kembali", command=ExitApp)
rock.grid(row=5,column=1, pady=30)
paper.grid(row=5,column=2, pady=30)
scissor.grid(row=5,column=3, pady=30)
btn_quit.grid(row=6, column=2)


#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()

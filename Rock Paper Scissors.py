#Rock Paper scissors game
from tkinter import *  # type: ignore
import random  as rn

window=Tk()

window.title("Rock Paper Scissors")
window.geometry("1280x720")

usr=0
comp=0

def rand():#Computer Decision
    return rn.choice(["rock", "paper", "scissor"])

def update():#GUI Updater
    l2.config(text=f"You: {usr}")
    l3.config(text=f"Computer: {comp}")

def rock():
    global usr
    global comp
    print("rock")
    temp=rand()
    l4.pack_forget()
    l5.pack_forget()
    if temp=="rock":
        comp=comp+1
        print("comp")
        l5.pack()
    else:
        usr=usr+1
        print("usr")
        l4.pack()

    update()

def paper():
    global usr
    global comp
    print("paper")
    temp=rand()
    l4.pack_forget()
    l5.pack_forget()
    if temp=="paper":
        comp=comp+1
        print("comp")
        l5.pack()
    else:
        usr=usr+1
        print("usr")
        l4.pack()

    update()

def scissor():
    global usr
    global comp
    print("scissor")
    temp=rand()
    l4.pack_forget()
    l5.pack_forget()
    if temp=="scissor":
        comp=comp+1
        print("comp")
        l5.pack()
    else:
        usr=usr+1
        print("usr")
        l4.pack()

    update()
    

#Tkinter GUI
f1=Frame(window)
f1.pack()
l2=Label(f1, text=f"You: {usr}",font="AnnaiMN 30")
l2.pack(side='left')
l1=Label(f1,text="Rock Paper Scissors",font="AnnaiMN 40")
l1.pack(side='left',padx=300)
l3=Label(f1, text=f"Computer: {comp}",font="AnnaiMN 30")
l3.pack(side='left')

f2=Frame(window)
f2.pack(pady= 150)
b1=Button(f2, text="Rock", command=rock,font="AnnaiMN 30")#Rock
b1.pack(side='left')
b2=Button(f2, text="Paper", command=paper,font="AnnaiMN 30")#Paper
b2.pack(side='left',padx=300)
b3=Button(f2, text="Scissor", command=scissor,font="AnnaiMN 30")#Scissor
b3.pack(side='left')

l4=Label(window,text="🎉YOU WIN🎉",font="AnnaiMN 30")
l5=Label(window,text="🎉COMPUTER WINS🎉",font="AnnaiMN 30")

window.mainloop()
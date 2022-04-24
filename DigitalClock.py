#-------------------------------------------------------------------------------
# Name: Digital Calender & Clock
# Purpose: Learning
#
# Author:      Argha Mukherjee
#
# Created:     24-04-2022
# Copyright:   (c) Argha 2022
# Licence:     <your licence> <This is an open source Code Everyone can use it. >
#-------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime


def quit(*args):
    root.destroy()

def clock_time():

    time= datetime.datetime.now()
    time= (time.strftime("Date: %Y -%m -%d \nTime: %H:%M:%S"))
    txt.set(time)

    root.after(1000,clock_time)

root =Tk()
# root.attributes("-fullscreen", False)
root.configure(bg= "#7DF9FF")
root.bind("x",quit)
root.geometry("1200x400")
root.title("Digital Calender & Clock  GUI by ARGHA MUKHERJEE")
root.after(1000,clock_time)

fnt = font.Font(family = "helvetica",size=80, weight ="bold")
txt = StringVar()
lbl = ttk.Label(root,textvariable=txt, font = fnt,foreground= "navy" ,background= "#00FF7F")
lbl.place(relx=0.5,rely=0.5, anchor=CENTER)

root.mainloop()
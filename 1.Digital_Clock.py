# Program to create a digital clock using Python.

from tkinter import *
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("clock")

def time ():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time)
    
label = Label(root, font=("sans-serif",150), background = "black", foreground = "white")
label.pack(anchor="center")
time()

mainloop() 
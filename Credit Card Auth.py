# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:39:53 2022

@author: anees
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.geometry("400x400")
numberInput = Entry(root)
numberInput.pack()

img = ImageTk.PhotoImage(Image.open("credit.jpg"))
label = Label(root, image=img)

def auth():
    try:
        inputValue = int(numberInput.get())
        messagebox.showinfo("Alert","Credit card accepted")
    except(ValueError):
        messagebox.showinfo("Alert", "Credit card not accepted. Enter valid pin")
        
btn = Button(root, text = "check credit card", command = auth)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()
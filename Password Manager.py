from os import replace
from tkinter import *
import random,string
import pyperclip

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Password Manager")

frame = Frame(root)
frame.grid(row=0,column=0,padx=10,pady=10)

labelPass = Label(frame,text="Password Length",font = "arial 10 bold")
labelPass.grid(row=0,column=0,padx=10,pady=10)

passLen = IntVar()
length = Spinbox(frame,from_=8,to=32,textvariable=passLen)
length.grid(row=0,column=1,padx=10,pady=10)

pass_str = StringVar()
def PassGenerator():
    password = ''
    for x in range (0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(passLen.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

buttonGen = Button(root,text="Generate",command=PassGenerator)
buttonGen.grid(row=1,column=0,padx=10,pady=10)

entry = Entry(root,textvariable=pass_str)
entry.grid(row=2,column=0,padx=10,pady=10)

def copyPassword():
    pyperclip.copy(pass_str.get())

copyButton = Button(root,text="Copy to Clipboard",command=copyPassword)
copyButton.grid(row=3,column=0,padx=10,pady=10)

root.mainloop()

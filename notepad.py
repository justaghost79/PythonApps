import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *

root = tk.Tk()

root.title("Notes")

textarea = ScrolledText(root)
textarea.pack()

menu = Menu(root)
file = Menu(menu, tearoff = 0)

def Open():
    print("Hello")
def Save():
    print("Save")
def SaveAs():
    print("Save As")
def Exit():
    print("Exit")
file.add_command(label="Open", command=open)
file.add_command(label="Save", command=Save)
file.add_command(label="Save As", command=SaveAs)
file.add_separator()
file.add_command(label="Exit", command=Exit)
menu.add_cascade(label="File", menu=file)
root.config(menu=menu)

root.mainloop()

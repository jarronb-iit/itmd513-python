from tkinter import *


class JarronsButtons:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()


def printName(event):
    print("My name is Jarron")


def leftClick(event):
    print("Left")


def middleClick(event):
    print("Middle")


def rightClick(event):
    print("Right")


root = Tk()
# button1 = Button(root, text="Print my name", command=printName)
button1 = Button(root, text="Print my name")
button1.bind("<Button-1>", printName)
label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)


label1.grid(row=0, sticky=N)
label2.grid(row=1, sticky=N)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
button1.grid(columnspan=2)
frame.grid()

root.mainloop()

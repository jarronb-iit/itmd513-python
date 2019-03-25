from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk


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


def onclick(event=None):
    print(event.widget.get())
    root.focus()


# window.geometry("200x100+0+100")
root = tk.ThemedTk()
root.get_themes()
# aquativo, arc, black, blue, clearlooks, elegance, equilux, itft1, keramik, kroc, plastik, radiance, scid themes, smog, winxpblue
root.set_theme("radiance")
# button1 = Button(root, text="Print my name", command=printName)
button1 = ttk.Button(root, text="Print my name")
button1.bind("<Button-1>", printName)
label1 = ttk.Label(root, text="Name")
label2 = ttk.Label(root, text="Password")
entry_1 = ttk.Entry(root)
entry_2 = ttk.Entry(root)

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
entry_1.bind('<Return>', onclick)


label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
button1.grid(columnspan=2)
# frame.grid()

root.mainloop()

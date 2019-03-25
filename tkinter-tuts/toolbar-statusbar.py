from tkinter import *


def doNothing():
    print("Ok ok I won't...")


root = Tk()

# ***** Main Menu ******

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project...", command=doNothing)
submenu.add_command(label="New...", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ***** Toolbar ******

toolbar = Frame(root, bg="blue")

insetButton1 = Button(toolbar, text="Insert Image", command=doNothing)
insetButton1.pack(side=LEFT, padx=2, pady=2)
insetButton2 = Button(toolbar, text="Print", command=doNothing)
insetButton2.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** The Toolbar ******
status = Label(root, text="Preparing to do nothing....",
               bd=1, relief=SUNKEN, anchor=W, font="Times 10 italic")

status.pack(side=BOTTOM, fill=X)
root.mainloop()

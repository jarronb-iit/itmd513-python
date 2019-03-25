'''
Jarron Bailey
Homework 8
Date: March 22nd, 2019
Description: The program should display a menu that lets the user look up a person’s email address, add a new name and email address, change an existing email address, and delete an existing name and email address. The program should bind the dictionary and save it to a file when the user exits the program.
'''

from tkinter import *
import tkinter as tk1
from tkinter import ttk
from ttkthemes import themed_tk as tk
import json

dataSet = {
    "alex": "alex@aol.com",
    "alex2": "alex@aol.com",
    "alex3": "alex@aol.com",
    "cierra": "cieraa@gmail.com",
    "cierra2": "cieraa@gmail.com",
    "cierra3": "cieraa@gmail.com",
    "jimmy": "kimmy@gmail.com",
    "jimmy2": "kimmy@gmail.com",
    "jimmy3": "kimmy@gmail.com",
    "tom": "tom@gmail.com",
    "tom1": "tom@gmail.com@gmail.com",
    "tom3": "tom@gmail.com@gmail.com",
    "alex4": "alex@aol.com",
    "cierra4": "cieraa@gmail.com",
    "jimmy4": "kimmy@gmail.com",
    "tom4": "tom@gmail.com@gmail.com",
    "alex5": "alex@aol.com",
    "cierra5": "cieraa@gmail.com",
    "jimmy5": "kimmy@gmail.com",
    "tom15": "tom@gmail.com@gmail.com"
}


class AppGui:
    def __init__(self, master):
        self.master = master

        # Fame 1
        self.frameOne = Frame(self.master)
        self.frameOne.grid(row=0, column=0)

        # Frame 2
        self.frameTwo = Frame(self.master)
        self.frameTwo.grid(row=1, column=0)

        self.canvas = Canvas(self.frameTwo)
        self.listFrame = Frame(self.canvas)

        self.scrollbar = Scrollbar(
            self.master, orient="vertical", command=self.canvas.yview)

        # set scroll on canvas
        self.canvas["yscrollcommand"] = self.scrollbar.set

        self.canvas.create_window((0, 0), window=self.listFrame, anchor="nw")
        self.listFrame.bind("<Configure>", self.AuxscrollFunction)
        self.scrollbar.grid_forget()

        self.canvas.pack(side="left")

        self.scrollbar.grid(row=1, column=5, sticky="nsew")
        self.nameLabel = ttk.Label(
            self.listFrame, text="Names", font="Helvetica 16 bold")
        self.emailLabel = ttk.Label(
            self.listFrame, text="Emails", font="Helvetica 16 bold")
        self.nameLabel.grid(row=2)
        self.emailLabel.grid(row=2, column=3)

    def AuxscrollFunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"), width=X, height=Y)


root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.geometry("500x500+100+100")
b = AppGui(root)
root.mainloop()

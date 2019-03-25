'''
Jarron Bailey
Homework 8
Date: March 22nd, 2019
Description: The program should display a menu that lets the user look up a person’s email address, add a new name and email address, change an existing email address, and delete an existing name and email address. The program should bind the dictionary and save it to a file when the user exits the program.
'''

# using partial
# https://stackoverflow.com/questions/3296893/how-to-pass-an-argument-to-event-handler-in-tkinter

# Get widgets grid info
# https://stackoverflow.com/questions/37731654/how-to-retrieve-the-row-and-column-information-of-a-button-and-use-this-to-alter

from tkinter import *
import tkinter as tk1
from tkinter import ttk
from ttkthemes import themed_tk as tk
import json
from functools import partial

dataSetSample = {
    "tom": "tom@gmail.com",
    "jimmy": "kimmy@gmail.com",
    "cierra": "cieraa@gmail.com"
}

for name in dataSetSample:
    print(name + ":" + dataSetSample[name])
    entryName = name + "name"
    print(entryName)
    entryEmail = name + "email"
    print(entryEmail)

# saveDataSetToFile()

# ************************
# Scrollable Frame Class
# ************************


class ScrollFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # create a frame (self)

        # place canvas on self
        self.canvas = tk1.Canvas(self, borderwidth=0, background="#ffffff")
        # place a frame on the canvas, this frame will hold the child widgets
        self.viewPort = tk1.Frame(self.canvas, background="#ffffff")
        # place a scrollbar on self
        self.vsb = tk1.Scrollbar(self, orient="vertical",
                                 command=self.canvas.yview)
        # attach scrollbar action to scroll of canvas
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # pack scrollbar to right of self
        self.vsb.pack(side="right", fill="y")
        # pack canvas to left of self and expand to fil
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.viewPort, anchor="nw",  # add view port frame to canvas
                                  tags="self.viewPort")

        # bind an event whenever the size of the viewPort frame changes.
        self.viewPort.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"))  # whenever the size of the frame changes, alter the scroll region respectively.


class AppGui:
    def __init__(self, master):
        self.currentEntryVal = ""
        self.newEntryVal = ""
        self.entryType = ""

        self.master = master

        self.topFrame = Frame(self.master)
        self.topFrame.grid(column=0, row=0, sticky=(N, E, W))

        self.mainFrame = Frame(self.master)
        self.mainFrame.grid(column=0, row=1, sticky=(N, E, W), pady=(0, 20))

        # ***** Top Frame *****
        self.saveFileBtn = ttk.Button(
            self.topFrame, text="Save File", command=self.saveDataSetToFile)
        self.exitBtn = ttk.Button(
            self.topFrame, text="Exit", command=self.onExit)

        self.saveFileBtn.grid(row=0, column=1, sticky=(
            S, E, W, N), pady=15, padx=7.5)
        self.exitBtn.grid(row=0, column=2, sticky=(
            S, E, W, N), pady=15, padx=7.5)

        # ***** Main Frame *****
        self.nameLabel = ttk.Label(
            self.mainFrame, text="Names", font="Helvetica 16 bold")
        self.emailLabel = ttk.Label(
            self.mainFrame, text="Emails", font="Helvetica 16 bold")
        self.nameLabel.grid(row=0)
        self.emailLabel.grid(row=0, column=1)
        self.dataSet = self.loadDataSetFromFile()

        for ctr, name in enumerate(self.dataSet):
            ctr += 1
            self.name = name
            self.email = self.dataSet[name]
            self.entryName = name + "Name"
            self.entryEmail = name + "Email"

            self.entryName = ttk.Entry(
                self.mainFrame, font="Helvetica 12")
            self.entryName.insert(0, self.name)
            self.entryName.bind('<Return>', self.onEntryInteraction)
            self.entryName.bind('<Button-1>', self.onEntryInteraction)

            self.entryEmail = ttk.Entry(self.mainFrame, font="Helvetica 12")
            self.entryEmail.insert(0, self.email)
            self.entryEmail.bind('<Return>', self.onEntryInteraction)
            self.entryEmail.bind('<Button-1>', self.onEntryInteraction)

            self.entryButton = ttk.Button(
                self.mainFrame, text="Delete")
            self.entryButton.bind(
                "<ButtonPress-1>", partial(self.deleteEntry, name=self.name, email=self.email))

            self.entryName.grid(row=ctr, column=0, sticky=(
                N, S, E, W), pady=2, padx=(15, 7.5))
            self.entryEmail.grid(row=ctr, column=1, sticky=(
                N, S, E, W), pady=2, padx=(7.5, 15))
            self.entryButton.grid(row=ctr, column=2, sticky=(
                N, S, E, W), pady=2, padx=(0, 10))

            self.ctr = ctr

        # ***** Scroll Bar *****
        self.scrollbar = ttk.Scrollbar(self.master)
        self.scrollbar.grid(column=6, row=1,  sticky=N+S+W)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.columnconfigure(1, weight=1)

        self.topFrame.columnconfigure(0, weight=2)
        self.topFrame.columnconfigure(3, weight=2)

        self.topFrame.columnconfigure(1, weight=1)
        self.topFrame.columnconfigure(2, weight=1)

    def loadDataSetFromFile(self):
        try:
            with open('dataSet.json', 'r') as inputFile:
                dataSet = json.load(inputFile)
            return dataSet
        except FileNotFoundError:
            # TODO: Alert message file not found
            print("File not found!")
            dataSet = {}
            return dataSet

    def saveDataSetToFile(self):
        print("File")
        with open('dataSet.json', 'w') as outfile:
            json.dump(self.dataSet, outfile, sort_keys=True,
                      indent=2, separators=(',', ': '))

    def onExit(self):
        self.master.destroy()

    def addEntry(self):
        self.newNameEntry = ttk.Entry(self.mainFrame, font="Helvetica 12")
        self.newNameEntry.bind('<Return>', self.onEntryInteraction)
        self.newNameEntry.bind('<Button-1>', self.onEntryInteraction)

        self.newEmailEntry = ttk.Entry(self.mainFrame, font="Helvetica 12")
        self.newEmailEntry.bind('<Return>', self.onEntryInteraction)
        self.newEmailEntry.bind('<Button-1>', self.onEntryInteraction)

        self.entryButton = ttk.Button(self.mainFrame, text="Delete")
        self.entryButton.bind("<ButtonPress-1>", partial(self.deleteEntry, name=self.name, email=self.email))

    def deleteEntry(self, event, name, email):
        print(name, email, event)
        row = event.widget.grid_info()['row']      # Row of the button
        # grid_info will return dictionary with all grid elements (row, column, ipadx, ipday, sticky, rowspan and columnspan)
        column = event.widget.grid_info()['column']
        print("Grid position of 'btn': {} {}".format(row, column))
        for label in self.mainFrame.grid_slaves():
            if int(label.grid_info()["row"]) == row:
                label.grid_forget()

    def onEntryInteraction(self, event):
        print(event.num)
        print(event.keycode)
        print(event.widget.get())
        self.master.focus()

        if event.num == 1:
            self.currentEntryVal = event.widget.get()

        if event.keycode == 13:
            self.newEntryVal = event.widget.get()
            print("old data")
            print(self.dataSet)

            for name, email in self.dataSet.items():
                if name == self.currentEntryVal:
                    print(name)
                    self.dataSet[self.newEntryVal] = self.dataSet.pop(
                        self.currentEntryVal)
                    break
                elif email == self.currentEntryVal:
                    self.dataSet[name] = self.newEntryVal
                    break
            print("NEW data")
            print(self.dataSet)

        print("[CURRENT_VAL]" + self.currentEntryVal)
        print("[NEW_VAL]" + self.newEntryVal)


root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.geometry("500x500+100+100")
b = AppGui(root)
root.mainloop()

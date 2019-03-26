'''
Jarron Bailey
Homework 8
Date: April 1st, 2019
Description: This program displays a menu that lets the user look up a person’s email address, add a new name and email address, change an existing email address, and delete an existing name and email address. Each time the program starts, it retrieves the dictionary from the file. The program runs continuously until the user selects option exit from the menu.
'''

try:
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import tkinter.messagebox
    import json
    from functools import partial
    import re
except ImportError:  # If Import error -> Try again
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import tkinter.messagebox
    import json
    from functools import partial
    import re

# Scrollable Frame Class
# https://gist.github.com/novel-yet-trivial/3eddfce704db3082e38c84664fc1fdf8

# using partial
# https://stackoverflow.com/questions/3296893/how-to-pass-an-argument-to-event-handler-in-tkinter

# Get widgets grid info
# https://stackoverflow.com/questions/37731654/how-to-retrieve-the-row-and-column-information-of-a-button-and-use-this-to-alter


class VerticalScrolledFrame:
    """
    Author: Github ID = @novel-yet-trivial
    Link: https://gist.github.com/novel-yet-trivial/3eddfce704db3082e38c84664fc1fdf8
    A vertically scrolled Frame that can be treated like any other Frame
    ie it needs a master and layout and it can be a master.
    keyword arguments are passed to the underlying Frame
    except the keyword arguments 'width' and 'height', which
    are passed to the underlying Canvas
    note that a widget layed out in this frame will have Canvas as self.master,
    if you subclass this there is no built in way for the children to access it.
    You need to provide the controller separately.
    """

    def __init__(self, master, **kwargs):
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)
        self.outer = ttk.Frame(master, **kwargs)

        self.vsb = ttk.Scrollbar(self.outer, orient=VERTICAL)
        self.vsb.pack(fill=Y, side=RIGHT)
        self.canvas = Canvas(self.outer, highlightthickness=0,
                             width=width, height=height)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvas['yscrollcommand'] = self.vsb.set
        # mouse scroll does not seem to work with just "bind"; You have
        # to use "bind_all". Therefore to use multiple windows you have
        # to bind_all in the current widget
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview

        self.inner = ttk.Frame(self.canvas)
        # pack the inner Frame into the Canvas with the topleft corner 4 pixels offset
        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(ttk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            # geometry attributes etc (eg pack, destroy, tkraise) are passed on to self.outer
            return getattr(self.outer, item)
        else:
            # all other attributes (_w, children, etc) are passed to self.inner
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        self.canvas.config(scrollregion=(0, 0, x2, max(y2, height)))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")


class AppGui:
    '''
    This class is responsible for displaying the Application GUI and handling the different states of the widgets
    '''

    def __init__(self, master):
        '''
        Init Function is responsible for Initializing variables that will be used to manage state of widgets
        and run
        '''
        # ***Initial variables for Entry list***
        self.currentEntryVal = ""
        self.newEntryVal = ""
        self.entryColumn = ""
        self.entriesAdded = 0
        self.entriesDeleted = 0
        self.entriesUpdated = 0

        # ***Initial variables for search results***
        self.searchResult = StringVar()
        self.searchResult.set("Result Pending...")

        # ***Initial variables for status bar***
        self.statusText = StringVar()
        self.statusText.set("Actions pending...")

        # ***Initial variables for Frame***
        self.entriesFrameNum = 4
        self.entryErroed = False
        self.master = master

        self.dataSet = self.loadDataSetFromFile()

        # ***Initializing Frames postion in root***
        self.topFrame = Frame(self.master)
        self.topFrame.pack(side=TOP, fill=X, anchor=NW)

        self.addFrame = Frame(self.master)
        self.addFrame.pack(side=TOP, fill=BOTH)

        self.searchFrame = Frame(self.master)
        self.searchFrame.pack(side=TOP, fill=BOTH)

        status = ttk.Label(self.master, textvariable=self.statusText,
                           relief=SUNKEN, anchor=W, font="Times 10 italic")
        status.pack(side=BOTTOM, fill=X)

        self.createTopFrame()
        self.createMainFrame()
        self.setFrameGridConfigs()

    def createTopFrame(self):
        '''
        Function builds the top frame of the which consits of four buttons that are
        save file, add entry, search entry, and exit
        '''
        # ***Creates widgets***
        self.saveFileBtn = ttk.Button(
            self.topFrame, text="Save File", command=self.saveDataSetToFile)
        self.addSectionBtn = ttk.Button(
            self.topFrame, text="Add Entry", command=self.onAddEntrySection)
        self.searchSectionBtn = ttk.Button(
            self.topFrame, text="Search Entry", command=self.onAddSearchSection)
        self.exitBtn = ttk.Button(
            self.topFrame, text="Exit", command=self.onExit)

        # ***Widgets Layout***
        self.saveFileBtn.grid(row=0, column=1, sticky=(
            S, E, W, N), pady=15, padx=7.5)
        self.addSectionBtn.grid(row=0, column=2, sticky=(
            S, E, W, N), pady=15, padx=7.5)
        self.searchSectionBtn.grid(row=0, column=3, sticky=(
            S, E, W, N), pady=15, padx=7.5)
        self.exitBtn.grid(row=0, column=4, sticky=(
            S, E, W, N), pady=15, padx=7.5)

    def createMainFrame(self):
        '''
        Function build out the main frame of the application which consits of
        a list of entries that filled with names and email address that can be edited or deleted
         '''

        # ***** Add Main Frame to Master Frame*****
        self.mainFrame = VerticalScrolledFrame(self.master)
        self.mainFrame.pack(fill=BOTH, expand=True)

        # ***** If dataset is empty*****
        if len(self.dataSet) == 0:
            self.datasetEmpty = ttk.Label(
                self.mainFrame, text="No data loaded from file...\nPlease add an entry.\nNote: Entries in the List can be directly modified", font="Helvetica 16")

            self.datasetEmpty.grid(row=0, column=1)

        # ***Creates widgets***
        self.nameLabel = ttk.Label(
            self.mainFrame, text="Names", font="Helvetica 16 bold")
        self.emailLabel = ttk.Label(
            self.mainFrame, text="Emails", font="Helvetica 16 bold")

        for ctr, name in enumerate(self.dataSet):
            ctr += 1
            self.name = name
            self.email = self.dataSet[name]
            self.entryName = name + "Name"
            self.entryEmail = name + "Email"

            # Names Entries
            self.entryName = ttk.Entry(
                self.mainFrame, font="Helvetica 12")
            self.entryName.insert(0, self.name)
            self.entryName.bind('<Return>', self.onEntryInteraction)
            self.entryName.bind('<Button-1>', self.onEntryInteraction)

            # Email Entries
            self.entryEmail = ttk.Entry(self.mainFrame, font="Helvetica 12")
            self.entryEmail.insert(0, self.email)
            self.entryEmail.bind('<Return>', self.onEntryInteraction)
            self.entryEmail.bind('<Button-1>', self.onEntryInteraction)

            # Delete Buttons
            self.entryButton = ttk.Button(
                self.mainFrame, text="Delete")
            self.entryButton.bind(
                "<ButtonPress-1>", partial(self.deleteEntry, name=self.name, email=self.email))

            # ***Widgets Layout***
            self.nameLabel.grid(row=0, column=1)
            self.entryName.grid(row=ctr, column=1, sticky=(
                N, S, E, W), pady=2, padx=(15, 7.5))
            self.emailLabel.grid(row=0, column=2)
            self.entryEmail.grid(row=ctr, column=2, sticky=(
                N, S, E, W), pady=2, padx=(7.5, 15))
            self.entryButton.grid(row=ctr, column=3, sticky=(
                N, S, E, W), pady=2, padx=(0, 10))

            self.ctr = ctr

    def onAddEntrySection(self):
        '''
        Function is responsible for building out the add entry section during
        the "Add Entry" button click
        '''

        # ***Creates widgets***
        self.addSectionLabel = ttk.Label(
            self.addFrame, text="Add Entry", font="Helvetica 12 bold")
        self.nameLabel = ttk.Label(
            self.addFrame, text="Name:", font="Helvetica 10")
        self.emailLabel = ttk.Label(
            self.addFrame, text="Email:", font="Helvetica 10")
        self.newEntryName = ttk.Entry(
            self.addFrame, font="Helvetica 12")
        self.newEntryEmail = ttk.Entry(
            self.addFrame, font="Helvetica 12")
        self.addNewEntryBtn = ttk.Button(
            self.addFrame, text="Done")

        self.addNewEntryBtn.bind('<Button-1>', self.addNewEntry)
        self.newEntryEmail.bind('<Return>', self.addNewEntry)

        # ***Widgets Layout***
        self.addSectionLabel.grid(row=0, column=1, sticky=(
            N, E, W))
        self.nameLabel.grid(row=1, column=1, sticky=(
            N, E, W))
        self.newEntryName.grid(row=2, column=1, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.emailLabel.grid(row=1, column=2, sticky=(
            N, E, W))
        self.newEntryEmail.grid(row=2, column=2, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.addNewEntryBtn.grid(row=2, column=3, sticky=(
            N, E, W), pady=15, padx=7.5)

        self.addSectionBtn.config(state=DISABLED)
        self.master.focus()
        self.statusText.set("Adding entry...")

    def onAddSearchSection(self):
        '''
        Function is responsible for building out the add entry section during
        the "Add Entry" button click
        '''

        # ***Creates widgets***
        self.addSearchSectionLabel = ttk.Label(
            self.searchFrame, text="Search for Entry", font="Helvetica 12 bold")
        self.searchEntryLabel = ttk.Label(
            self.searchFrame, text="By Name or Email:", font="Helvetica 10")
        self.searchEntry = ttk.Entry(
            self.searchFrame, font="Helvetica 12", width=30)
        self.searchResultEntry = ttk.Entry(
            self.searchFrame, textvariable=self.searchResult, font="Helvetica 12", state="readonly", width=30)
        self.searchEntryBtn = ttk.Button(
            self.searchFrame, text="Search")
        self.searchEntryBtn.bind("<ButtonPress-1>", self.onSearch)
        self.searchEntry.bind("<Return>", self.onSearch)

        # ***Widgets Layout***
        self.addSearchSectionLabel.grid(row=0, column=1, sticky=(
            N, E, W))
        self.searchEntryLabel.grid(row=1, column=1, sticky=(
            N, E, W))
        self.searchEntry.grid(row=2, column=1, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.searchResultEntry.grid(row=2, column=3, sticky=(
            N, E, W))
        self.searchEntryBtn.grid(row=2, column=4, sticky=(
            N, E, W), pady=15, padx=7.5)

        self.searchSectionBtn.config(state=DISABLED)
        self.master.focus()
        self.statusText.set("Searching entry...")

    def setFrameGridConfigs(self):
        '''
        Function is responsible for adding grid configurations for 3/4 of the frames
        which is the top frame, add section frame, search entry frame. First group of 
        configs for each frame prospectively is for the content, and the second is the 
        spacing around the content.
        '''
        self.topFrame.columnconfigure(1, weight=1)
        self.topFrame.columnconfigure(2, weight=1)
        self.topFrame.columnconfigure(3, weight=1)
        self.topFrame.columnconfigure(4, weight=1)

        self.topFrame.columnconfigure(0, weight=4)
        self.topFrame.columnconfigure(5, weight=4)

        self.addFrame.columnconfigure(1, weight=1)
        self.addFrame.columnconfigure(2, weight=1)
        self.addFrame.columnconfigure(3, weight=1)

        self.addFrame.columnconfigure(0, weight=4)
        self.addFrame.columnconfigure(4, weight=4)

        self.searchFrame.columnconfigure(1, weight=1)
        self.searchFrame.columnconfigure(3, weight=1)
        self.searchFrame.columnconfigure(4, weight=1)

        self.searchFrame.columnconfigure(0, weight=4)
        self.searchFrame.columnconfigure(2, weight=0)
        self.searchFrame.columnconfigure(5, weight=4)

    def onEntryInteraction(self, event):
        '''
        Function allows entries in the main frame to be modified and updates dataset of modification
        '''

        # Initializing variables
        isNameInDataset = False
        nameInDataset = None
        isEmailInDataset = False
        emailInDataset = None

        self.master.focus()

        # Mouse click
        if event.num == 1:
            self.currentEntryVal = event.widget.get()

        # Enter Key
        if event.keycode == 13:
            self.newEntryVal = event.widget.get()
            self.entryColumn = event.widget.grid_info()['column']

            if self.entryColumn == 1:
                self.entryColumn = "name"
            elif self.entryColumn == 2:
                self.entryColumn = "email"

            # Get original name and email of modified data entry
            for name, email in self.dataSet.items():
                if name == self.currentEntryVal or self.currentEntryVal == email:
                    nameInDataset = name
                    emailInDataset = email
                    break

            answer = tkinter.messagebox.askyesno(
                "Overwriting Entry", "Are you sure you want to overwrite existing entry of {}.".format(self.currentEntryVal))

            if answer == False:
                self.entryErroed = True
                event.widget.delete(0, END)
                event.widget.insert(0, self.currentEntryVal)
                self.currentEntryVal = None
                self.newEntryVal = None
                return
            else:
                if self.entryColumn == "name":
                    emailInDataset = self.dataSet[self.currentEntryVal]
                    del self.dataSet[self.currentEntryVal]
                    self.dataSet[self.newEntryVal] = emailInDataset

                elif self.entryColumn == 'email':
                    isValidEmail = self.validEmail(self.newEntryVal)
                    if not isValidEmail:
                        self.entryErroed = True
                        tkinter.messagebox.showerror(
                            "Invalid Entry", "Please enter a valid email")
                        print("Error: Please enter a valid email")
                        return
                    else:
                        self.dataSet[nameInDataset] = self.newEntryVal

                print(self.dataSet)
                self.entriesUpdated += 1

            self.statusText.set("Entry updated | Total entries updated: {} | Total entries: {}".format(
                self.entriesUpdated, len(self.dataSet)))
            return print("Entry updated | Total entries updated: {} | Total entries: {}".format(self.entriesUpdated, len(self.dataSet)))

    def addNewEntry(self, event):
        '''
        Function adds a new entry of an name and email to the main frame which is the listing
        of the dataset
        '''
        newEntryName = self.newEntryName.get()
        newEntryEmail = self.newEntryEmail.get()

        # Check to see if name or email exist in dataset already
        for name, email in self.dataSet.items():
            if name == newEntryName:
                self.entryErroed = True
                tkinter.messagebox.showerror(
                    "Invalid Entry", "Name already exist.")
                print("Error: Name already exist.")
                return
            elif email == newEntryEmail:
                self.entryErroed = True
                tkinter.messagebox.showerror(
                    "Invalid Entry", "Email already exist.")
                print("Error: Email already exist.")
                return

        # If name and email is unique check the validity of email
        isValidEmail = self.validEmail(newEntryEmail)
        if not isValidEmail:
            self.entryErroed = True
            tkinter.messagebox.showerror(
                "Invalid Entry", "Please enter a valid email")
            print("Error: Please enter a valid email.")
        else:
            # If erroed increase number of the main entry frame is increased by one
            if self.entryErroed:
                self.entriesFrameNum + 1

            # Set Entry & update frame
            self.dataSet[newEntryName] = newEntryEmail
            self.removeFrame(self.mainFrame)

            # Reset styles
            self.master.after(0, self.createMainFrame)
            self.newEntryName.delete(0, 'end')
            self.newEntryEmail.delete(0, 'end')
            self.master.focus()
            self.entriesFrameNum += 1

            self.entriesAdded += 1
            self.statusText.set("Entry added | Total new entries: {} | Total entries: {}".format(
                self.entriesAdded, len(self.dataSet)))
            return print("Entry added | Total new entries: {} | Total entries: {}".format(
                self.entriesAdded, len(self.dataSet)))

    def onSearch(self, event):
        '''
        Function search through dataset and returns either a matching email or name depending on information queried
        '''
        # Variables initialization
        isNameInDataset = False
        isEmailInDataset = False
        nameInDataset = ""
        emailInDataset = ""

        searchEntryText = self.searchEntry.get()

        for name, email in self.dataSet.items():

            if name == searchEntryText:
                isNameInDataset = True
                emailInDataset = email
            elif searchEntryText == email:
                isEmailInDataset = True
                nameInDataset = name
                break

        if isNameInDataset:
            self.searchResult.set("Email: " + emailInDataset)
        elif isEmailInDataset:
            self.searchResult.set("Name: " + nameInDataset)
        else:
            print("Error: Entry Not Found...")
            return tkinter.messagebox.showerror("Entry Not Found", "Entry doesn't exist.")

        self.statusText.set("Results retrieved...")
        print("Results retrieved...")

    def deleteEntry(self, event, name, email):
        parentFame = event.widget.master.winfo_name()
        self.entriesFrameNum = int(list(filter(str.isdigit, parentFame))[0])

        row = event.widget.grid_info()['row']      # Row of the button
        # grid_info will return dictionary with all grid elements (row, column, ipadx, ipday, sticky, rowspan and columnspan)

        for label in self.master.children[parentFame].children["!canvas"].children["!frame"].grid_slaves():
            if int(label.grid_info()["row"]) == row:
                label.grid_remove()
        self.dataSet.pop(name)
        self.entriesDeleted += 1

        self.statusText.set("Entry deleted | Total entries deleted: {} | Total entries: {}".format(
            self.entriesDeleted, len(self.dataSet)))
        return print("Entry deleted | Total entries deleted: {} | Total entries: {}".format(self.entriesDeleted, len(self.dataSet)))

    def loadDataSetFromFile(self):
        '''
        Function returns a dataset from "dataset.json" file if file dont exist
        the dataset is initialized to an empty dictionary
        '''
        try:
            with open('dataSet.json', 'r') as inputFile:
                dataSet = json.load(inputFile)
                inputFile.close()

            self.statusText.set(
                "File loaded | Total entries: {}".format(len(dataSet)))
            print(("File loaded | Total entries: {}".format(len(dataSet))))
            return dataSet
        except FileNotFoundError:
            # TODO: Alert message file not found
            dataSet = {}
            print("File not found!")
            return dataSet

    def saveDataSetToFile(self):
        '''
        Function saves current dataset to "dataset.json and sorts data on save
        '''
        with open('dataSet.json', 'w') as outfile:
            json.dump(self.dataSet, outfile, sort_keys=True,
                      indent=2, separators=(',', ': '))
            outfile.close()

        self.master.focus()

        self.statusText.set("File saved | Total new entries: {} | Total deleted: {} | Total entries updated: {} | Total entries: {}".format(
            self.entriesAdded, self.entriesDeleted, self.entriesUpdated, len(self.dataSet)))
        return print("File saved | Total new entries: {} | Total deleted: {} | Total entries updated: {} | Total entries: {}".format(
            self.entriesAdded, self.entriesDeleted, self.entriesUpdated, len(self.dataSet)))

    def validEmail(self, email):
        '''
        Function returns if an email is valid or not by checking email against an
        regular expression
        '''
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not EMAIL_REGEX.match(email):
            return False
        else:
            return True

    def removeFrame(self, frame):
        '''Function removes the frame passed in from the GUI'''
        frame.pack_forget()
        frame.destroy()

    def onExit(self):
        '''Function quits program by destroying root frame during click of the "Exit" button '''
        self.master.destroy()
        return print("Program exited...")


# Run Main program with themes, if fail -> no thememing
if __name__ == "__main__":
    try:
        root = tk.ThemedTk()
        root.get_themes()
        root.set_theme("radiance")
    except:
        root = Tk()
    finally:
        root.geometry("700x500+100+100")
        AppGui(root)
        root.mainloop()

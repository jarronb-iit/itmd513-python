
try:
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import json
except ImportError:
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import json

# https://gist.github.com/novel-yet-trivial/3eddfce704db3082e38c84664fc1fdf8
class VerticalScrolledFrame:
    """
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
        self.canvas = Canvas(self.outer, highlightthickness=0, width=width, height=height)
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
        self.canvas.config(scrollregion = (0,0, x2, max(y2, height)))

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
            self.canvas.yview_scroll(-1, "units" )
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units" )

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
        self.currentEntryVal = ""
        self.newEntryVal = ""
        self.entryType = ""
        self.dataSet = dataSet

        self.master = master
        self.frame = VerticalScrolledFrame(root, width=300, borderwidth=2, relief=SUNKEN)
        #frame.grid(column=0, row=0, sticky='nsew') # fixed size
        self.frame.pack(fill=BOTH, expand=True) # fill window
        
        for ctr, name in enumerate(self.dataSet):
            ctr += 1
            self.name = name
            self.email = self.dataSet[name]
            self.entryName = name + "Name"
            self.entryEmail = name + "Email"

            self.entryName = ttk.Entry(
                self.frame, font="Helvetica 12")
            self.entryName.insert(0, self.name)
            self.entryName.bind('<Return>', self.onEntryInteraction)
            self.entryName.bind('<Button-1>', self.onEntryInteraction)

            self.entryEmail = ttk.Entry(self.frame, font="Helvetica 12")
            self.entryEmail.insert(0, self.email)
            self.entryEmail.bind('<Return>', self.onEntryInteraction)
            self.entryEmail.bind('<Button-1>', self.onEntryInteraction)

            self.entryButton = ttk.Button(self.frame, text="Delete")

            self.entryName.grid(row=ctr, column=0, sticky=(N, S, E, W), pady=2, padx=(15, 7.5))
            self.entryEmail.grid(row=ctr, column=1, sticky=(N, S, E, W), pady=2, padx=(7.5, 15))
            self.entryButton.grid(row=ctr, column=2, sticky=(N, S, E, W), pady=2, padx=(0, 10))

    #     self.topFrame = Frame(self.master)
    #     self.topFrame.grid(column=0, row=0, sticky=(N, E, W))

    #     self.mainFrame = Frame(self.master)
    #     self.mainFrame.grid(column=0, row=1, sticky=(N, E, W), pady=(0, 20))

    #     # ***** Top Frame *****
    #     self.saveFileBtn = ttk.Button(
    #         self.topFrame, text="Save File", command=self.saveDataSetToFile)
    #     self.exitBtn = ttk.Button(
    #         self.topFrame, text="Exit", command=self.onExit)

    #     self.saveFileBtn.grid(row=0, column=1, sticky=(
    #         S, E, W, N), pady=15, padx=7.5)
    #     self.exitBtn.grid(row=0, column=2, sticky=(
    #         S, E, W, N), pady=15, padx=7.5)

    #     # ***** Main Frame *****
    #     self.nameLabel = ttk.Label(
    #         self.mainFrame, text="Names", font="Helvetica 16 bold")
    #     self.emailLabel = ttk.Label(
    #         self.mainFrame, text="Emails", font="Helvetica 16 bold")
    #     self.nameLabel.grid(row=0)
    #     self.emailLabel.grid(row=0, column=1)
    #     self.dataSet = self.loadDataSetFromFile()

    #     for ctr, name in enumerate(self.dataSet):
    #         ctr += 1
    #         self.name = name
    #         self.email = self.dataSet[name]
    #         self.entryName = name + "Name"
    #         self.entryEmail = name + "Email"

    #         self.entryName = ttk.Entry(
    #             self.mainFrame, font="Helvetica 12")
    #         self.entryName.insert(0, self.name)
    #         self.entryName.bind('<Return>', self.onEntryInteraction)
    #         self.entryName.bind('<Button-1>', self.onEntryInteraction)

    #         self.entryEmail = ttk.Entry(self.mainFrame, font="Helvetica 12")
    #         self.entryEmail.insert(0, self.email)
    #         self.entryEmail.bind('<Return>', self.onEntryInteraction)
    #         self.entryEmail.bind('<Button-1>', self.onEntryInteraction)

    #         self.entryButton = ttk.Button(self.mainFrame, text="Delete")

    #         self.entryName.grid(row=ctr, column=0, sticky=(
    #             N, S, E, W), pady=2, padx=(15, 7.5))
    #         self.entryEmail.grid(row=ctr, column=1, sticky=(
    #             N, S, E, W), pady=2, padx=(7.5, 15))
    #         self.entryButton.grid(row=ctr, column=2, sticky=(
    #             N, S, E, W), pady=2, padx=(0, 10))

    #     # ***** Scroll Bar *****
    #     self.scrollbar = ttk.Scrollbar(self.master)
    #     self.scrollbar.grid(column=6, row=1,  sticky=N+S+W)
      

    #     self.master.columnconfigure(0, weight=1)
    #     self.master.rowconfigure(1, weight=1)
    #     self.mainFrame.columnconfigure(0, weight=1)
    #     self.mainFrame.columnconfigure(1, weight=1)

    #     self.topFrame.columnconfigure(0, weight=2)
    #     self.topFrame.columnconfigure(3, weight=2)

    #     self.topFrame.columnconfigure(1, weight=1)
    #     self.topFrame.columnconfigure(2, weight=1)

    # def loadDataSetFromFile(self):
    #     try:
    #         with open('dataSet.json', 'r') as inputFile:
    #             dataSet = json.load(inputFile)
    #         return dataSet
    #     except FileNotFoundError:
    #         # TODO: Alert message file not found
    #         print("File not found!")
    #         dataSet = {}
    #         return dataSet

    # def saveDataSetToFile(self):
    #     print("File")
    #     with open('dataSet.json', 'w') as outfile:
    #         json.dump(self.dataSet, outfile, sort_keys=True,
    #                   indent=2, separators=(',', ': '))

    # def onExit(self):
    #     self.master.destroy()

    def onEntryInteraction(self, event):
        print(event.num)
        print(event.keycode)
        print(event.widget.get())
        self.master.focus()

        if event.num == 1:
            self.currentEntryVal = event.widget.get()
            # if self.currentEntryVal in self.dataSet:
            #     print("IN NAMMEE")
            #     self.entryType = "name"
            # else:
            #     print("IN EMMAILLLSS")
            #     self.entryType = "email"

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

    #     print("[CURRENT_VAL]" + self.currentEntryVal)
    #     print("[NEW_VAL]" + self.newEntryVal)

#  **** SCROLL BAR TEST *****
if __name__ == "__main__":
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("radiance")
    root.geometry("500x500+100+100")
    b = AppGui(root)
    root.mainloop()
        
root.mainloop()
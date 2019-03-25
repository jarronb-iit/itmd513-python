        self.searchFrame = Frame(self.master)
        self.searchFrame.pack(side=TOP, fill=X, anchor=NW)

        self.searchFrame.columnconfigure(1, weight=1)
        self.searchFrame.columnconfigure(2, weight=1)
        self.searchFrame.columnconfigure(3, weight=1)
        self.searchFrame.columnconfigure(4, weight=1)

        self.searchFrame.columnconfigure(0, weight=4)
        self.searchFrame.columnconfigure(5, weight=4)
    
    def onAddSearchSection(self):
        # Show Search Section

        self.searchResult = StringVar()

        self.addSearchLabel = ttk.Label(
            self.searchFrame, text="Search for Entry by Name or Email", font="Helvetica 12 bold")
        self.searchEntry = ttk.Entry(
            self.searchFrame, font="Helvetica 12")
        self.searchResultLabel = ttk.Label(
            self.searchFrame, text=self.searchResult, font="Helvetica 12 bold")
        self.searchEntryBtn = ttk.Button(
            self.searchFrame, text="Search", command=self.addNewEntry)

        self.addSearchLabel.grid(row=0, column=1, sticky=(
            N, E, W))
        self.searchEntry.grid(row=1, column=2, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.searchResultLabel.grid(row=1, column=3, sticky=(
            N, E, W))
        self.searchResultLabel.grid(row=1, column=4, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.searchEntryBtn.grid(row=1, column=4, sticky=(
            N, E, W), pady=15, padx=7.5)
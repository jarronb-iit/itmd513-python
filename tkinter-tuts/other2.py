frame = Frame(self.bottom_frame)
        frame.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)

        self.canvas = Canvas(frame, bg = 'pink')
        self.canvas.pack(side = RIGHT, fill = BOTH, expand = True)

        self.mailbox_frame = Frame(self.canvas, bg = 'purple')

        self.canvas_frame = self.canvas.create_window((0,0),
            window=self.mailbox_frame, anchor = NW)
        #self.mailbox_frame.pack(side = LEFT, fill = BOTH, expand = True)

        mail_scroll = Scrollbar(self.canvas, orient = "vertical", 
            command = self.canvas.yview)
        mail_scroll.pack(side = RIGHT, fill = Y)

        self.canvas.config(yscrollcommand = mail_scroll.set)

        self.mailbox_frame.bind("<Configure>", self.OnFrameConfigure)
        self.canvas.bind('<Configure>', self.FrameWidth)

    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
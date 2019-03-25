from tkinter import *


class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Delete Row")
        self.frameOne = Frame(self.master)
        self.frameOne.grid(row=0, column=0)

        self.frameTwo = Frame(self.master)
        self.frameTwo.grid(row=1, column=0)
        # The purpose of creating a "frameTwo" is to add scrollbar
        self.canvas = Canvas(self.frameTwo)
        self.listFrame = Frame(self.canvas)
        self.scrollb = Scrollbar(
            self.master, orient="vertical", command=self.canvas.yview)
        self.scrollb.grid(row=1, column=1, sticky="nsew")
        self.canvas["yscrollcommand"] = self.scrollb.set

        self.canvas.create_window((0, 0), window=self.listFrame, anchor="nw")
        self.listFrame.bind("<Configure>", self.AuxscrollFunction)
        self.scrollb.grid_forget()
        self.canvas.bind('<Configure>', self.FrameWidth)

        self.canvas.pack(side="left")
        self.frameThree = Frame(self.master)
        self.frameThree.grid(row=2, column=0)
        self.welcome = Button(self.frameOne, text="Welcome",
                              command=self.welcome_to, width=10)
        self.welcome.grid(row=0, column=0, columnspan=3)

    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def AuxscrollFunction(self, event):

        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"), width=500, height=750)

    def welcome_to(self):
        try:
            self.main()
            self.scrollb.grid(row=1, column=1, sticky="nsew")
        except ValueError:
            showerror("Not working")

    def main(self):
        self.welcome.grid_remove()
        menu = Menu(self.listFrame)
        self.master.config(menu=menu)
        # creating the menu bar object-File
        file = Menu(menu)
        # adding commands to File
        file.add_command(label="New")
        file.add_command(label="Load")
        file.add_command(label="Save")
        file.add_command(label="Save As")
        file.add_command(label="Exit", command=self.client_exit)
        # adding File to the Menu bar
        menu.add_cascade(label="File", menu=file)
        # Name and Description
        self.entry = Entry(self.listFrame)
        self.entry.grid(column=1, row=0, sticky="EW")
        nameLabel = Label(self.listFrame, text="NAME")
        nameLabel.grid(column=0, row=0)
        self.entry = Entry(self.listFrame)
        self.entry.grid(column=1, row=1, columnspan=8, sticky="EW")
        descriptionLabel = Label(self.listFrame, text="DESCRIPTION")
        descriptionLabel.grid(column=0, row=1)

        Box = Button(self.listFrame, text="Box", bg="white")
        Box.grid(column=0, row=2)
        Button1 = Button(self.listFrame, text="+",
                         command=self.combo, fg="green")
        Button1.grid(column=1, row=2, sticky="W")
        self.num = 10

    def client_exit(self):
        exit()

    def tryon(self):
        BurstCountButton = Button(self.listFrame, text="Button 1")
        BurstCountButton.grid(column=2, row=2)
        DelayLabel = Label(self.listFrame, text="Label 1")
        DelayLabel.grid(column=4, row=2)

        tryLabel = Label(self.listFrame, text="Label 2")
        tryLabel.grid(column=1, row=int(self.num), sticky="EW")
        self.entry = Entry(self.listFrame)
        self.entry.grid(column=2, row=int(self.num), sticky="EW")
        TimesLabel = Label(self.listFrame, text="Label 2")
        TimesLabel.grid(column=3, row=int(self.num))
        self.entry = Entry(self.listFrame)
        self.entry.grid(column=4, row=int(self.num), sticky="EW")
        var = StringVar()
        menu1 = OptionMenu(self.listFrame, var, "")
        menu1.config(width=10)
        menu1.grid(column=5, row=int(self.num))
        var.set("")
        andLabel = Label(self.listFrame, text="and")
        andLabel.grid(column=6, row=int(self.num))
        self.entry = Entry(self.listFrame)
        self.entry.grid(column=7, row=int(self.num), sticky="EW")
        menu2 = OptionMenu(self.listFrame, var, ")")
        menu2.config(width=10)
        menu2.grid(column=8, row=int(self.num))
        var.set("")
        closeButton = Button(self.listFrame, text="X", fg="red")
        closeButton.grid(column=9, row=int(self.num))
        self.num = self.num+1
        self.b = self.num

    def mbutton(self):
        global counter
        counter += 1
        label = Label(self.listFrame, text="tryon(%s)" % counter)
        label.config(text="tryon(%s)" % counter, fg="blue")
        label.grid(column=0, row=int(self.num))

    def combo(self):
        self.mbutton()
        self.tryon()


if __name__ == "__main__":
    counter = 0
    count_service = 0
    root = Tk()

    aplicacion = Window(root)
    root.mainloop()

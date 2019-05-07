'''
Jarron Bailey
Homework 13
Date: May 6th, 2019
Description:  Python program to input the number of each type of coin a user has in their possession and then compute and
display the total dollar and cents value of these coins. Solution must accommodate Quarter, Dime, Nickel, and Penny, Half-dollar and Dollar coins as well.
Solution must be robust against invalid inputs (i.e., negative value entered into any coin entry widget).
'''
try:
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import tkinter.messagebox
except ImportError:  # If Import error -> Try again
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import tkinter.messagebox


class AppGui(ttk.Frame):
    '''Class is responsible for the applications gui, a header frame and two content frames splitting th content'''

    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

        # Header Frame
        self.__headerFrame = ttk.Frame(self)
        self.__headerFrame.pack(side=TOP, fill=X, pady=15)
        self.__headerLabel = ttk.Label(
            self.__headerFrame, text="Change Counter", font="Helvetica 18 bold", anchor="center", relief="raised")
        self.__headerLabel.pack()

        # Content Frame
        self.__contentFrame = ttk.Frame(self)
        self.__contentFrame.pack(side=TOP, fill=BOTH, pady=15)
        self.__headerLabel = ttk.Label(
            self.__contentFrame, text="Enter the number of each coin type and hit, Compute:", font="Helvetica 16 bold", anchor="center")

        # Left side
        self.__leftFrame = ttk.Frame(self.__contentFrame)
        self.__leftFrame.pack(side=LEFT, padx=(50, 0))

        self.__quarterLabel = ttk.Label(
            self.__leftFrame, text="Quarters:", font="Helvetica 12 bold")
        self.__quarterEntry = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15)

        self.__dimesLabel = ttk.Label(
            self.__leftFrame, text="Dimes:", font="Helvetica 12 bold")
        self.__dimesEntry = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15)

        self.__nickelsLabel = ttk.Label(
            self.__leftFrame, text="Nickels:", font="Helvetica 12 bold")
        self.__nickelsEntry = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15)

        self.__penniesLabel = ttk.Label(
            self.__leftFrame, text="Pennies:", font="Helvetica 12 bold")
        self.__penniesEntry = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15)

        self.__halfDollarLabel = ttk.Label(
            self.__leftFrame, text="Half Dollars:", font="Helvetica 12 bold")
        self.__halfDollarEntry = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15)

        self.__dollarCoinsLabel = ttk.Label(
            self.__leftFrame, text="Dollar Coins:", font="Helvetica 12 bold")
        self.__dollarCoinsEntry = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15)

        self.__calculateButton = ttk.Button(self.__leftFrame, text="Calculate",
                                            command=self.__getInputs)

        # Layout
        self.__quarterLabel.grid(row=1, column=0)
        self.__quarterEntry.grid(row=1, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__dimesLabel.grid(row=2, column=0)
        self.__dimesEntry.grid(row=2, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__nickelsLabel.grid(row=3, column=0)
        self.__nickelsEntry.grid(row=3, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__penniesLabel.grid(row=4, column=0)
        self.__penniesEntry.grid(row=4, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__halfDollarLabel.grid(row=5, column=0)
        self.__halfDollarEntry.grid(row=5, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__dollarCoinsLabel.grid(row=6, column=0)
        self.__dollarCoinsEntry.grid(row=6, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__calculateButton.grid(row=7, column=0, columnspan=2, sticky=(
            N, S, E, W), pady=5)

        # Right side / Values
        self.__leftFrame = ttk.Frame(self.__contentFrame)
        self.__leftFrame.pack(side=LEFT, padx=(50, 0))

        self.__quarterLabelValue = ttk.Label(
            self.__leftFrame, text="Quarter values:", font="Helvetica 12 bold")
        self.__quartersResultVar = StringVar()
        self.__quartersResultVar.set("$0.00")
        self.__quarterEntryValue = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15, textvariable=self.__quartersResultVar, state="readonly")

        self.__dimesLabelValue = ttk.Label(
            self.__leftFrame, text="Dime values:", font="Helvetica 12 bold")
        self.__dimesResultVar = StringVar()
        self.__dimesResultVar.set("$0.00")
        self.__dimesEntryValue = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15, textvariable=self.__dimesResultVar, state="readonly")

        self.__nickelsLabelValue = ttk.Label(
            self.__leftFrame, text="Nickel values:", font="Helvetica 12 bold")
        self.__nickelsResultVar = StringVar()
        self.__nickelsResultVar.set("$0.00")
        self.__nickelsEntryValue = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15, textvariable=self.__nickelsResultVar, state="readonly")

        self.__penniesLabelValue = ttk.Label(
            self.__leftFrame, text="Penny values:", font="Helvetica 12 bold")
        self.__penniesResultVar = StringVar()
        self.__penniesResultVar.set("$0.00")
        self.__penniesEntryValue = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15, textvariable=self.__penniesResultVar, state="readonly")

        self.__halfDollarLabelValue = ttk.Label(
            self.__leftFrame, text="Half Dollar values:", font="Helvetica 12 bold")
        self.__halfDollarResultVar = StringVar()
        self.__halfDollarResultVar.set("$0.00")
        self.__halfDollarEntryValue = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15, textvariable=self.__halfDollarResultVar, state="readonly")

        self.__dollarCoinsLabelValue = ttk.Label(
            self.__leftFrame, text="Dollar Coin values:", font="Helvetica 12 bold")
        self.__dollarCoinsResultVar = StringVar()
        self.__dollarCoinsResultVar.set("$0.00")
        self.__dollarCoinsEntryValue = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15, textvariable=self.__dollarCoinsResultVar, state="readonly")

        self.__totalAmountLabel = ttk.Label(
            self.__leftFrame, text="Total change value:", font="Helvetica 14 bold")
        self.__totalAmountResultVar = StringVar()
        self.__totalAmountResultVar.set("$00.00")
        self.__totalAmountEntry = ttk.Entry(
            self.__leftFrame, font="Helvetica 12", width=15, textvariable=self.__totalAmountResultVar, state="readonly")

        # Layout
        self.__quarterLabelValue.grid(row=1, column=0)
        self.__quarterEntryValue.grid(row=1, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__dimesLabelValue.grid(row=2, column=0)
        self.__dimesEntryValue.grid(row=2, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__nickelsLabelValue.grid(row=3, column=0)
        self.__nickelsEntryValue.grid(row=3, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__penniesLabelValue.grid(row=4, column=0)
        self.__penniesEntryValue.grid(row=4, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__halfDollarLabelValue.grid(row=5, column=0)
        self.__halfDollarEntryValue.grid(row=5, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__dollarCoinsLabelValue.grid(row=6, column=0)
        self.__dollarCoinsEntryValue.grid(row=6, column=1, sticky=(
            N, S, E, W), pady=5)

        self.__totalAmountLabel.grid(row=7, column=0)
        self.__totalAmountEntry.grid(row=7, column=1, sticky=(
            N, S, E, W), pady=5)

    def __vaildateInt(self, number):
        '''Function validates an integer passed in as an string or number and returns valid or not and the number'''
        valid = False
        number.strip()
        if isinstance(number, str):
            try:
                number = int(number)
            except ValueError:
                valid = False
        if isinstance(number, int):
            if number < 0:
                valid = False
            else:
                valid = True

        return {"valid": valid, "number": number}

    def __getInputs(self):
        '''Function get the input from the entries and validates the number, if not valid error is returned'''
        # Quarters
        quarters = self.__quarterEntry.get()
        validationVars = self.__vaildateInt(quarters)
        valid = validationVars["valid"]
        if not valid:
            return tkinter.messagebox.showerror(
                "Invalid Entry", "Quarters must be a positive integer")
        quarters = validationVars["number"]

        # Dimes
        dimes = self.__dimesEntry.get()
        validationVars = self.__vaildateInt(dimes)
        valid = validationVars["valid"]
        if not valid:
            return tkinter.messagebox.showerror(
                "Invalid Entry", "Dimes must be a positive integer")
        dimes = validationVars["number"]

        # Nickels
        nickels = self.__nickelsEntry.get()
        validationVars = self.__vaildateInt(nickels)
        valid = validationVars["valid"]
        if not valid:
            return tkinter.messagebox.showerror(
                "Invalid Entry", "Nickels must be a positive integer")

        # Pennies
        pennies = validationVars["number"]
        pennies = self.__penniesEntry.get()
        validationVars = self.__vaildateInt(pennies)
        valid = validationVars["valid"]
        if not valid:
            return tkinter.messagebox.showerror(
                "Invalid Entry", "Pennies must be a positive integer")
        pennies = validationVars["number"]

        # Half dollar
        halfDollars = self.__halfDollarEntry.get()
        validationVars = self.__vaildateInt(halfDollars)
        valid = validationVars["valid"]
        if not valid:
            return tkinter.messagebox.showerror(
                "Invalid Entry", "Half dollars must be a positive integer")
        halfDollars = validationVars["number"]

        # Dollar coins
        dollarCoins = self.__dollarCoinsEntry.get()
        validationVars = self.__vaildateInt(dollarCoins)
        valid = validationVars["valid"]
        if not valid:
            return tkinter.messagebox.showerror(
                "Invalid Entry", "Dollar coins must be a positive integer")
        dollarCoins = validationVars["number"]
        print("[COINS AMOUNT]", quarters, dimes,
              nickels, pennies, halfDollars, dollarCoins)
        return self.__calculateMoney(quarters, dimes, nickels, pennies, halfDollars, dollarCoins)

    def __calculateMoney(self, quarters, dimes, nickels, pennies, halfDollars, dollarCoins):
        '''Function returns each coin value entered to the set values function'''
        quarters = float(quarters) * 0.25
        dimes = float(dimes) * 0.10
        nickels = float(nickels) * 0.05
        pennies = float(pennies) * 0.01
        halfDollars = float(halfDollars) * 0.50
        dollarCoins = float(dollarCoins) * 1.00
        total = quarters + dimes + nickels + pennies + halfDollars + dollarCoins
        print("[CALC]", quarters, dimes, nickels,
              pennies, halfDollars, dollarCoins, total)
        return self.__setEntryValues(quarters, dimes, nickels, pennies, halfDollars, dollarCoins, total)

    def __setEntryValues(self, quarters, dimes, nickels, pennies, halfDollars, dollarCoins, total):
        '''Function set the coins values to associated variable text'''
        self.__quartersResultVar.set("${:,.2f}".format(quarters))
        self.__dimesResultVar.set("${:,.2f}".format(dimes))
        self.__nickelsResultVar.set("${:,.2f}".format(nickels))
        self.__penniesResultVar.set("${:,.2f}".format(pennies))
        self.__halfDollarResultVar.set("${:,.2f}".format(halfDollars))
        self.__dollarCoinsResultVar.set("${:,.2f}".format(dollarCoins))
        self.__totalAmountResultVar.set("${:,.2f}".format(total))
        return print("Values set...")

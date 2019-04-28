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
    from functools import partial
    import re
    from datetime import datetime
    from PatientAccount import PatientAccount
    from Pharmacy import Pharmacy
    from Surgery import Surgery
except ImportError:  # If Import error -> Try again
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import tkinter.messagebox
    from functools import partial
    import re
    from datetime import datetime
    from PatientAccount import PatientAccount
    from Pharmacy import Pharmacy
    from Surgery import Surgery

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


class Page(ttk.Frame):
    '''
    Base class of an page, responsible for instantiating the PatientAccount, Surgery, and Pharmacy class
    as well as provide the base functions for the pages
    '''
    PatientAccountObj = PatientAccount()
    SurgeryObj = Surgery()
    PharmacyObj = Pharmacy()
    surgeriesDataset = SurgeryObj.getSurgeries()
    medicationsDataset = PharmacyObj.getMedications()

    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        '''Function is responsible for showing page'''
        self.lift()

    def onProductButtonClick(self, event, product, price):
        '''
        Function handles the toggling of the add/remove buttons for the products, and
        add the product to the charges accumulator or remove the product     
        '''
        buttonText = event.widget["text"]
        if buttonText == "Add":
            event.widget["text"] = "Remove"
            self.__buttonType = 1
            self.PatientAccountObj.setChargeToAccumulator(product, price)

        elif buttonText == "Remove":
            event.widget["text"] = "Add"
            self.__buttonType = 0
            self.PatientAccountObj.deleteChargeFromAccumulator(product)
    
    def representsInt(self, num):
        '''Functions returns if a number is a valid int or not'''
        try: 
            int(num)
            return True
        except ValueError:
            return False


class HomePage(Page):
    '''Class is responsible for the HomePage GUI'''
    def __init__(self, *args, **kwargs):
        '''Constructor builds and displays the HomePage widgets'''
        Page.__init__(self, *args, **kwargs)
    
        self.__nameResult = StringVar()
        self.__nameResult.set("Name Pending...")

        self.__dateOfBirthResult = StringVar()
        self.__dateOfBirthResult.set("Date of Birth Pending...")

        self.__daysSpentResult = StringVar()
        self.__daysSpentResult.set("Days in Hospital Pending...")

        self.__frame = Frame(self)
        self.__frame.pack(side=TOP, fill=BOTH, expand=True, pady=50)

        # Header/App title
        self.__headerLabel = ttk.Label(
            self.__frame, text="Welcome to IIT Patient Management System", font="Helvetica 22 bold", anchor="center")
        self.__letsStartWith = ttk.Label(
            self.__frame, text="Lets start with entering the patients details(Press enter to submit detail) ", font="Helvetica 16", anchor="center")

        # Name widgets
        self.__patientsNameLabel = ttk.Label(
            self.__frame, text="Pateint's name:", font="Helvetica 12")
        self.__patientsNameEntry = ttk.Entry(
            self.__frame, font="Helvetica 12", width=30)
        self.__patientsNameResultLabel = ttk.Label(
            self.__frame, textvariable=self.__nameResult, font="Helvetica 12", state="readonly", width=30, relief=RAISED)

        # Bindings
        self.__patientsNameEntry.insert(0, 'Patient Name...')
        self.__patientsNameEntry.bind("<FocusIn>", lambda args: self.__patientsNameEntry.delete('0', 'end'))
        self.__patientsNameEntry.bind('<Return>', self.__onNameEntry)

        # Date of Birth widgets
        self.__dateOfBirthLabel = ttk.Label(
            self.__frame, text="Date of Birth:", font="Helvetica 12")
        self.__dateOfBirthLabelEntry = ttk.Entry(
            self.__frame, font="Helvetica 12", width=30)
        self.__dateOfBirthResultLabel = ttk.Label(
            self.__frame, textvariable=self.__dateOfBirthResult, font="Helvetica 12", state="readonly", width=30, relief=RAISED)

        # Bindings
        self.__dateOfBirthLabelEntry.insert(0, 'Ex: mm-dd-yyyy')
        self.__dateOfBirthLabelEntry.bind("<FocusIn>", lambda args: self.__dateOfBirthLabelEntry.delete('0', 'end'))
        self.__dateOfBirthLabelEntry.bind('<Return>', self.__onDateOfBirthEntry)
     
        # Days spent in hospital widgets
        self.__daysSpentLabel = ttk.Label(
            self.__frame, text="Days in Hospital:", font="Helvetica 12")
        self.__daysSpentEntry = ttk.Entry(
            self.__frame, font="Helvetica 12", width=30)
        self.__daysSpentResultLabel = ttk.Label(
            self.__frame, textvariable=self.__daysSpentResult, font="Helvetica 12", state="readonly", width=30, relief=RAISED)

        # Bindings
        self.__daysSpentEntry.insert(0, 'Days in hospital...')
        self.__daysSpentEntry.bind("<FocusIn>", lambda args: self.__daysSpentEntry.delete('0', 'end'))
        self.__daysSpentEntry.bind('<Return>', self.__onDaysInHospital)

        # ***Widgets Layout***
        # Header
        self.__headerLabel.grid(row=0, column=1, columnspan=2, sticky=(
            N, E, W))
        self.__letsStartWith.grid(row=2, column=1, columnspan=2, sticky=(
            N, E, W), pady=10)

        # Name
        self.__patientsNameLabel.grid(row=3, column=1, sticky=(
            N, E, W))
        self.__patientsNameEntry.grid(row=4, column=1, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.__patientsNameResultLabel.grid(row=4, column=2, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))

        # Date of Birth
        self.__dateOfBirthLabel.grid(row=5, column=1, sticky=(
            N, E, W))
        self.__dateOfBirthLabelEntry.grid(row=6, column=1, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.__dateOfBirthResultLabel.grid(row=6, column=2, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))

        # Days spent in hospital
        self.__daysSpentLabel.grid(row=7, column=1, sticky=(
            N, E, W))
        self.__daysSpentEntry.grid(row=8, column=1, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))
        self.__daysSpentResultLabel.grid(row=8, column=2, sticky=(
            N, E, W), pady=2, padx=(15, 7.5))

        # Grid Column Configs
        self.__frame.columnconfigure(1, weight=1)
        self.__frame.columnconfigure(2, weight=1)

        self.__frame.columnconfigure(0, weight=4)
        self.__frame.columnconfigure(3, weight=4)
    
    def __onNameEntry(self, event):
        '''Function is responsible getting the name from the entry, validating, and passing the name to the patients account'''
        name = event.widget.get()
        isValidName = self.__validateName(name)
        if not isValidName:
            tkinter.messagebox.showerror(
                    "Invalid Entry", "Invalid characters entered, please reenter name")
            return
        self.PatientAccountObj.setPatientName(name)
        self.__nameResult.set(name)

    def __onDateOfBirthEntry(self, event):
        '''Function is responsible getting the Date of birth from the entry, validating, and passing the name to the patients account'''
        dateOfBirth = event.widget.get()
        isValidDateOfBirth = self.__validateDate(dateOfBirth)
        if not isValidDateOfBirth:
            tkinter.messagebox.showerror(
                    "Invalid Entry", "Invalid date, Format is MM-DD-YYYY and can't be a future date")
            return
        self.PatientAccountObj.setPatientDateOfBirth(dateOfBirth)
        self.__dateOfBirthResult.set(dateOfBirth)

    def __onDaysInHospital(self, event):
        '''
        Function is responsible getting the days in hospital from the entry, validating, and passing the name to the patients account
        '''
        daysSpent = event.widget.get()
        isDaysSpentValid = daysSpent.replace(".", "", 1).isdigit()
        try:
            if int(daysSpent) <= 0:
                    isDaysSpentValid = False
        except ValueError:
            pass
        if not isDaysSpentValid:
            tkinter.messagebox.showerror(
                    "Invalid Entry", "Invalid amount of days")
            return
        self.PatientAccountObj.setDaysSpentInHospital(daysSpent)
        self.__daysSpentResult.set(daysSpent)
    
    def __validateDate(self , date_string):
        '''Return if date is valid'''
        date_format = '%m-%d-%Y'
        try:
            date_obj = datetime.strptime(
                date_string, date_format).strftime('%m-%d-%Y')
            date_obj = date_obj.split('-')
            if datetime(int(date_obj[2]), int(
                    date_obj[0]), int(date_obj[1])) < datetime.now():
                return True
            else:
                raise ValueError

        except ValueError:
            return False
            
    def __validateName(self, name):
        '''Return if date is valid'''
        if re.match("^[a-zA-Z ]+$", name):
            return True
        else: 
            return False

class SurgeriesPage(Page):
    '''
    This class is responsible for displaying the SurgeriesPage widgets
    '''
    def __init__(self, *args, **kwargs):
        '''
        This constructor is responsible for initializing the SurgeryPage with the header and calling the function to create the 
        pages widgets
        '''
        Page.__init__(self, *args, **kwargs)
        self.__frame = Frame(self)
        self.__frame.pack(side=TOP, fill=BOTH, expand=True, pady=50)

        # Header
        self.__headerLabel = ttk.Label(
            self.__frame, text="Pick surgical operations", font="Helvetica 22 bold", anchor="center")

        # ***Widgets Layout***
        # Header
        self.__headerLabel.grid(row=0, column=1, columnspan=3, sticky=(
            N, E, W))

        # Surgeries frame
        self.__createSurgeriesFrame()

        # Grid Column Configs
        self.__frame.columnconfigure(1, weight=1)
        self.__frame.columnconfigure(2, weight=1)
        self.__frame.columnconfigure(3, weight=1)

        self.__frame.columnconfigure(0, weight=4)
        self.__frame.columnconfigure(4, weight=4)

    def __createSurgeriesFrame(self):
        '''Function creates the surgery listing widgets'''
        self.__surgeriesFrameHeader = ttk.Label(
            self.__frame, text="Surgeries", font="Helvetica 14 bold", anchor="center")
        # ***Creates widgets***
        self.__surgeriesTypeLabel = ttk.Label(
            self.__frame, text="Type", font="Helvetica 16 bold")
        self.__priceLabel = ttk.Label(
            self.__frame, text="Price", font="Helvetica 16 bold")

        # Creates list of surgeries
        for ctr, surgery in enumerate(self.surgeriesDataset):
            ctr += 3
            self.__surgery = surgery
            self.__price = self.surgeriesDataset[surgery]
            self.__priceFormatted = "${:,.2f}".format(self.__price)
            self.__entrySurgery = surgery + "Surgery"
            self.__entryPrice = surgery + "Price"

            # Surgery Entries
            self.__entrySurgery = ttk.Label(
                self.__frame, font="Helvetica 12", text=self.__surgery, relief=RAISED)

            # Price Entries
            self.__entryPrice = ttk.Label(
                self.__frame, font="Helvetica 12", text=self.__priceFormatted, relief=RAISED)

            # Add/Delete Buttons
            self.entryButton = ttk.Button(
                self.__frame, text="Add")
            self.entryButton.bind(
                "<ButtonPress-1>", partial(self.onProductButtonClick, product=self.__surgery, price=self.__price))

            # ***Widgets Layout***
            self.__surgeriesFrameHeader.grid(
                row=1, column=1, columnspan=2, pady=(50, 15))
            self.__surgeriesTypeLabel.grid(row=2, column=1)
            self.__entrySurgery.grid(row=ctr, column=1, sticky=(
                N, S, E, W), pady=2, padx=(15, 7.5))
            self.__priceLabel.grid(row=2, column=2)
            self.__entryPrice.grid(row=ctr, column=2, sticky=(
                N, S, E, W), pady=2, padx=(7.5, 15))
            self.entryButton.grid(row=ctr, column=3, sticky=(
                N, S, E, W), pady=2, padx=(0, 10))

            self.ctr = ctr


class MedicationsPage(Page):
    '''
    This class is responsible for displaying the MedicationsPage widgets
    '''

    def __init__(self, *args, **kwargs):
        '''
        This constructor is responsible for initializing the MedicationsPage with the header and calling the function to create the 
        pages widgets
        '''
        Page.__init__(self, *args, **kwargs)
        self.__nameResult = StringVar()
        self.__nameResult.set("Name Pending...")

        self.__frame = Frame(self)
        self.__frame.pack(side=TOP, fill=BOTH, expand=True, pady=50)

        # Header
        self.__headerLabel = ttk.Label(
            self.__frame, text="Pick medication prescriptions", font="Helvetica 22 bold", anchor="center")

        # ***Widgets Layout***
        # Header
        self.__headerLabel.grid(row=0, column=1, columnspan=3, sticky=(
            N, E, W))

        # Surgeries frame
        self.__createMedicationsFrame()

        # Grid Column Configs
        self.__frame.columnconfigure(1, weight=1)
        self.__frame.columnconfigure(2, weight=1)
        self.__frame.columnconfigure(3, weight=1)

        self.__frame.columnconfigure(0, weight=3)
        self.__frame.columnconfigure(4, weight=4)

        self.medicationsData = {
            "Synthroid (levothyroxine)": 38.07,
            "Crestor (rosuvastatin)": 500.19,
            "Ventolin HFA (albuterol)": 50.00,
            "Nexium (esomeprazole)": 238.12,
            "Advair Diskus (fluticasone)": 16.00
        }

    def __createMedicationsFrame(self):
        '''Function creates the medications listing widgets'''
        self.__medicationsFrameHeader = ttk.Label(
            self.__frame, text="Medications", font="Helvetica 14 bold", anchor="center")

        # ***Creates widgets***
        self.__medicationsTypeLabel = ttk.Label(
            self.__frame, text="Type", font="Helvetica 16 bold")
        self.__priceLabel = ttk.Label(
            self.__frame, text="Price", font="Helvetica 16 bold")

        # Creates list of medication
        for ctr, medication in enumerate(self.medicationsDataset):
            ctr += 3
            self.__medication = medication
            self.__price = self.medicationsDataset[medication]
            self.__priceFormatted = "${:,.2f}".format(self.__price)
            self.__entryMedication = medication + "Medication"
            self.__entryPrice = medication + "Price"

            # Medication Entries
            self.__entryMedication = ttk.Label(
                self.__frame, font="Helvetica 12", text=self.__medication, relief=RAISED)

            # Price Entries
            self.__entryPrice = ttk.Label(
                self.__frame, font="Helvetica 12", text=self.__priceFormatted, relief=RAISED)

            # Add/Delete Buttons
            self.entryButton = ttk.Button(
                self.__frame, text="Add")
            self.entryButton.bind(
                "<ButtonPress-1>", partial(self.onProductButtonClick, product=self.__medication, price=self.__price))

            # ***Widgets Layout***
            self.__medicationsFrameHeader.grid(
                row=1, column=1, columnspan=2, pady=(50, 15))
            self.__medicationsTypeLabel.grid(row=2, column=1)
            self.__entryMedication.grid(row=ctr, column=1, sticky=(
                N, S, E, W), pady=2, padx=(15, 7.5))
            self.__priceLabel.grid(row=2, column=2)
            self.__entryPrice.grid(row=ctr, column=2, sticky=(
                N, S, E, W), pady=2, padx=(7.5, 15))
            self.entryButton.grid(row=ctr, column=3, sticky=(
                N, S, E, W), pady=2, padx=(0, 10))

            self.ctr = ctr


class BillingPage(Page):
    '''
    This class is responsible for displaying the BillingsPage widgets
    '''

    def __init__(self, *args, **kwargs):
        '''
        This constructor is responsible calling the function to create the BillingsPage
        '''
        Page.__init__(self, *args, **kwargs)

        # Billing frame
        self.__createBillingsFrame()

    def __createBillingsFrame(self):
        '''Function created all the BillingsPage widgets and displays them'''
        # ***** Initializing *****
        self.ctr = 0
        # Data
        self.__chargesAccumulator = self.PatientAccountObj.getChargesAccumulator()
        self.__chargesAccumulatorTotal = self.PatientAccountObj.getChargesAccumulatorTotal()
        self.__chargesAccumulatorTotalFormatted = "${:,.2f}".format(
            self.__chargesAccumulatorTotal)
        self.__patientName = self.PatientAccountObj.getPatientName()
        self.__daysSpent = self.PatientAccountObj.getDaysSpentInHospital()
        self.__patientDateOfBirth = self.PatientAccountObj.getPatientDateOfBirth()

        # Initializing frame
        self.__frame = VerticalScrolledFrame(self)
        self.__frame.pack(side=TOP, fill=BOTH, expand=True, pady=50)

        # Header
        self.__headerLabel = ttk.Label(
            self.__frame, text="Review billing and proceed to checkout", font="Helvetica 22 bold", anchor="center")

        # ***Widgets Layout***
        # Header
        self.__headerLabel.grid(row=0, column=1, columnspan=3, sticky=(
            N, E, W))

        self.__billingsFrameHeader = ttk.Label(
            self.__frame, text="Patient: {} Billings".format(self.__patientName), font="Helvetica 14 bold", anchor="center")

        # ***Creates widgets***
        self.__billingsTypeLabel = ttk.Label(
            self.__frame, text="Product", font="Helvetica 16 bold")
        self.__priceLabel = ttk.Label(
            self.__frame, text="Price", font="Helvetica 16 bold")

        if not self.__patientName or len(self.__chargesAccumulator) <= 1 or self.__daysSpent == 0 or not        self.__patientDateOfBirth:
            self.__errorLabel = ttk.Label(
            self.__frame, text="Must enter patient details, and select at minimun one product", font="Helvetica 16 bold")
            self.__errorLabel.grid(row=2, column=2, sticky=(N, S, E, W), pady=(100, 0))
            return 
            
        # Create List of Bills
        for ctr, product in enumerate(self.__chargesAccumulator):
            ctr += 3
            self.__product = product
            self.__price = self.__chargesAccumulator[product]
            self.__priceFormatted = "${:,.2f}".format(self.__price)
            self.__entryProduct = product + "Product"
            self.__entryPrice = product + "Price"

            # Product Entries
            self.__entryProduct = ttk.Label(
                self.__frame, font="Helvetica 12", text=self.__product, relief=RAISED)

            # Price Entries
            self.__entryPrice = ttk.Label(
                self.__frame, font="Helvetica 12", text=self.__priceFormatted, relief=RAISED)

            # ***Widgets Layout***
            self.__billingsFrameHeader.grid(
                row=1, column=1, columnspan=2, pady=(50, 15))
            self.__billingsTypeLabel.grid(row=2, column=1)
            self.__entryProduct.grid(row=ctr, column=1, sticky=(
                N, S, E, W), pady=2, padx=(15, 7.5))
            self.__priceLabel.grid(row=2, column=2)
            self.__entryPrice.grid(row=ctr, column=2, sticky=(
                N, S, E, W), pady=2, padx=(7.5, 15))

            self.ctr = ctr

        # Total Entry
        self.__entryTotal = ttk.Label(
            self.__frame, font="Helvetica 12 bold", text="Total Charges: {}".format(self.__chargesAccumulatorTotalFormatted), relief=RAISED)

        self.__entryTotal.grid(row=self.ctr+1, column=1, columnspan=2, sticky=(
            N, S, E, W), pady=(20, 10), padx=(10))
        
        # Total Entry
        self.__exitButton = ttk.Button(
            self.__frame, text="Exit", command=self.__onExit)

        self.__exitButton.grid(row=self.ctr+2, column=1, columnspan=2, sticky=(
            N, S, E, W), pady=(20, 10), padx=(10))

        # Grid Column Configs
        self.__frame.columnconfigure(1, weight=1)
        self.__frame.columnconfigure(2, weight=1)

        self.__frame.columnconfigure(0, weight=3)
        self.__frame.columnconfigure(3, weight=3)

    def refreshFrame(self):
        '''Function destroys and rebuilds the Billings Page in order to refresh its data'''
        try: 
            self.__frame.destroy()
            self.__createBillingsFrame()
        except:
            pass

    def __onExit(self):
        '''Function exit the program by destroy the master frame'''
        self.master.master.destroy()
            

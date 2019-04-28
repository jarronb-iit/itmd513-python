'''
Jarron Bailey
Homework 11
Date: May 6th, 2019
Description: This program is to present a GUI that computes a patient’s bill for a hospital stay.
A GUI that allows the user to enter a type of surgery and a type of medication, and check the patient 
out of the hospital. When the patient checks out, the total charges should be displayed in a Window 
format (GUI Interface).
'''

try:
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    from AppGui import HomePage
    from AppGui import SurgeriesPage
    from AppGui import MedicationsPage
    from AppGui import BillingPage
except ImportError:  # If Import error -> Try again
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    from AppGui import HomePage
    from AppGui import SurgeriesPage
    from AppGui import MedicationsPage
    from AppGui import BillingPage


class MainView(ttk.Frame):
    '''
    This class is responsible for instantiating the AppGui components
    and run the applications GUI interface
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor initializes the application's pages and bottom button frame
        for navigating between each page
        '''
        ttk.Frame.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("Bailey, Jarron - Spring 2019 Final")
        self.p1 = HomePage(self)
        self.p2 = SurgeriesPage(self)
        self.p3 = MedicationsPage(self)
        self.p4 = BillingPage(self)

        self.buttonframe = ttk.Frame(self)
        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.buttonframe.pack(side="top", fill="x", expand=False)

        self.p1.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p4.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.b1 = ttk.Button(
            self.buttonframe, text="Patient Details", command=self.p1.lift)
        self.b2 = ttk.Button(
            self.buttonframe, text="Surgeries", command=self.p2.lift)
        self.b3 = ttk.Button(
            self.buttonframe, text="Medications", command=self.p3.lift)
        self.b4 = ttk.Button(self.buttonframe, text="Checkout",
                             command=self.refreshBillings)

        self.b1.pack(side="left")
        self.b2.pack(side="left")
        self.b3.pack(side="left")
        self.b4.pack(side="left")

        self.p1.show()

    def refreshBillings(self):
        '''
        Function is responsible for calling the Billings page refresh method, and
        showing the Billings Page
        '''
        self.p4.refreshFrame()
        self.p4.lift()
        return print("Billings page refreshed")


# Run Main program with themes, if fail -> no thememing
if __name__ == "__main__":
    try:
        root = tk.ThemedTk()
        root.get_themes()
        root.set_theme("radiance")
    except:
        root = Tk()
    finally:
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        main = MainView(root)
        main.pack(side="top", fill="both", expand=True)
        root.geometry("700x500+100+100")
        root.mainloop()

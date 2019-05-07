'''
Jarron Bailey
Homework 12
Date: April 29nd, 2019
Description:  Python program to input the number of each type of coin a user has in their possession and then compute and
display the total dollar and cents value of these coins. Solution must accommodate Quarter, Dime, Nickel, and Penny, Half-dollar and Dollar coins as well.
Solution must be robust against invalid inputs (i.e., negative value entered into any coin entry widget).
'''
try:
    from AppGui import AppGui
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import tkinter.messagebox
except ImportError:  # If Import error -> Try again
    from AppGui import AppGui
    from tkinter import *
    from tkinter import ttk
    from ttkthemes import themed_tk as tk
    import tkinter.messagebox


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
        main = AppGui(root)
        main.pack(side="top", fill="both", expand=True)
        root.geometry("700x350+100+100")
        root.mainloop()

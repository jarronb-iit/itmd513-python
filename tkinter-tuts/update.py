from tkinter import *

font1 = ("Helvetica", 12)

root = Tk()
root.geometry('100x50+20+20')

mainframe = Frame(root)
mainframe.grid(column=1000, row=1000, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

best = StringVar()
best.set('start')
label1 = Label(mainframe, textvariable=best,
               bg='#321000', fg='#000fff000', font=font1)
label1.grid()


def run(n=0, master=mainframe):
    best.set('test # %d' % (n))
    n += 1
    if n <= 10:
        mainframe.after(1000, run, n, master)


but1 = Button(text="RUN", command=run)
but1.grid()
root.mainloop()

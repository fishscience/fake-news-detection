##SID 2040885
##Team Name: Global Pandas

from tkinter import *
import tkinter as tk


class ABC(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        # don't assume that self.parent is a root window.
        # instead, call `winfo_toplevel to get the root window
        self.winfo_toplevel().title("Freeky")

        # this adds something to the frame, otherwise the default
        # size of the window will be very small
        label = Entry(self)
        label.pack(side="top", fill="x")


root= tk.Tk()
abc = ABC(root)

bg = PhotoImage(file = "bg375-667b.png")

canvas1 = tk.Canvas(root, width = 375, height = 667)
canvas1.pack()

label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)


def FactCheck ():
    x1 = entry1.get()
    analyse_input = x1

def Clear ():
    cleartext = 0

button1 = tk.Button(text='Fact check now', command=FactCheck)
canvas1.create_window(200, 280, window=button1)

button2 = tk.Button(text='Clear', command=Clear)
canvas1.create_window(200, 615, window=button2)


root.mainloop()

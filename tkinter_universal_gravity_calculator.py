# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.


import tkinter
from tkinter import font
import random


class App():
    '''Its an app.'''
    tk = tkinter.Tk()
    G = 6.67e-11

    def __init__(self):
        default_font = tkinter.font.nametofont("TkDefaultFont")
        default_font.configure(size=18)
        self.tk.title("Magic Universal Gravity Calculator")
        self.instructions = tkinter.Label(self.tk, text="Type In Your Values Below", fg="blue")
        self.instructions.grid(row=1, column=1, columnspan=4, sticky='ew')
        self.answer = tkinter.StringVar()

        self.m1 = tkinter.StringVar()
        self.m1_l = tkinter.Label(self.tk, text="M_1 (kg)", fg="black")
        self.m1_l.grid(row=2, column=1, columnspan=1, sticky='ew')
        self.m1_e = tkinter.Entry(self.tk, textvariable=self.m1, highlightcolor="blue", font="TkDefaultFont", bg="white", fg="black")
        self.m1_e.grid(row=2, column=2, columnspan=3, sticky='ew')

        self.m2 = tkinter.StringVar()
        self.m2_l = tkinter.Label(self.tk, text="M_2 (kg)", fg="black")
        self.m2_l.grid(row=3, column=1, columnspan=1, sticky='ew')
        self.m2_e = tkinter.Entry(self.tk, textvariable=self.m2, highlightcolor="blue", font="TkDefaultFont", bg="white", fg="black")
        self.m2_e.grid(row=3, column=2, columnspan=3, sticky='ew')

        self.r = tkinter.StringVar()
        self.r_l = tkinter.Label(self.tk, text="r (m)", fg="black")
        self.r_l.grid(row=4, column=1, columnspan=1, sticky='ew')
        self.r_e = tkinter.Entry(self.tk, textvariable=self.r, highlightcolor="blue", font="TkDefaultFont", bg="white", fg="black")
        self.r_e.grid(row=4, column=2, columnspan=3, sticky='ew')

        self.go = tkinter.Button(self.tk, text="Calculate!", bg="white", activeforeground="white",
                                 activebackground="blue", highlightbackground="blue",
                                 command=lambda: self.answer.set(self.calculate()))
        self.go.grid(row=5, column=1, columnspan=4, sticky='ew')
        photo = tkinter.PhotoImage(file="images/parker_logo.gif")
        self.image = tkinter.Label(self.tk, image=photo, bg="white")
        self.image.photo = photo
        self.image.grid(row=6, column=1, columnspan=4, sticky='ew')
        self.result = tkinter.Label(self.tk, textvariable=self.answer, bg="white", fg="black")
        self.result.grid(row=7, column=1, columnspan=4, sticky='ew')

    def calculate(self):
        try:
            m1 = float(self.m1.get())
        except ValueError:
            return "m1 isn't a number"
        try:
            m2 = float(self.m2.get())
        except ValueError:
            return "m2 isn't a number"
        try:
            r = float(self.r.get())
            assert r != 0
        except ValueError:
            return "r isn't a number"
        except AssertionError:
            return "Radius != 0 !!"
        # - Make exceptions for division by zero and type conversion errors.
        # - When "Calculate" is pushed, the result is displayed.  Yay!
        # - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
        F = self.G * (m1 * m2) / r ** 2
        return "F_g = " + str(F) + " kg"


if __name__ == '__main__':
    App().tk.mainloop()

    # Three modifications:
    # Font size
    # Image
    # Font Color Blue

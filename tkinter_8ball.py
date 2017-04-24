# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller

# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.


# Your program will have the following properties:

# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings.
# (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])


# - Add THREE or more other style modifications to make your app unique
# (font family, font size, color, padding, image, borders, justification,whatever you can find in tkinter library etc.)
#  Make a comment at the top or bottom of your code to tell me your 3 things you did.
# (Just to help me out in checking your assignment)

import tkinter
from tkinter import font
import random


class App():
    '''Its an app.'''
    tk = tkinter.Tk()
    answers = ["Yes", "No", "Most Likely", "Definitely", "Maybe", "Probably", "Definitely Not", "Absolutely", "No Way", "I don't know"]

    def __init__(self):
        default_font = tkinter.font.nametofont("TkDefaultFont")
        default_font.configure(size=18)
        self.tk.title("Magic 8-Ball")
        self.instructions = tkinter.Label(self.tk, text="Type In Your Question Below", fg="blue")
        self.instructions.grid(row=1, column=1, columnspan=4, sticky='ew')
        self.question = tkinter.StringVar()
        self.answer = tkinter.StringVar()
        self.entry = tkinter.Entry(self.tk, textvariable=self.question, font="TkDefaultFont", bg="white", fg="black")
        self.entry.grid(row=2, column=1, columnspan=4, sticky='ew')
        self.go = tkinter.Button(self.tk, text="Click Me",
                                 command=lambda: self.answer.set(self.answers[random.randrange(len(self.answers))]))
        self.go.grid(row=3, column=1, columnspan=4, sticky='ew')
        photo = tkinter.PhotoImage(file="images/8_ball.gif")
        self.image = tkinter.Label(self.tk, image=photo)
        self.image.photo = photo
        self.image.grid(row=4, column=1, columnspan=4, sticky='ew')
        self.result = tkinter.Label(self.tk, textvariable=self.answer, bg="black", fg="white")
        self.result.grid(row=5, column=1, columnspan=4, sticky='ew')


if __name__ == '__main__':
    App().tk.mainloop()

    # Three modifications:
    # Font size
    # Image
    # Font Color Blue

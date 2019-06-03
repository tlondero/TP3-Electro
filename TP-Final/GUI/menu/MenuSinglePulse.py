import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

class MenuSinglePulse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.insertSingPulseParamText = tk.Label(
            self, text="Insert the single pulse parameters",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.insertSingPulseParamText.grid(row=0, column=0, columnspan=6, sticky=N+E+W)

    def focus(self):
        pass
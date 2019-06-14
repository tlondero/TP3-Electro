import tkinter as tk
from tkinter import *
import config

class MenuMaths(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(self, text="This is the maths menu.", font=config.SMALL_FONT, bg="#ffe4c4")
        self.title.pack(side=TOP, fill=BOTH, expand=True)

    ######################################
    #   Reset Buttons' Relief Function   #
    ######################################

    def resetButtons(self):
        pass

    def focus(self):
        pass
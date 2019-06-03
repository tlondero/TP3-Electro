import tkinter as tk
from tkinter import *
import config

class CurveZerosAndPoles(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(self, text="This is the Zeros and Poles curve.", font=config.LARGE_FONT, bg="#ffffff")
        self.title.pack(side=TOP, fill=BOTH, expand=True)

    def focus(self):
        pass
import tkinter as tk
from tkinter import *
import config

from menu.MenuParameters import MenuParameters
from menu.MenuInputSignal import MenuInputSignal 
from menu.MenuMaths import MenuMaths

from menu.MenuFirstOrder import MenuFirstOrder
from menu.MenuSecondOrder import MenuSecondOrder

from menu.MenuSinewave import MenuSinewave
from menu.MenuSinglePulse import MenuSinglePulse
from menu.MenuPeriodicPulse import MenuPeriodicPulse

menus = [
    MenuParameters,
    MenuInputSignal,
    MenuMaths
]

class MenuMain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.buttonParameters = tk.Button(
            self, width=17, text="Parameters", 
            font=config.SMALL_FONT, bg="#ffe4c4", relief=FLAT, 
            command=self.buttonParametersPressed)

        self.buttonInputSignal = tk.Button(
            self, width=17, text="Input Signal",
            font=config.SMALL_FONT, bg="#fff0bc", command=self.buttonInputSignalPressed)

        self.buttonMaths = tk.Button(
            self, width=17, text="Maths",
            font=config.SMALL_FONT, bg="#fff0bc", command=self.buttonMathsPressed)
        
        self.buttonParameters.grid( row=0, column=0, ipadx=3, sticky = W)
        self.buttonInputSignal.grid(row=0, column=1, ipadx=3)
        self.buttonMaths.grid(      row=0, column=2, ipadx=3, sticky = E)

        self.buttonSimulate = tk.Button(
            self, width=36, text="Simulate",
            font=config.SMALL_FONT, background="#fff0bc", command=self.buttonSimulatePressed)

        self.buttonSimulate.grid(row=2, column=0, columnspan=3, pady=12, sticky=S)

        self.containMenu = tk.Frame(self)
        self.containMenu.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

        self.menus = {}

        for menu in menus:
            self.menus[menu] = menu(self.containMenu, self)
            self.menus[menu].grid_propagate(True)
            self.menus[menu].grid(row=0, column=0, sticky=E+W+N+S)
            self.menus[menu].config(bg="#ffe4c4")
        
        self.showMenu(MenuParameters)

    #Menu managing functions
    
    def showMenu(self, menu):
        self.menus[menu].focus()
        menu = self.menus[menu]
        menu.tkraise()
        self.menu = menu

    def getCurrentMenu(self):
        return self.menu

    #Buttons' callback functions
    
    def buttonParametersPressed(self):
        self.buttonParameters.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonInputSignal.config(relief=RAISED, bg="#fff0bc")
        self.buttonMaths.config(      relief=RAISED, bg="#fff0bc")
        self.showMenu(MenuParameters)

    def buttonInputSignalPressed(self):
        self.buttonParameters.config( relief=RAISED, bg="#fff0bc")
        self.buttonInputSignal.config(relief=FLAT,   bg="#ffe4c4")
        self.buttonMaths.config(      relief=RAISED, bg="#fff0bc")
        self.showMenu(MenuInputSignal)

    def buttonMathsPressed(self):
        self.buttonParameters.config( relief=RAISED, bg="#fff0bc")
        self.buttonInputSignal.config(relief=RAISED, bg="#fff0bc")
        self.buttonMaths.config(      relief=FLAT,   bg="#ffe4c4")
        self.showMenu(MenuMaths)

    def buttonSimulatePressed(self):
        self.menus[MenuInputSignal].getCurrentSignalMenu().updateSignal()
        self.controller.curveFrame.getCurrentCurve().simulate()
        for menu in menus:
            self.menus[menu].resetButtons()

    def focus(self):
        pass
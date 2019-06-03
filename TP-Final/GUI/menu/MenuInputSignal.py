import tkinter as tk
from tkinter import *
import config

from menu.MenuSinewave import MenuSinewave
from menu.MenuSinglePulse import MenuSinglePulse
from menu.MenuPeriodicPulse import MenuPeriodicPulse

signalMenus = [
    MenuSinewave,
    MenuSinglePulse,
    MenuPeriodicPulse
]

class MenuInputSignal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        ####################################
        #   Input Signal Inline Selector   #
        ####################################

        # Widgets Definition
        self.selectInputSignalText = tk.Label(
            self, width=30, text="Select the input signal", font=config.SMALL_FONT, bg="#ffe4c4")
        
        self.buttonSinewave = tk.Button(
            self, width=12, text="Sinewave",
            font=config.SMALL_FONT, bg="#fff0bc", command=self.buttonSinewavePressed)
        self.buttonSinglePulse = tk.Button(
            self, width=12, text="Single Pulse",
            font=config.SMALL_FONT, bg="#fff0bc", command=self.buttonSinglePulsePressed)
        self.buttonPeriodicPulse = tk.Button(
            self, width=12, text="Periodic Pulse",
            font=config.SMALL_FONT, bg="#fff0bc", command=self.buttonPeriodicPulsePressed)

        # Widgets Placement
        self.selectInputSignalText.grid(row=0, column=0, columnspan=3, ipady=5)

        self.buttonSinewave.grid(     row=1, column=0, sticky=W)
        self.buttonSinglePulse.grid(  row=1, column=1)
        self.buttonPeriodicPulse.grid(row=1, column=2, sticky=E)

        ##########################################
        #   Signal Menus Containers Definition   #
        ##########################################

        self.containSignalMenu = tk.Frame(self)
        self.containSignalMenu.grid(row=2, column=0, columnspan=3, sticky = E + W + N + S)

        self.signalMenus = {}

        for signalMenu in signalMenus:
            self.signalMenus[signalMenu] = signalMenu(self.containSignalMenu, self)
            self.signalMenus[signalMenu].grid_propagate(True)
            self.signalMenus[signalMenu].grid(row=0, column=0, sticky=E + W + N + S)
     
    #######################################
    #   Signal Menus Managing Functions   #
    #######################################

    def showSignalMenu(self, signalMenu):
        self.signalMenus[signalMenu].focus()
        signalMenu = self.signalMenus[signalMenu]
        signalMenu.tkraise()
        self.signalMenu = signalMenu

    def getCurrentSignalMenu(self):
        return self.signalMenu

    ###############################################
    #   Input Signal Buttons' Callback Functions  #
    ###############################################

    def buttonSinewavePressed(self):
        self.buttonSinewave.config(     relief=SUNKEN, bg="#ffe4c4")
        self.buttonSinglePulse.config(  relief=RAISED, bg="#fff0bc")
        self.buttonPeriodicPulse.config(relief=RAISED, bg="#fff0bc")
        self.showSignalMenu(MenuSinewave)

    def buttonSinglePulsePressed(self):
        self.buttonSinewave.config(     relief=RAISED, bg="#fff0bc")
        self.buttonSinglePulse.config(  relief=SUNKEN, bg="#ffe4c4")
        self.buttonPeriodicPulse.config(relief=RAISED, bg="#fff0bc")
        self.showSignalMenu(MenuSinglePulse)

    def buttonPeriodicPulsePressed(self):
        self.buttonSinewave.config(     relief=RAISED, bg="#fff0bc")
        self.buttonSinglePulse.config(  relief=RAISED, bg="#fff0bc")
        self.buttonPeriodicPulse.config(relief=SUNKEN, bg="#ffe4c4")
        self.showSignalMenu(MenuPeriodicPulse)

    def focus(self):
        pass
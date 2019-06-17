import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

class MenuFirstOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, width=55, text="Insert the first order parameters",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.title.grid(row=0, column=0, columnspan=5, ipadx=3, ipady=5, sticky=N+E+W)

        #################################
        #   Frequency Inline Selector   #
        #################################

        # Widgets Definition
        self.labelFrequency = tk.Label(self, width=15, text="Cutoff Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryFrequency = tk.Entry(self, width=5)

        self.HzUnitButton = tk.Button( self, width=8, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitButtonPressed)
        self.kHzUnitButton = tk.Button(self, width=8, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitButtonPressed)
        self.MHzUnitButton = tk.Button(self, width=8, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitButtonPressed)

        # Widgets Placement
        self.labelFrequency.grid(row=1, column=0, sticky=W, ipady=10)
        self.entryFrequency.grid(row=1, column=1, sticky=E, ipadx=10)

        self.HzUnitButton.grid( row=1, column=2)
        self.kHzUnitButton.grid(row=1, column=3)
        self.MHzUnitButton.grid(row=1, column=4)

        ######################################
        #   BandWidth Gain Inline Selector   #
        ######################################
        
        # Widgets Definition
        self.labelGainBW = tk.Label(self, width=15, text="BandWidth Gain", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryGainBW = tk.Entry(self, width=5)
        self.buttonGainBW = tk.Button(self, width=8, text="Send", font=config.SMALL_FONT, command=self.buttonGainBWPressed)

        # Widgets Placement
        self.labelGainBW.grid( row=2, column=0, sticky=W, ipady=10)
        self.entryGainBW.grid( row=2, column=1, sticky=E, ipadx=10)
        self.buttonGainBW.grid(row=2, column=2)

        ###################################
        #   Filter Type Inline Selector   #
        ###################################

        # Widgets Definition
        self.labelFilterType = tk.Label(self, width=15, text="Filter Type", font=config.SMALL_FONT, bg="#ffe4c4")

        self.buttonLowPass = tk.Button(
            self, width=8, text="Low Pass", font=config.SMALL_FONT, command=self.buttonLowPassPressed)
        self.buttonHighPass =tk.Button(
            self, width=8, text="High Pass",font=config.SMALL_FONT, command=self.buttonHighPassPressed)
        self.buttonAllPass = tk.Button(
            self, width=8, text="All Pass", font=config.SMALL_FONT, command=self.buttonAllPassPressed)

        # Widgets Placement
        self.labelFilterType.grid(row=3, column=0, sticky=W, ipady=10)

        self.buttonLowPass.grid( row=3, column=2)
        self.buttonHighPass.grid(row=3, column=3)
        self.buttonAllPass.grid( row=3, column=4)

    #################################################
    #   Frequency Unit Buttons' Callback Functions  #
    #################################################

    def HzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=FLAT,   bg="#ffe4c4")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        try:
            dictInput["frequencyValue"] = float(self.entryFrequency.get())
        except(ValueError):
            self.title.config(text="Please insert a float cutoff frequency value", fg="#ff0000")
            self.HzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Insert the first order parameters", fg="#000000")

        dictInput["frequencyUnit"] = "Hz"
        dictInput["frequencyUnitFactor"] = 1

    def kHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        try:
            dictInput["frequencyValue"] = float(self.entryFrequency.get())
        except(ValueError):
            self.title.config(text="Please insert a float cutoff frequency value", fg="#ff0000")
            self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Insert the first order parameters", fg="#000000")

        dictInput["frequencyUnit"] = "kHz"
        dictInput["frequencyUnitFactor"] = 1000

    def MHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")

        try:
            dictInput["frequencyValue"] = float(self.entryFrequency.get())
        except(ValueError):
            self.title.config(text="Please insert a float cutoff frequency value", fg="#ff0000")
            self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Insert the first order parameters", fg="#000000")

        dictInput["frequencyUnit"] = "MHz"
        dictInput["frequencyUnitFactor"] = 1000000

    ##############################################
    #   Filter Type Buttons' Callback Functions  #
    ##############################################

    def buttonLowPassPressed(self):
        self.buttonLowPass.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonHighPass.config(relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config( relief=RAISED, bg="#f0f0f0")
        dictInput["filterType"] = "Low Pass"
    
    def buttonHighPassPressed(self):
        self.buttonLowPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config(relief=FLAT,   bg="#ffe4c4")
        self.buttonAllPass.config( relief=RAISED, bg="#f0f0f0")
        dictInput["filterType"] = "High Pass"

    def buttonAllPassPressed(self):
        self.buttonLowPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config(relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config( relief=FLAT,   bg="#ffe4c4")
        dictInput["filterType"] = "All Pass"
    
    ###############################################
    #   Bandwidth Gain Button Callback Function   #
    ###############################################

    def buttonGainBWPressed(self):
        self.buttonGainBW.config(relief=FLAT, bg="#ffe4c4")
        try:
            dictInput["gainBW"] = float(self.entryGainBW.get())
        except(ValueError):
            self.title.config(text="Please insert a float bandwidth gain value", fg="#ff0000")
            self.buttonGainBW.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Insert the first order parameters", fg="#000000")

    ######################################
    #   Reset Buttons' Relief Function   #
    ######################################

    def resetButtons(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        self.buttonLowPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config(relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config( relief=RAISED, bg="#f0f0f0")

        self.buttonGainBW.config(relief=RAISED, bg="#f0f0f0")

    def focus(self):
        pass
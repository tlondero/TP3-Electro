import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

class MenuSecondOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.insertSOParamText = tk.Label(
            self, width=55, text="Insert the second order parameters",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.insertSOParamText.grid(row=0, column=0, columnspan=5, ipadx=3, ipady=5, sticky=N+E+W)

        #################################
        #   Frequency Inline Selector   #
        #################################

        # Widgets Definition
        self.labelFrequency = tk.Label(self, width=21, text="Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryFrequency = tk.Entry(self, width=5)

        self.HzUnitButton = tk.Button( self, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitButtonPressed)
        self.kHzUnitButton = tk.Button(self, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitButtonPressed)
        self.MHzUnitButton = tk.Button(self, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitButtonPressed)

        # Widgets Placement
        self.labelFrequency.grid(row=1, column=0, sticky=W, ipady=10)
        self.entryFrequency.grid(row=1, column=1, sticky=E, ipadx=10)

        self.HzUnitButton.grid( row=1, column=2)
        self.kHzUnitButton.grid(row=1, column=3)
        self.MHzUnitButton.grid(row=1, column=4)

        ###########################################
        #   Damping Coefficient Inline Selector   #
        ###########################################
        
        # Widgets Definition
        self.labelDampCoeff = tk.Label(self, width=21, text="Damping Coefficient", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryDampCoeff = tk.Entry(self, width=5)
        self.buttonDampCoeff = tk.Button(self, text="Get", font=config.SMALL_FONT, command=self.buttonDampCoeffPressed)

        # Widgets Placement
        self.labelDampCoeff.grid( row=2, column=0, sticky=W, ipady=10)
        self.entryDampCoeff.grid( row=2, column=1, ipadx=10)
        self.buttonDampCoeff.grid(row=2, column=2, columnspan=3)

        ######################################
        #   BandWidth Gain Inline Selector   #
        ######################################
        
        # Widgets Definition
        self.labelGainBW = tk.Label(self, width=21, text="BandWidth Gain", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryGainBW = tk.Entry(self, width=5)
        self.buttonGainBW = tk.Button(self, text="Get", font=config.SMALL_FONT, command=self.buttonGainBWPressed)

        # Widgets Placement
        self.labelGainBW.grid( row=3, column=0, sticky=W, ipady=10)
        self.entryGainBW.grid( row=3, column=1, ipadx=10)
        self.buttonGainBW.grid(row=3, column=2, columnspan=3)

        ###################################
        #   Filter Type Inline Selector   #
        ###################################

        # Widgets Definition
        self.labelFilterType = tk.Label(self, width=21, text="Filter Type", font=config.SMALL_FONT, bg="#ffe4c4")

        self.buttonLowPass = tk.Button(
            self, text="Low Pass", font=config.SMALL_FONT, command=self.buttonLowPassPressed)
        self.buttonHighPass =tk.Button(
            self, text="High Pass",font=config.SMALL_FONT, command=self.buttonHighPassPressed)
        self.buttonAllPass = tk.Button(
            self, text="All Pass", font=config.SMALL_FONT, command=self.buttonAllPassPressed)
        self.buttonBandPass = tk.Button(
            self, text="Band Pass", font=config.SMALL_FONT, command=self.buttonBandPassPressed)

        # Widgets Placement
        self.labelFilterType.grid(row=4, rowspan=2, column=0, columnspan=2, sticky=W, ipady=10)

        self.buttonLowPass.grid( row=4, column=2)
        self.buttonHighPass.grid(row=4, column=3)
        self.buttonAllPass.grid( row=4, column=4)
        self.buttonBandPass.grid(row=5, column=2)

        dictInput["filterType"] = "lowPass"

    #################################################
    #   Frequency Unit Buttons' Callback Functions  #
    #################################################

    def HzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=FLAT)
        self.kHzUnitButton.config(relief=RAISED)
        self.MHzUnitButton.config(relief=RAISED)
        dictInput["frequencyValue"] = int(self.entryFrequency.get())
        dictInput["frequencyUnitFactor"] = 1

    def kHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED)
        self.kHzUnitButton.config(relief=FLAT)
        self.MHzUnitButton.config(relief=RAISED)
        dictInput["frequencyValue"] = int(self.entryFrequency.get())
        dictInput["frequencyUnitFactor"] = 1000

    def MHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED)
        self.kHzUnitButton.config(relief=RAISED)
        self.MHzUnitButton.config(relief=FLAT)
        dictInput["frequencyValue"] = int(self.entryFrequency.get())
        dictInput["frequencyUnitFactor"] = 1000000

    ##############################################
    #   Filter Type Buttons' Callback Functions  #
    ##############################################

    def buttonLowPassPressed(self):
        self.buttonLowPass.config( relief=FLAT)
        self.buttonHighPass.config(relief=RAISED)
        self.buttonAllPass.config( relief=RAISED)
        self.buttonBandPass.config(relief=RAISED)
        dictInput["filterType"] = "lowPass"
    
    def buttonHighPassPressed(self):
        self.buttonLowPass.config( relief=RAISED)
        self.buttonHighPass.config(relief=FLAT)
        self.buttonAllPass.config( relief=RAISED)
        self.buttonBandPass.config(relief=RAISED)
        dictInput["filterType"] = "highPass"

    def buttonAllPassPressed(self):
        self.buttonLowPass.config( relief=RAISED)
        self.buttonHighPass.config(relief=RAISED)
        self.buttonAllPass.config( relief=FLAT)
        self.buttonBandPass.config(relief=RAISED)
        dictInput["filterType"] = "allPass"

    def buttonBandPassPressed(self):
        self.buttonLowPass.config( relief=RAISED)
        self.buttonHighPass.config(relief=RAISED)
        self.buttonAllPass.config( relief=RAISED)
        self.buttonBandPass.config(relief=FLAT)
        dictInput["filterType"] = "bandPass"

    ###################################################
    #   Damping Coefficient Button Callback Function  #
    ###################################################

    def buttonDampCoeffPressed(self):
        self.buttonDampCoeff.config( relief=FLAT)
        dictInput["dampCoeff"] = float(self.entryDampCoeff.get())

    #################################################
    #   Bandwidth Gain Buttons' Callback Functions  #
    #################################################

    def buttonGainBWPressed(self):
        self.buttonGainBW.config( relief=FLAT)
        dictInput["gainBW"] = int(self.entryGainBW.get())

    def focus(self):
        pass
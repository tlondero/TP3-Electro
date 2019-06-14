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
        self.labelFrequency = tk.Label(self, width=15, text="Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
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

        ###########################################
        #   Damping Coefficient Inline Selector   #
        ###########################################
        
        # Widgets Definition
        self.labelDampCoeff = tk.Label(self, width=15, text="Damping Coeff", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryDampCoeff = tk.Entry(self, width=5)
        self.buttonDampCoeff = tk.Button(self, width=8, text="Send", font=config.SMALL_FONT, command=self.buttonDampCoeffPressed)

        # Widgets Placement
        self.labelDampCoeff.grid( row=2, column=0, sticky=W, ipady=10)
        self.entryDampCoeff.grid( row=2, column=1, sticky=E, ipadx=10)
        self.buttonDampCoeff.grid(row=2, column=2)

        ######################################
        #   BandWidth Gain Inline Selector   #
        ######################################
        
        # Widgets Definition
        self.labelGainBW = tk.Label(self, width=15, text="BandWidth Gain", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryGainBW = tk.Entry(self, width=5)
        self.buttonGainBW = tk.Button(self, width=8, text="Send", font=config.SMALL_FONT, command=self.buttonGainBWPressed)

        # Widgets Placement
        self.labelGainBW.grid( row=3, column=0, sticky=W, ipady=10)
        self.entryGainBW.grid( row=3, column=1, sticky=E, ipadx=10)
        self.buttonGainBW.grid(row=3, column=2)

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
        self.buttonBandPass = tk.Button(
            self, width=8, text="Band Pass", font=config.SMALL_FONT, command=self.buttonBandPassPressed)
        self.buttonSingNotch = tk.Button(
            self, width=8, text="SingNotch", font=config.SMALL_FONT, command=self.buttonSingNotchPressed)
        self.buttonMultNotch = tk.Button(
            self, width=8, text="MultNotch", font=config.SMALL_FONT, command=self.buttonMultNotchPressed)

        # Widgets Placement
        self.labelFilterType.grid(row=4, rowspan=2, column=0, columnspan=2, sticky=W, ipady=10)

        self.buttonLowPass.grid(  row=4, column=2, pady=5)
        self.buttonHighPass.grid( row=4, column=3)
        self.buttonAllPass.grid(  row=4, column=4)
        self.buttonBandPass.grid( row=5, column=2, pady=5)
        self.buttonSingNotch.grid(row=5, column=3)
        self.buttonMultNotch.grid(row=5, column=4)

        self.insertMNParamText = tk.Label(
            self, width=55, text="For the multiple Notch, insert the parameters below",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.insertMNParamText.grid(row=6, column=0, columnspan=5, ipadx=3, ipady=5, sticky=N+E+W)

        dictInput["filterType"] = "lowPass"

        ############################################
        #   Notch Zero Frequency Inline Selector   #
        ############################################

        # Widgets Definition
        self.labelNZFrequency = tk.Label(self, width=15, text="Zero Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryNZFrequency = tk.Entry(self, width=5)

        self.HzUnitNZButton = tk.Button( self, width=8, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitNZButtonPressed)
        self.kHzUnitNZButton = tk.Button(self, width=8, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitNZButtonPressed)
        self.MHzUnitNZButton = tk.Button(self, width=8, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitNZButtonPressed)

        # Widgets Placement
        self.labelNZFrequency.grid(row=7, column=0, sticky=W, ipady=10)
        self.entryNZFrequency.grid(row=7, column=1, sticky=E, ipadx=10)

        self.HzUnitNZButton.grid( row=7, column=2)
        self.kHzUnitNZButton.grid(row=7, column=3)
        self.MHzUnitNZButton.grid(row=7, column=4)

        ######################################################
        #   Notch Zero Damping Coefficient Inline Selector   #
        ######################################################
        
        # Widgets Definition
        self.labelNZDampCoeff = tk.Label(self, width=15, text="Damping Coeff", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryNZDampCoeff = tk.Entry(self, width=5)
        self.buttonNZDampCoeff = tk.Button(self, width=8, text="Send", font=config.SMALL_FONT, command=self.buttonNZDampCoeffPressed)

        # Widgets Placement
        self.labelNZDampCoeff.grid( row=8, column=0, sticky=W, ipady=10)
        self.entryNZDampCoeff.grid( row=8, column=1, sticky=E, ipadx=10)
        self.buttonNZDampCoeff.grid(row=8, column=2)

        ############################################
        #   Notch Pole Frequency Inline Selector   #
        ############################################

        # Widgets Definition
        self.labelNPFrequency = tk.Label(self, width=15, text="Pole Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryNPFrequency = tk.Entry(self, width=5)

        self.HzUnitNPButton = tk.Button( self, width=8, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitNPButtonPressed)
        self.kHzUnitNPButton = tk.Button(self, width=8, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitNPButtonPressed)
        self.MHzUnitNPButton = tk.Button(self, width=8, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitNPButtonPressed)

        # Widgets Placement
        self.labelNPFrequency.grid(row=9, column=0, sticky=W, ipady=10)
        self.entryNPFrequency.grid(row=9, column=1, sticky=E, ipadx=10)

        self.HzUnitNPButton.grid( row=9, column=2)
        self.kHzUnitNPButton.grid(row=9, column=3)
        self.MHzUnitNPButton.grid(row=9, column=4)

        ######################################################
        #   Notch Pole Damping Coefficient Inline Selector   #
        ######################################################
        
        # Widgets Definition
        self.labelNPDampCoeff = tk.Label(self, width=15, text="Damping Coeff", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryNPDampCoeff = tk.Entry(self, width=5)
        self.buttonNPDampCoeff = tk.Button(self, width=8, text="Send", font=config.SMALL_FONT, command=self.buttonNPDampCoeffPressed)

        # Widgets Placement
        self.labelNPDampCoeff.grid( row=10, column=0, sticky=W, ipady=10)
        self.entryNPDampCoeff.grid( row=10, column=1, sticky=E, ipadx=10)
        self.buttonNPDampCoeff.grid(row=10, column=2)

    #################################################
    #   Frequency Unit Buttons' Callback Functions  #
    #################################################

    def HzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=FLAT,   bg="#ffe4c4")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        dictInput["frequencyValue"] = float(self.entryFrequency.get())
        dictInput["frequencyUnitFactor"] = 1

    def kHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        dictInput["frequencyValue"] = float(self.entryFrequency.get())
        dictInput["frequencyUnitFactor"] = 1000

    def MHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")
        dictInput["frequencyValue"] = float(self.entryFrequency.get())
        dictInput["frequencyUnitFactor"] = 1000000
    
    ############################################################
    #   Notch Zero Frequency Unit Buttons' Callback Functions  #
    ############################################################

    def HzUnitNZButtonPressed(self):
        self.HzUnitNZButton.config( relief=FLAT,   bg="#ffe4c4")
        self.kHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        dictInput["frequencyNZValue"] = float(self.entryNZFrequency.get())
        dictInput["frequencyNZUnitFactor"] = 1

    def kHzUnitNZButtonPressed(self):
        self.HzUnitNZButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitNZButton.config(relief=FLAT,   bg="#ffe4c4")
        self.MHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        dictInput["frequencyNZValue"] = float(self.entryNZFrequency.get())
        dictInput["frequencyNZUnitFactor"] = 1000

    def MHzUnitNZButtonPressed(self):
        self.HzUnitNZButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitNZButton.config(relief=FLAT,   bg="#ffe4c4")
        dictInput["frequencyNZValue"] = float(self.entryNZFrequency.get())
        dictInput["frequencyNZUnitFactor"] = 1000000

    ############################################################
    #   Notch Pole Frequency Unit Buttons' Callback Functions  #
    ############################################################

    def HzUnitNPButtonPressed(self):
        self.HzUnitNPButton.config( relief=FLAT,   bg="#ffe4c4")
        self.kHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        dictInput["frequencyNPValue"] = float(self.entryNPFrequency.get())
        dictInput["frequencyNPUnitFactor"] = 1

    def kHzUnitNPButtonPressed(self):
        self.HzUnitNPButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitNPButton.config(relief=FLAT,   bg="#ffe4c4")
        self.MHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        dictInput["frequencyNPValue"] = float(self.entryNPFrequency.get())
        dictInput["frequencyNPUnitFactor"] = 1000

    def MHzUnitNPButtonPressed(self):
        self.HzUnitNPButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitNPButton.config(relief=FLAT,   bg="#ffe4c4")
        dictInput["frequencyNPValue"] = float(self.entryNPFrequency.get())
        dictInput["frequencyNPUnitFactor"] = 1000000

    ##############################################
    #   Filter Type Buttons' Callback Functions  #
    ##############################################

    def buttonLowPassPressed(self):
        self.buttonLowPass.config(  relief=FLAT,   bg="#ffe4c4")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")
        dictInput["filterType"] = "lowPass"
    
    def buttonHighPassPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")
        dictInput["filterType"] = "highPass"

    def buttonAllPassPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=FLAT,   bg="#ffe4c4")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")
        dictInput["filterType"] = "allPass"

    def buttonBandPassPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")
        dictInput["filterType"] = "bandPass"
    
    def buttonSingNotchPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=FLAT,   bg="#ffe4c4")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")
        dictInput["filterType"] = "singleNotch"

    def buttonMultNotchPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=FLAT,   bg="#ffe4c4")
        dictInput["filterType"] = "multipleNotch"  

    ###################################################
    #   Damping Coefficient Button Callback Function  #
    ###################################################

    def buttonDampCoeffPressed(self):
        self.buttonDampCoeff.config(relief=FLAT, bg="#ffe4c4")
        dictInput["dampCoeff"] = float(self.entryDampCoeff.get())

    ##############################################################
    #   Notch Zero Damping Coefficient Button Callback Function  #
    ##############################################################

    def buttonNZDampCoeffPressed(self):
        self.buttonNZDampCoeff.config(relief=FLAT, bg="#ffe4c4")
        dictInput["NZdampCoeff"] = float(self.entryNZDampCoeff.get())

    ##############################################################
    #   Notch Pole Damping Coefficient Button Callback Function  #
    ##############################################################

    def buttonNPDampCoeffPressed(self):
        self.buttonNPDampCoeff.config(relief=FLAT, bg="#ffe4c4")
        dictInput["NPdampCoeff"] = float(self.entryNPDampCoeff.get())

    #################################################
    #   Bandwidth Gain Buttons' Callback Functions  #
    #################################################

    def buttonGainBWPressed(self):
        self.buttonGainBW.config(relief=FLAT, bg="#ffe4c4")
        dictInput["gainBW"] = int(self.entryGainBW.get())

    ######################################
    #   Reset Buttons' Relief Function   #
    ######################################

    def resetButtons(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        self.HzUnitNZButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")

        self.HzUnitNPButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")

        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")

        self.buttonDampCoeff.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonNZDampCoeff.config(relief=RAISED, bg="#f0f0f0")
        self.buttonNPDampCoeff.config(relief=RAISED, bg="#f0f0f0")

        self.buttonGainBW.config(relief=RAISED, bg="#f0f0f0")

    def focus(self):
        pass
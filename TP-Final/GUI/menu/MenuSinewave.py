import tkinter as tk
from tkinter import *
import config
from userInput import dictInput
import numpy as np

class MenuSinewave(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.insertSineParamText = tk.Label(
            self, width=55, text="Insert the sinewave parameters",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.insertSineParamText.grid(row=0, column=0, columnspan=5, ipadx=3, ipady=5, sticky=N+E+W)

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

        self.HzUnitButton.grid(row =1, column=2)
        self.kHzUnitButton.grid(row=1, column=3)
        self.MHzUnitButton.grid(row=1, column=4)  

        #################################
        #   Amplitude Inline Selector   #
        #################################

        # Widgets Definition
        self.labelAmplitude = tk.Label(self, width=15, text="Amplitude", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryAmplitude = tk.Entry(self, width=5)

        self.mVUnitButton = tk.Button(self, width=8, text="mV", font=config.SMALL_FONT, command=self.mVUnitButtonPressed)
        self.VUnitButton = tk.Button( self, width=8, text="V",  font=config.SMALL_FONT, command=self.VUnitButtonPressed)

        # Widgets Placement
        self.labelAmplitude.grid(row=2, column=0, sticky=W, ipady=10)
        self.entryAmplitude.grid(row=2, column=1, sticky=E, ipadx=10)

        self.mVUnitButton.grid(row=2, column=2)
        self.VUnitButton.grid( row=2, column=3)   

        ##############################
        #   Offset Inline Selector   #
        ##############################

        # Widgets Definition
        self.labelOffset = tk.Label(self, width=15, text="Offset", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryOffset = tk.Entry(self, width=5)

        self.mVUnitOffButton = tk.Button(self, width=8, text="mV", font=config.SMALL_FONT, command=self.mVUnitOffButtonPressed)
        self.VUnitOffButton = tk.Button( self, width=8, text="V",  font=config.SMALL_FONT, command=self.VUnitOffButtonPressed)

        # Widgets Placement
        self.labelOffset.grid(row=3, column=0, sticky=W, ipady=10)
        self.entryOffset.grid(row=3, column=1, sticky=E, ipadx=10)

        self.mVUnitOffButton.grid(row=3, column=2)
        self.VUnitOffButton.grid( row=3, column=3) 

        ######################################
        #   Initialize Sinewave Parameters   #
        ######################################

        self.frequencyValue = 1
        self.frequencyUnitFactor = 1
        self.amplitudeValue = 1
        self.amplitudeUnitFactor = 1
        self.offsetValue = 0
        self.offsetUnitFactor = 1

    #################################################
    #   Frequency Unit Buttons' Callback Functions  #
    #################################################

    def HzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=FLAT,   bg="#ffe4c4")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.frequencyValue = float(self.entryFrequency.get())
        self.frequencyUnitFactor = 1
        self.updateSignal()
        dictInput["inputFrequencyValue"] = self.frequencyValue
        dictInput["inputFrequencyUnitFactor"] = self.frequencyUnitFactor

    def kHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.frequencyValue = float(self.entryFrequency.get())
        self.frequencyUnitFactor = 1000
        self.updateSignal()
        dictInput["inputFrequencyValue"] = self.frequencyValue
        dictInput["inputFrequencyUnitFactor"] = self.frequencyUnitFactor

    def MHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")
        self.frequencyValue = float(self.entryFrequency.get())
        self.frequencyUnitFactor = 1000000
        self.updateSignal()
        dictInput["inputFrequencyValue"] = self.frequencyValue
        dictInput["inputFrequencyUnitFactor"] = self.frequencyUnitFactor

    #################################################
    #   Amplitude Unit Buttons' Callback Functions  #
    #################################################

    def mVUnitButtonPressed(self):
        self.mVUnitButton.config(relief=FLAT,   bg="#ffe4c4")
        self.VUnitButton.config (relief=RAISED, bg="#f0f0f0")
        self.amplitudeValue = float(self.entryAmplitude.get())
        self.amplitudeUnitFactor = 0.001
        self.updateSignal()
        dictInput["inputAmplitudeValue"] = self.amplitudeValue
        dictInput["inputAmplitudeUnitFactor"] = self.amplitudeUnitFactor

    def VUnitButtonPressed(self):
        self.mVUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.VUnitButton.config (relief=FLAT,   bg="#ffe4c4")
        self.amplitudeValue = float(self.entryAmplitude.get())
        self.amplitudeUnitFactor = 1
        self.updateSignal()
        dictInput["inputAmplitudeValue"] = self.amplitudeValue
        dictInput["inputAmplitudeUnitFactor"] = self.amplitudeUnitFactor

    ##############################################
    #   Offset Unit Buttons' Callback Functions  #
    ##############################################

    def mVUnitOffButtonPressed(self):
        self.mVUnitOffButton.config(relief=FLAT,   bg="#ffe4c4")
        self.VUnitOffButton.config (relief=RAISED, bg="#f0f0f0")
        self.offsetValue = float(self.entryOffset.get())
        self.offsetUnitFactor = 0.001
        self.updateSignal()
        dictInput["inputOffsetValue"] = self.offsetValue
        dictInput["inputOffsetUnitFactor"] = self.offsetUnitFactor

    def VUnitOffButtonPressed(self):
        self.mVUnitOffButton.config(relief=RAISED, bg="#f0f0f0")
        self.VUnitOffButton.config (relief=FLAT,   bg="#ffe4c4")
        self.offsetValue = float(self.entryOffset.get())
        self.offsetUnitFactor = 1
        self.updateSignal()
        dictInput["inputOffsetValue"] = self.offsetValue
        dictInput["inputOffsetUnitFactor"] = self.offsetUnitFactor

    ######################################
    #   Reset Buttons' Relief Function   #
    ######################################

    def resetButtons(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        self.mVUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.VUnitButton.config (relief=RAISED, bg="#f0f0f0")

    ####################################################
    #   Update Sinewave With Modified Params Function  #
    ####################################################

    def updateSignal(self):
        period = 1/(self.frequencyValue * self.frequencyUnitFactor)
        t = np.linspace(0, 20*period, 1e5)
        A = self.amplitudeValue * self.amplitudeUnitFactor
        f = self.frequencyValue * self.frequencyUnitFactor
        off = self.offsetValue * self.offsetUnitFactor
        w = 2 * np.pi * f
        y = A * np.sin(w * t) + off
        dictInput["inputSignal"] = {"y": y, "t": t}
        dictInput["inputSignalType"] = "Sinewave"

    def focus(self):
        pass
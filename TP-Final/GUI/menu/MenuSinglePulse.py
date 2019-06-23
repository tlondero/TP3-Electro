import tkinter as tk
from tkinter import *
import config
from userInput import dictInput
import numpy as np
from scipy import signal

class MenuSinglePulse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.insertSingPulseParamText = tk.Label(
            self, width=55, text="Entregar los parametros del pulso único",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.insertSingPulseParamText.grid(row=0, column=0, columnspan=6, ipadx=3, ipady=5, sticky=N+E+W)

        #################################
        #   Amplitude Inline Selector   #
        #################################

        # Widgets Definition
        self.labelAmplitude = tk.Label(self, width=15, text="Amplitud", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryAmplitude = tk.Entry(self, width=5)

        self.mVUnitAmpButton = tk.Button(self, width=8, text="mV", font=config.SMALL_FONT, command=self.mVUnitAmpButtonPressed)
        self.VUnitAmpButton = tk.Button( self, width=8, text="V",  font=config.SMALL_FONT, command=self.VUnitAmpButtonPressed)

        # Widgets Placement
        self.labelAmplitude.grid(row=1, column=0, sticky=W, ipady=10)
        self.entryAmplitude.grid(row=1, column=1, sticky=E, ipadx=10)

        self.mVUnitAmpButton.grid(row=1, column=2)
        self.VUnitAmpButton.grid( row=1, column=3)     

        ##############################
        #   Offset Inline Selector   #
        ##############################

        # Widgets Definition
        self.labelOffset = tk.Label(self, width=15, text="Offset", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryOffset = tk.Entry(self, width=5)

        self.mVUnitOffButton = tk.Button(self, width=8, text="mV", font=config.SMALL_FONT, command=self.mVUnitOffButtonPressed)
        self.VUnitOffButton = tk.Button( self, width=8, text="V",  font=config.SMALL_FONT, command=self.VUnitOffButtonPressed)

        # Widgets Placement
        self.labelOffset.grid(row=2, column=0, sticky=W, ipady=10)
        self.entryOffset.grid(row=2, column=1, sticky=E, ipadx=10)

        self.mVUnitOffButton.grid(row=2, column=2)
        self.VUnitOffButton.grid( row=2, column=3) 

        ##########################################
        #   Initialize Single Pulse Parameters   #
        ##########################################

        self.amplitudeValue = 1
        self.amplitudeUnitFactor = 1
        self.offsetValue = 0
        self.offsetUnitFactor = 1
        self.dutyCycleValue = 50

    #################################################
    #   Amplitude Unit Buttons' Callback Functions  #
    #################################################

    def mVUnitAmpButtonPressed(self):
        self.mVUnitAmpButton.config(relief=FLAT,   bg="#ffe4c4")
        self.VUnitAmpButton.config (relief=RAISED, bg="#f0f0f0")
        self.amplitudeValue = float(self.entryAmplitude.get())
        self.amplitudeUnitFactor = 0.001
        self.updateSignal()
        dictInput["inputAmplitudeValue"] = self.amplitudeValue
        dictInput["inputAmplitudeUnitFactor"] = self.amplitudeUnitFactor

    def VUnitAmpButtonPressed(self):
        self.mVUnitAmpButton.config(relief=RAISED, bg="#f0f0f0")
        self.VUnitAmpButton.config (relief=FLAT,   bg="#ffe4c4")
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
        self.mVUnitAmpButton.config(relief=RAISED, bg="#f0f0f0")
        self.VUnitAmpButton.config (relief=RAISED, bg="#f0f0f0")

        self.mVUnitOffButton.config(relief=RAISED, bg="#f0f0f0")
        self.VUnitOffButton.config (relief=RAISED, bg="#f0f0f0")

    ##########################################################
    #   Update Periodic Pulse With Modified Params Function  #
    ##########################################################

    def updateSignal(self):
        period = 1 / (dictInput.get("frequencyValue") * dictInput.get("frequencyUnitFactor"))
        t = np.linspace(0, 2 * period, 1e5)
        A = self.amplitudeValue * self.amplitudeUnitFactor
        off = self.offsetValue * self.offsetUnitFactor
        y = (A * np.heaviside(t - (0.05 * period), 0.5)) + off
        dictInput["inputSignal"] = {"y": y, "t": t}
        dictInput["inputSignalType"] = "Single Pulse"

    def focus(self):
        pass
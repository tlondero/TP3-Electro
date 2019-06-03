import tkinter as tk
from tkinter import *
import config
from userInput import dictInput
import numpy as np

class MenuPeriodicPulse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.insertPerioPulseParamText = tk.Label(
            self, text="Insert the periodic pulse parameters",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.insertPerioPulseParamText.grid(row=0, column=0, columnspan=6, sticky=N+E+W)

        #################################
        #   Frequency Inline Selector   #
        #################################

        # Widgets Definition
        self.labelFrequency = tk.Label(self, text="Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
        self.entryFrequency = tk.Entry(self, background="#ffe4c4")

        self.mHzUnitButton = tk.Button(self, text="mHz", font=config.SMALL_FONT, command=self.mHzUnitButtonPressed)
        self.HzUnitButton = tk.Button( self, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitButtonPressed)
        self.kHzUnitButton = tk.Button(self, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitButtonPressed)
        self.MHzUnitButton = tk.Button(self, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitButtonPressed)

        # Widgets Placement
        self.labelFrequency.grid(row=1, column=0, sticky=W, ipady=10)
        self.entryFrequency.grid(row=1, column=1, sticky=E, ipadx=10)

        self.mHzUnitButton.grid(row=1, column=2)
        self.HzUnitButton.grid(row =1, column=3)
        self.kHzUnitButton.grid(row=1, column=4)
        self.MHzUnitButton.grid(row=1, column=5)       

        paso = 1e-6
        # generamos una señal de pulso periódico que arranque en t = 0.01 con f=1khz
        t = np.arange(0, 0.01, paso) # 1us de presición
        n = len(t)

        freq = 1e3
        period = 1 / freq
        periodSamples = int(period / paso)

        # este codigo genera una señal cuadrada,
        cuadrada = np.where(np.arange(n) % periodSamples < periodSamples/2, -0.5, 0.5)

        # para que la señal no empiece de golpe y visualmente se vea mejor su comienzo
        for i in range(2 * periodSamples):
            cuadrada[i] = 0

        # cargamos a la memoria la entrada seleccionada. Esta información será utilizada
        # por MenuInputOutput
        dictInput["inputSignal"] = {"y": cuadrada, "t": t}

    #################################################
    #   Frequency Unit Buttons' Callback Functions  #
    #################################################

    def mHzUnitButtonPressed(self):
        self.mHzUnitButton.config(relief=SUNKEN)
        self.HzUnitButton.config( relief=RAISED)
        self.kHzUnitButton.config(relief=RAISED)
        self.MHzUnitButton.config(relief=RAISED)
        dictInput["frequencyUnit"] = "mHz"

    def HzUnitButtonPressed(self):
        self.mHzUnitButton.config(relief=RAISED)
        self.HzUnitButton.config( relief=SUNKEN)
        self.kHzUnitButton.config(relief=RAISED)
        self.MHzUnitButton.config(relief=RAISED)
        dictInput["frequencyUnit"] = "Hz"

    def kHzUnitButtonPressed(self):
        self.mHzUnitButton.config(relief=RAISED)
        self.HzUnitButton.config( relief=RAISED)
        self.kHzUnitButton.config(relief=SUNKEN)
        self.MHzUnitButton.config(relief=RAISED)
        dictInput["frequencyUnit"] = "kHz"

    def MHzUnitButtonPressed(self):
        self.mHzUnitButton.config(relief=RAISED)
        self.HzUnitButton.config( relief=RAISED)
        self.kHzUnitButton.config(relief=RAISED)
        self.MHzUnitButton.config(relief=SUNKEN)
        dictInput["frequencyUnit"] = "MHz"

    def focus(self):
        pass
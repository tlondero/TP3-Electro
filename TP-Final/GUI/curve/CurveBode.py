import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from numpy import pi

class CurveBode(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, text="This is the Bode curve", font=config.SMALL_FONT, bg="#ffffff")
        self.title.pack(side=TOP, fill=X, ipady=10)

        ##########################
        #   Bode Graphs Canvas   #
        ##########################
        self.graphBode = Canvas(self)
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2, sharex=True)
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graphBode)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graphBode)
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graphBode.pack(side=TOP, expand=1, fill=BOTH)
    
    def simulate(self):
        ###########################################
        #   System Variables Reading User Input   #
        ###########################################
        # Frequency Value
        f0 = dictInput.get("frequencyValue")

        # Damping Coefficient
        xi = dictInput.get("dampCoeff")

        # BandWidth Gain
        k = dictInput.get("gainBW")

        # Frequency Unit
        frequencyUnitFactor = 1

        if dictInput["frequencyUnit"] == "mHZ":
            frequencyUnitFactor = 0.001
        elif dictInput["frequencyUnit"] == "HZ":
            frequencyUnitFactor = 1
        elif dictInput["frequencyUnit"] == "kHZ":
            frequencyUnitFactor = 1000
        elif dictInput["frequencyUnit"] == "MHZ":
            frequencyUnitFactor = 1000000

        # Defining pulsation
        w0 = 2 * pi * f0 * frequencyUnitFactor
    
        #############################################
        #   System Definition Reading  User Input   #
        #############################################
        global sys
        # First Order Systems
        if dictInput["order"] == 1:
            # Low Pass Filter
            if dictInput["filterType"] == "lowPass":
                sys = signal.lti([k * w0], [1, w0])
            # High Pass Filter
            elif dictInput["filterType"] == "highPass":
                sys = signal.lti([k * w0, 0], [1, w0])
            # All Pass Filter
            elif dictInput["filterType"] == "allPass":
                sys = signal.lti([k, -k * w0], [1, w0])

        # Second Order Systems
        elif dictInput["order"] == 2:
            # Low Pass Filter
            if dictInput["filterType"] == "lowPass":
                sys = signal.lti([k * w0 * w0], [1, 2 * xi * w0, w0 * w0])
            # High Pass Filter
            elif dictInput["filterType"] == "highPass":
                sys = signal.lti([k * w0 * w0, 0, 0], [1, 2 * xi * w0, w0 * w0])
            # All Pass Filter
            elif dictInput["filterType"] == "allPass":
                sys = signal.lti([k, -2 * k * xi * w0, w0 * w0], [1, 2 * xi * w0, w0 * w0])
            # Band Pass Filter
            elif dictInput["filterType"] == "bandPass":
                sys = signal.lti([0, k * w0 * w0, 0], [1, 2 * xi * w0, w0 * w0])

        ################################
        #   System's Bode generation   #
        ################################
        # Draw the Bode graph taking 1000 values between 1Hz and 10MHz
        bode = dict()
        bode["w"], bode["gain"], bode["arg"] = signal.bode(sys)         

        #######################################
        #   Input and output plot functions   #
        #######################################
        self.ax1.clear()

        self.ax1.semilogx(bode["w"], bode["gain"], color="red")
        self.ax1.minorticks_on()
        self.ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        self.ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        self.ax2.clear()

        self.ax2.semilogx(bode["w"], bode["arg"], color="purple")
        self.ax2.minorticks_on()
        self.ax2.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        self.ax2.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        self.dataPlot.draw()

    def focus(self):
        pass
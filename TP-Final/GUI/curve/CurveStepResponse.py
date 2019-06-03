import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi

class CurveStepResponse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, text="This is the Step Response curve", font=config.SMALL_FONT, bg="#ffffff")
        self.title.pack(side=TOP, fill=X, ipady=10)

        ###################################
        #   Step Response Graphs Canvas   #
        ###################################
        self.graphStepResponse = Canvas(self)
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2, sharex=True)
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graphStepResponse)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graphStepResponse)
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graphStepResponse.pack(side=TOP, expand=1, fill=BOTH)
    
    def simulate(self):
        ###########################################
        #   System Variables Reading User Input   #
        ###########################################
        # Frequency Value
        f0 = dictInput.get("frequencyValue")

        #BandWidth Gain
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
            # Undefined Filter

        # Second Order Systems
        elif dictInput["order"] == 2:
            pass

        ################################
        #   Output system generation   #
        ################################  
        output = dict()
        output["t"], output["y"], m = signal.lsim(sys, dictInput["inputSignal"]["y"], dictInput["inputSignal"]["t"])         

        #######################################
        #   Input and output plot functions   #
        #######################################
        self.ax1.clear()

        self.ax1.plot(dictInput["inputSignal"]["t"], dictInput["inputSignal"]["y"])
        self.ax1.minorticks_on()
        self.ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        self.ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        self.ax2.clear()

        self.ax2.plot(output["t"], output["y"], color="orange")
        self.ax2.minorticks_on()
        self.ax2.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        self.ax2.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        self.dataPlot.draw()

    def focus(self):
        pass
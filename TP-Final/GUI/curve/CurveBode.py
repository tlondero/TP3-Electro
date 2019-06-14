import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi, power

class CurveBode(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, text="This is the Bode curve", font=config.SMALL_FONT, bg="#ffffff")
        self.title.grid(row=0, column=0, columnspan=6, ipady=7, sticky=N)

        ##########################
        #   Bode Graphs Canvas   #
        ##########################

        self.graphBode = Canvas(self)
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2, sharex=True)
        self.fig.subplots_adjust(top=0.95, right=0.95, bottom=0.12, hspace=0.30)
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graphBode)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graphBode)
        self.nav.config(bg="#ffffff")
        self.nav._message_label.config(bg="#ffffff", fg="#ff0000")        
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graphBode.grid(row=1, column=0, columnspan=6, sticky=N)

        ###################################
        #    Axis Units Inline Selector   #
        ###################################     

        # Widgets Definition
        self.labelFrequencyAxis = tk.Label(self, width=15, text="Frequency Axis", font=config.SMALL_FONT, bg="#ffffff")

        self.HzAxisButton = tk.Button(  self, width=8, text="Hz", relief=FLAT,      
        font=config.SMALL_FONT, command=self.HzAxisButtonPressed, bg="#ffffff")
        self.radsAxisButton = tk.Button(self, width=8, text="rad/sec", 
        font=config.SMALL_FONT, command=self.radsAxisButtonPressed)

        self.labelGainAxis = tk.Label(self, width=15, text="Gain Axis", font=config.SMALL_FONT, bg="#ffffff")

        self.dBAxisButton = tk.Button(   self, width=8, text="dB", relief=FLAT, 
        font=config.SMALL_FONT,  command=self.dBAxisButtonPressed, bg="#ffffff")
        self.timesAxisButton = tk.Button(self, width=8, text="x", 
        font=config.SMALL_FONT,  command=self.timesAxisButtonPressed)

        # Widgets Placement
        self.labelFrequencyAxis.grid(row=2, column=0, ipady=5)
        self.HzAxisButton.grid(      row=2, column=1, pady=5)
        self.radsAxisButton.grid(    row=2, column=2, pady=5)

        self.labelGainAxis.grid(  row=2, column=3, ipady=5)
        self.dBAxisButton.grid(   row=2, column=4, pady=5)
        self.timesAxisButton.grid(row=2, column=5, pady=5)

        # Default XAxis and YAxis Units
        self.freqAxisUnitFactor = 1 / (2 * pi)
        self.ax1.set_xlabel("Pulsation (Hz)")
        self.ax2.set_xlabel("Pulsation (Hz)")

        self.gainAxisdBActivated = True

    ###############################################
    #    Axis Units Buttons' Callback Functions   #
    ###############################################

    def HzAxisButtonPressed(self):
        self.HzAxisButton.config(  relief=FLAT,   bg="#ffffff")
        self.radsAxisButton.config(relief=RAISED, bg="#f0f0f0")
        self.freqAxisUnitFactor = 1 / (2 * pi)
        self.simulate()
        self.ax1.set_xlabel("Pulsation (Hz)")
        self.ax2.set_xlabel("Pulsation (Hz)")
        self.dataPlot.draw()

    def radsAxisButtonPressed(self):
        self.HzAxisButton.config(  relief=RAISED, bg="#f0f0f0")
        self.radsAxisButton.config(relief=FLAT,   bg="#ffffff")
        self.freqAxisUnitFactor = 1
        self.simulate()
        self.ax1.set_xlabel("Pulsation (rad/s)")
        self.ax2.set_xlabel("Pulsation (rad/s)")
        self.dataPlot.draw()

    def dBAxisButtonPressed(self):
        self.dBAxisButton.config(   relief=FLAT,   bg="#ffffff")
        self.timesAxisButton.config(relief=RAISED, bg="#f0f0f0")
        self.gainAxisdBActivated = True
        self.simulate()

    def timesAxisButtonPressed(self):
        self.dBAxisButton.config(   relief=RAISED, bg="#f0f0f0")
        self.timesAxisButton.config(relief=FLAT,   bg="#ffffff")
        self.gainAxisdBActivated = False
        self.simulate()
              
    def simulate(self):
        ###########################################
        #   System Variables Reading User Input   #
        ###########################################
        # Frequency Value
        f0 = dictInput.get("frequencyValue")
        # Frequency Unit Factor
        frequencyUnitFactor = dictInput.get("frequencyUnitFactor")
        # Damping Coefficient
        xi = dictInput.get("dampCoeff")
        # BandWidth Gain
        k = dictInput.get("gainBW")
        try:
            # Defining pulsation
            w0 = 2 * pi * f0 * frequencyUnitFactor

            # Notch Zero Frequency Value
            #fz = dictInput.get("frequencyNZValue")
            # Notch Zero Frequency Unit Factor
            #frequencyNZUnitFactor = dictInput.get("frequencyNZUnitFactor")
            # Notch Zero Damping Coefficient
            #xiz = dictInput.get("NZdampCoeff")
            # Defining Notch Zero pulsation
            #wz = 2 * pi * fz * frequencyNZUnitFactor

            # Notch Pole Frequency Value
            #fp = dictInput.get("frequencyNPValue")
            # Notch Pole Frequency Unit Factor
            #frequencyNPUnitFactor = dictInput.get("frequencyNPUnitFactor")
            # Notch Pole Damping Coefficient
            #xip = dictInput.get("NPdampCoeff")
            # Defining Notch Pole pulsation
            #wp = 2 * pi * fp * frequencyNPUnitFactor
        
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
                # Single Notch
                elif dictInput["filterType"] == "singleNotch":
                    sys = signal.lti([0, 1 , k * w0 * w0], [1, 2 * xi * w0, w0 * w0])
                # Multiple Notch
                #elif dictInput["filterType"] == "multipleNotch":
                    #sys = signal.lti([1, 2* k * xiz * wz, k * wz * wz], [1, 2* k * xip * wp, k * wp * wp])

            ################################
            #   System's Bode generation   #
            ################################
            # Draw the Bode graph taking 1000 values between 1Hz and 10MHz
            bode = dict()
            bode["w"], bode["gain"], bode["arg"] = signal.bode(sys)    

            freqAxis =  bode["w"] * self.freqAxisUnitFactor

        except(TypeError):
            self.title.config(text="Please configure all the system parameters.", fg="#ff0000")
        else:
            self.title.config(text="", fg="#000000")

            if self.gainAxisdBActivated :
                gainAxis = bode["gain"]
                self.ax1.set_yscale("linear")
            else :
                gainAxis = []
                for values in bode["gain"] :
                    gainAxis.append(power(values / 20, 10))
                self.ax1.set_yscale("log")

            ########################################
            #   Gain and Argument plot functions   #
            ########################################
            self.ax1.clear()

            self.ax1.semilogx(freqAxis, gainAxis, color="red")   
            self.ax1.minorticks_on()
            self.ax1.set_ylabel("Gain (dB)")
            self.ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            self.ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            self.ax2.clear()

            self.ax2.semilogx(freqAxis, bode["arg"], color="purple")
            self.ax2.minorticks_on()
            self.ax2.set_ylabel("Argument (°)")
            self.ax2.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            self.ax2.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            self.dataPlot.draw()

    def focus(self):
        pass
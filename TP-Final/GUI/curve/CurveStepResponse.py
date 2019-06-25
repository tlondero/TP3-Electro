import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi, sqrt

class CurveStepResponse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, text="Respuesta a entrada", font=config.SMALL_FONT, bg="#ffffff")
        self.title.grid(row=0, column=0, columnspan=14, ipady=7, sticky=N)

        ###################################
        #   Step Response Graphs Canvas   #
        ###################################

        self.graphStepResponse = Canvas(self)
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2, sharex=True)
        self.fig.subplots_adjust(top=0.95, right=0.95, bottom=0.12, hspace=0.30)
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graphStepResponse)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graphStepResponse)
        self.nav.config(bg="#ffffff")
        self.nav._message_label.config(bg="#ffffff", fg="#ff0000")
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graphStepResponse.grid(row=1, column=0, columnspan=14, sticky=N)

        ####################################
        #    Axis Scaling Inline Setter    #
        #################################### 

        # Widgets Definition
        self.periodQuantityLabel = tk.Label(self, width=7, text="Periods :", font=config.SMALLEST_FONT, bg="#ffffff")
        self.periodQuantityEntry = tk.Entry(self, width=3)

        self.inputLabel = tk.Label(self, width=5, text="Input :", font=config.SMALLEST_FONT, fg="#1f77b4", bg="#ffffff")

        self.yMinInputLabel = tk.Label(self, width=5, text="Y min", font=config.SMALLEST_FONT, fg="#1f77b4", bg="#ffffff")
        self.yMinInputEntry = tk.Entry(self, width=3)
        self.yMaxInputLabel = tk.Label(self, width=5, text="Y max", font=config.SMALLEST_FONT, fg="#1f77b4", bg="#ffffff")
        self.yMaxInputEntry = tk.Entry(self, width=3)

        self.outputLabel = tk.Label(self, width=5, text="Output :", font=config.SMALLEST_FONT, fg="#ff7f0e", bg="#ffffff")

        self.yMinOutputLabel = tk.Label(self, width=5, text="Y min", font=config.SMALLEST_FONT, fg="#ff7f0e", bg="#ffffff")
        self.yMinOutputEntry = tk.Entry(self, width=3)
        self.yMaxOutputLabel = tk.Label(self, width=5, text="Y max", font=config.SMALLEST_FONT, fg="#ff7f0e", bg="#ffffff")
        self.yMaxOutputEntry = tk.Entry(self, width=3)

        self.rescaleAxisButton = tk.Button(  self, width=8, text="Rescale",    
        font=config.SMALL_FONT, command=self.rescaleAxisButtonPressed, bg="#ffffff")

        self.autoscaleAxisButton = tk.Button(  self, width=8, text="Autoscale",    
        font=config.SMALL_FONT, command=self.autoscaleAxisButtonPressed, bg="#ffffff")

        # Widgets Placement
        self.periodQuantityLabel.grid(row=2, column=0, ipady=5)
        self.periodQuantityEntry.grid(row=2, column=1, pady=5)

        self.inputLabel.grid(row=2, column=2, ipady=5)

        self.yMinInputLabel.grid(row=2, column=3, ipady=5)
        self.yMinInputEntry.grid(row=2, column=4, pady=5)
        self.yMaxInputLabel.grid(row=2, column=5, ipady=5)
        self.yMaxInputEntry.grid(row=2, column=6, pady=5)
        
        self.outputLabel.grid(row=2, column=7, ipady=5)

        self.yMinOutputLabel.grid(row=2, column=8, ipady=5)
        self.yMinOutputEntry.grid(row=2, column=9, pady=5)
        self.yMaxOutputLabel.grid(row=2, column=10, ipady=5)
        self.yMaxOutputEntry.grid(row=2, column=11, pady=5)

        self.rescaleAxisButton.grid(row=2, column=12, pady=5)
        self.autoscaleAxisButton.grid(row=2, column=13, pady=5)

        # Default scaling variables
        self.autoscale = True
        self.periodQuantity = 5
        self.yMinInput = -1
        self.yMaxInput = 1
        self.yMinOutput = -1
        self.yMaxOutput = 1

    ################################################
    #    Rescale Axis Button's Callback Function   #
    ################################################

    def rescaleAxisButtonPressed(self):
        self.autoscale = False
        if(self.periodQuantityEntry.get()!=""):
            self.periodQuantity = float(self.periodQuantityEntry.get())
        if(self.yMinInputEntry.get()!=""):
            self.yMinInput = float(self.yMinInputEntry.get())
        if(self.yMaxInputEntry.get()!=""):
            self.yMaxInput = float(self.yMaxInputEntry.get())
        if(self.yMinOutputEntry.get()!=""):
            self.yMinOutput = float(self.yMinOutputEntry.get())
        if(self.yMaxOutputEntry.get()!=""):
            self.yMaxOutput = float(self.yMaxOutputEntry.get())
        self.simulate()

    def autoscaleAxisButtonPressed(self):
        self.autoscale = True
        self.simulate()
    
    def simulate(self):
        ###########################################
        #   System Variables Reading User Input   #
        ###########################################
        # Frequency Value
        f0 = dictInput.get("frequencyValue")
        # Frequency Unit Factor
        frequencyUnitFactor = dictInput.get("frequencyUnitFactor")
        #BandWidth Gain
        k = dictInput.get("gainBW")
        # Damping Coefficient
        xi = dictInput.get("dampCoeff")

        try:
            # Defining pulsation
            w0 = 2 * pi * f0 * frequencyUnitFactor
            #############################################
            #   System Definition Reading  User Input   #
            #############################################
            global sys
            # First Order Systems
            if dictInput["order"] == "Primer":

                # Gain Param
                k = dictInput.get("gainBW")

                # Low Pass Filter
                if dictInput["filterType"] == "Pasa bajos":
                    sys = signal.lti([k * w0], [1, w0])
                # High Pass Filter
                elif dictInput["filterType"] == "Pasa altos":
                    sys = signal.lti([k, 0], [1, w0])
                # All Pass Filter
                elif dictInput["filterType"] == "Pasa todo":
                    sys = signal.lti([k, -k * w0], [1, w0])

            # Second Order Systems
            elif dictInput["order"] == "Segundo":

                # Gain Parameter
                gainParamType = dictInput.get("gainParamType")
                k = dictInput.get("gainParam")
                if (gainParamType == "gainBW"):
                    # BandWidth Gain
                    k = dictInput.get("gainParam")
                elif(gainParamType == "gainMax"):
                    if(xi<1):
                        # Maximum Gain
                        G = 1 / (2 * xi * sqrt(1 - (xi * xi)))
                        g = dictInput.get("gainParam")
                        k = g / G
                    else:
                        k = dictInput.get("gainParam")


                # Low Pass Filter
                if dictInput["filterType"] == "Pasa bajos":
                    sys = signal.lti([k * w0 * w0], [1, 2 * xi * w0, w0 * w0])
                # High Pass Filter
                elif dictInput["filterType"] == "Pasa altos":
                    sys = signal.lti([k, 0, 0], [1, 2 * xi * w0, w0 * w0])
                # All Pass Filter
                elif dictInput["filterType"] == "Pasa todo":
                    sys = signal.lti([k, -2 * k * xi * w0,  k * w0 * w0], [1, 2 * xi * w0, w0 * w0])
                # Band Pass Filter
                elif dictInput["filterType"] == "Pasa banda":
                    sys = signal.lti([0, 2* xi * k * w0, 0], [1, 2 * xi * w0, w0 * w0])
                # Single Notch
                elif dictInput["filterType"] == "Single Notch":
                    sys = signal.lti([k, 0 , k * w0 * w0], [1, 2 * xi * w0, w0 * w0])
                # Multiple Notch
                elif dictInput["filterType"] == "Multiple Notch":
                    # Notch Zero Frequency Value
                    fz = dictInput.get("frequencyNZValue")
                    # Notch Zero Frequency Unit Factor
                    frequencyNZUnitFactor = dictInput.get("frequencyNZUnitFactor")
                    # Notch Zero Damping Coefficient
                    xiz = dictInput.get("NZdampCoeff")
                    # Defining Notch Zero pulsation
                    wz = 2 * pi * fz * frequencyNZUnitFactor

                    # Notch Pole Frequency Value
                    fp = dictInput.get("frequencyNPValue")
                    # Notch Pole Frequency Unit Factor
                    frequencyNPUnitFactor = dictInput.get("frequencyNPUnitFactor")
                    # Notch Pole Damping Coefficient
                    xip = dictInput.get("NPdampCoeff")
                    # Defining Notch Pole pulsation
                    wp = 2 * pi * fp * frequencyNPUnitFactor

                    if (wz > wp) :
                        sys = signal.lti([(k * wp * wp) / (wz * wz), (2* k * xiz * wp * wp) / wz, k * wp * wp], 
                                         [1, 2 * xip * wp, wp * wp])
                    else :
                        sys = signal.lti([k, 2* k * xiz * wz, k * wz * wz], [1, 2 * xip * wp, wp * wp])

            amp = dictInput.get("inputAmplitudeValue") * dictInput.get("inputAmplitudeUnitFactor")

        except(TypeError):
            self.title.config(text="Se tiene que configurar todos los parametros del sistema\
                y de la señal de entrada.", fg="#ff0000")
        else:
            self.title.config(text="", fg="#000000")
            ################################
            #   Output system generation   #
            ################################  
            output = dict()
            output["t"], output["y"], m = signal.lsim(sys, dictInput["inputSignal"]["y"], dictInput["inputSignal"]["t"])         

            #######################################
            #   Input and output plot functions   #
            #######################################

            #self.displayErrorsLabel.config(text="Please configure the input signal.")

            #self.displayErrorsLabel.config(text="")

            self.ax1.clear()

            self.ax1.plot(dictInput["inputSignal"]["t"], dictInput["inputSignal"]["y"])
            self.ax1.minorticks_on()

            self.ax1.set_xlabel("Time (s)")
            self.ax1.set_ylabel("Voltage (V)")
            self.ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            self.ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            self.ax2.clear()

            self.ax2.plot(output["t"], output["y"], color="orange")
            self.ax2.minorticks_on()

            self.ax2.set_xlabel("Time (s)")
            self.ax2.set_ylabel("Voltage (V)")
            self.ax2.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            self.ax2.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            if dictInput.get("inputSignalType") == "Single Pulse" :
                period = 1 / (f0 * frequencyUnitFactor)
                offset = dictInput.get("inputOffsetValue") * dictInput.get("inputOffsetUnitFactor")

                self.ax1.set_xlim((0, 2 * period))
                self.ax1.set_ylim(((- amp/8 + offset)*k, (amp + amp/4 + offset)*k))

                self.ax2.set_xlim((0, 2 * period))
                self.ax2.set_ylim(((- amp/8 + offset)*k, (amp + amp/4 + offset)*k))    

            else :        
                period = 1 / (dictInput.get("inputFrequencyValue") * dictInput.get("inputFrequencyUnitFactor"))

                if self.autoscale :
                    self.ax1.set_xlim((0, self.periodQuantity * period))
                    self.ax1.set_ylim(((-amp - amp/4)*k, (amp + amp/4)*k))

                    self.ax2.set_xlim((0, self.periodQuantity * period))
                    self.ax2.set_ylim(((-amp - amp/4)*k, (amp + amp/4)*k))

                else :
                    self.ax1.set_xlim((0, self.periodQuantity * period))
                    self.ax1.set_ylim((self.yMinInput, self.yMaxInput))

                    self.ax2.set_xlim((0, self.periodQuantity * period))
                    self.ax2.set_ylim((self.yMinOutput, self.yMaxOutput))

            self.dataPlot.draw()

            self.title.config(text="{} Response curve : {} order {}, f0 = {}{}, K = {}.".format(
                dictInput.get("inputSignalType"),
                dictInput.get("order"),
                dictInput.get("filterType"),
                dictInput.get("frequencyValue"),
                dictInput.get("frequencyUnit"),
                round(k, 2)))

    def focus(self):
        pass
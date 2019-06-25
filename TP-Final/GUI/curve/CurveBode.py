import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi, sqrt, power

class CurveBode(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, text="Diagrama de Bode", font=config.SMALL_FONT, bg="#ffffff")
        self.title.grid(row=0, column=0, columnspan=6, ipady=7, sticky=N)

        plt.rc('text', usetex=False)

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
        self.labelFrequencyAxis = tk.Label(self, width=15, text="Eje de frecuencia", font=config.SMALL_FONT, bg="#ffffff")

        self.HzAxisButton = tk.Button(  self, width=8, text="Hz", relief=FLAT,      
        font=config.SMALL_FONT, command=self.HzAxisButtonPressed, bg="#ffffff")
        self.radsAxisButton = tk.Button(self, width=8, text="rad/sec", 
        font=config.SMALL_FONT, command=self.radsAxisButtonPressed)

        self.labelGainAxis = tk.Label(self, width=15, text="Eje de ganancia", font=config.SMALL_FONT, bg="#ffffff")

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
        self.ax1.set_xlabel("Pulsación (Hz)")
        self.ax2.set_xlabel("Pulsación (Hz)")
        self.gainAxisdBActivated = True
        self.dataPlot.draw()

    ###############################################
    #    Axis Units Buttons' Callback Functions   #
    ###############################################

    def HzAxisButtonPressed(self):
        self.HzAxisButton.config(  relief=FLAT,   bg="#ffffff")
        self.radsAxisButton.config(relief=RAISED, bg="#f0f0f0")
        self.freqAxisUnitFactor = 1 / (2 * pi)
        self.simulate()
        self.ax1.set_xlabel("Frecuencia (Hz)")
        self.ax2.set_xlabel("Frecuencia (Hz)")
        self.dataPlot.draw()

    def radsAxisButtonPressed(self):
        self.HzAxisButton.config(  relief=RAISED, bg="#f0f0f0")
        self.radsAxisButton.config(relief=FLAT,   bg="#ffffff")
        self.freqAxisUnitFactor = 1
        self.simulate()
        self.ax1.set_xlabel("Pulsación (rad/s)")
        self.ax2.set_xlabel("Pulsación (rad/s)")
        self.dataPlot.draw()

    def dBAxisButtonPressed(self):
        self.dBAxisButton.config(   relief=FLAT,   bg="#ffffff")
        self.timesAxisButton.config(relief=RAISED, bg="#f0f0f0")
        self.gainAxisdBActivated = True
        self.simulate()
        self.ax1.set_ylabel("Gain (dB)")
        self.dataPlot.draw()

    def timesAxisButtonPressed(self):
        self.dBAxisButton.config(   relief=RAISED, bg="#f0f0f0")
        self.timesAxisButton.config(relief=FLAT,   bg="#ffffff")
        self.gainAxisdBActivated = False
        self.simulate()
        self.ax1.set_ylabel("Gain (Veces)")
        self.dataPlot.draw()
              
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
                if (gainParamType == "gainBW" ):
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

            ################################
            #   System's Bode generation   #
            ################################
            # Draw the Bode graph taking 1000 values between 1Hz and 10MHz
            bode = dict()
            bode["w"], bode["gain"], bode["arg"] = signal.bode(sys)    

            freqAxis =  bode["w"] * self.freqAxisUnitFactor

        except(TypeError):
            self.title.config(text="Se tiene que configurar todos los parametros del sistema.", fg="#ff0000")
        else:
            self.title.config(text="", fg="#000000")

            if self.gainAxisdBActivated :
                gainAxis = bode["gain"]

            else :
                gainAxis = []
                for values in bode["gain"] :
                    gainAxis.append(power(10, values / 20))

            ########################################
            #   Gain and Argument plot functions   #
            ########################################
            self.ax1.clear()
            plt.rc('text', usetex=False)
            self.ax1.semilogx(freqAxis, gainAxis, color="red")   
            self.ax1.minorticks_on()
            self.ax1.set_xlabel("Pulsación (Hz)")
            self.ax1.set_ylabel("Gain (dB)")
            self.ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            self.ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            self.ax2.clear()
            plt.rc('text', usetex=False)
            self.ax2.semilogx(freqAxis, bode["arg"], color="purple")
            self.ax2.minorticks_on()
            self.ax2.set_xlabel("Pulsación (Hz)")
            self.ax2.set_ylabel("Fase (°)")
            self.ax2.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            self.ax2.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            self.dataPlot.draw()

            self.title.config(text="Bode : {} order {}, f0 = {}{}, G = {}.".format(
                dictInput.get("order"),
                dictInput.get("filterType"),
                dictInput.get("frequencyValue"),
                dictInput.get("frequencyUnit"), 
                round(k, 2)))

    def focus(self):
        pass
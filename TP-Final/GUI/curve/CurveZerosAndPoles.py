import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi, sqrt

class CurveZerosAndPoles(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, text="Diagrama de Ceros y Polos", font=config.SMALL_FONT, bg="#ffffff")
        self.title.grid(row=0, column=0, ipady=7, sticky=N)

        ####################################
        #   Zeros and Poles Graph Canvas   #
        ####################################

        self.graphZerosAndPoles = Canvas(self)
        self.fig, self.ax = plt.subplots(nrows=1, sharex=True, figsize=(6.3, 5))
        self.fig.subplots_adjust(top=0.95, right=0.95, bottom=0.12, hspace=0.30)
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graphZerosAndPoles)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graphZerosAndPoles)
        self.nav.config(bg="#ffffff")
        self.nav._message_label.config(bg="#ffffff", fg="#ff0000")
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graphZerosAndPoles.grid(row=1, column=0, sticky=N)

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
            global num
            global den
            # First Order Systems
            if dictInput["order"] == "Primer":

                # Gain Param
                k = dictInput.get("gainBW")

                # Low Pass Filter
                if dictInput["filterType"] == "Pasa bajos":
                    num = [k * w0]
                    den = [1, w0]
                # High Pass Filter
                elif dictInput["filterType"] == "Pasa altos":
                    num = [k, 0] 
                    den = [1, w0]
                # All Pass Filter
                elif dictInput["filterType"] == "Pasa todo":
                    num = [k, -k * w0]
                    den = [1, w0]

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
                    num = [k * w0 * w0]
                    den = [1, 2 * xi * w0, w0 * w0]
                # High Pass Filter
                elif dictInput["filterType"] == "Pasa altos":
                    num = [k, 0, 0]
                    den = [1, 2 * xi * w0, w0 * w0]
                # All Pass Filter
                elif dictInput["filterType"] == "Pasa todo":
                    num = [k, -2 * k * xi * w0,  k * w0 * w0]
                    den = [1, 2 * xi * w0, w0 * w0]
                # Band Pass Filter
                elif dictInput["filterType"] == "Pasa banda":
                    num = [0, 2* xi * k * w0, 0]
                    den = [1, 2 * xi * w0, w0 * w0]
                # Single Notch
                elif dictInput["filterType"] == "Single Notch":
                    num = [k, 0 , k * w0 * w0]
                    den = [1, 2 * xi * w0, w0 * w0]
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
                        num = [(k * wp * wp) / (wz * wz), (2* k * xiz * wp * wp) / wz, k * wp * wp]
                        den = [1, 2 * xip * wp, wp * wp]
                    else :
                        num = [k, 2* k * xiz * wz, k * wz * wz]
                        den = [1, 2 * xip * wp, wp * wp]

            ################################
            #   System's Bode generation   #
            ################################
            # Draw the Bode graph taking 1000 values between 1Hz and 10MHz
            zpk = dict()
            zpk["zeros"], zpk["poles"], zpk["gain"] = signal.tf2zpk(num, den)  

            #print(zpk["zeros"], zpk["poles"])  

        except(TypeError):
            self.title.config(text="Se tiene que configurar todos los parametros del sistema.", fg="#ff0000")
        else:
            self.title.config(text="", fg="#000000")

            ######################################
            #   Zeros and poles plot functions   #
            ######################################
            self.ax.clear()
            
            self.ax.plot(zpk["zeros"].real, zpk["zeros"].imag, "ro", color="g", label="Zeros")
            self.ax.plot(zpk["poles"].real, zpk["poles"].imag, "x", color="r", label="Poles")
            self.ax.legend()

            #self.ax.set_aspect('equal')
            #m = max(max(abs(zpk["zeros"].real), abs(zpk["poles"].real)), max(abs(zpk["zeros"].imag), abs(zpk["poles"].imag)))
            #print(m)
            #self.ax.set_xlim(-1.1*m, 1.1*m)
            #self.ax.set_ylim(-1.1*m, 1.1*m)

            self.ax.minorticks_on()
            self.ax.set_xlabel("Eje Real")
            self.ax.set_ylabel("Eje Imaginario")
            self.ax.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            self.ax.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            self.dataPlot.draw()

            self.title.config(text="Zeros and Poles : {} order {}, f0 = {}{}, G = {}.".format(
                dictInput.get("order"),
                dictInput.get("filterType"),
                dictInput.get("frequencyValue"),
                dictInput.get("frequencyUnit"),
                dictInput.get("gainBW")))

    def focus(self):
        pass
import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib

class MenuSecondOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, width=55, text="Seleccionar el filtro de segundo orden",
            font=config.SMALL_FONT, background="#ffe4c4")

        self.title.grid(row=0, column=0, columnspan=5, ipadx=3, ipady=5, sticky=N+E+W)

        ###################################
        #   Filter Type Inline Selector   #
        ###################################

        # Widgets Definition
        self.buttonLowPass = tk.Button(
            self, width=8, text="Pasa bajos", font=config.SMALL_FONT, command=self.buttonLowPassPressed)
        self.buttonHighPass =tk.Button(
            self, width=8, text="Pasa altos",font=config.SMALL_FONT, command=self.buttonHighPassPressed)
        self.buttonAllPass = tk.Button(
            self, width=8, text="Pasa todo", font=config.SMALL_FONT, command=self.buttonAllPassPressed)
        self.buttonBandPass = tk.Button(
            self, width=8, text="Pasa banda", font=config.SMALL_FONT, command=self.buttonBandPassPressed)
        self.buttonSingNotch = tk.Button(
            self, width=8, text="Notch", font=config.SMALL_FONT, command=self.buttonSingNotchPressed)
        self.buttonMultNotch = tk.Button(
            self, width=8, text="H-L Notch", font=config.SMALL_FONT, command=self.buttonMultNotchPressed)

        # Widgets Placement
        self.buttonLowPass.grid(  row=1, column=1, ipadx=3, pady=5)
        self.buttonHighPass.grid( row=1, column=2, ipadx=3)
        self.buttonAllPass.grid(  row=1, column=3, ipadx=3)
        self.buttonBandPass.grid( row=2, column=1, ipadx=3, pady=5)
        self.buttonSingNotch.grid(row=2, column=2, ipadx=3)
        self.buttonMultNotch.grid(row=2, column=3, ipadx=3)

        #####################################
        #   General Filter Formula Canvas   #
        #####################################

        self.graphFilter = Canvas(self)
        self.figFilter = matplotlib.figure.Figure(figsize=(5, 1))
        self.figFilter.patch.set_facecolor("#ffe4c4")
        self.axFilter = self.figFilter.add_subplot(111)
        self.canvasFilter = FigureCanvasTkAgg(self.figFilter, master=self.graphFilter)      
        self.canvasFilter.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvasFilter._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.graphFilter.grid(row=3, column=0, columnspan=5, sticky=N)

        self.axFilter.get_xaxis().set_visible(False)
        self.axFilter.get_yaxis().set_visible(False)
        for sides in ['top','bottom','left','right']:
            self.axFilter.spines[sides].set_visible(False)
        self.axFilter.set_facecolor("#ffe4c4")

        #################################
        #   Frequency Inline Selector   #
        #################################

        # Widgets Definition
        self.graphOmega = Canvas(self)
        plt.rc('text', usetex=True)
        self.figOmega = matplotlib.figure.Figure(figsize=(0.5, 0.5))
        self.figOmega.patch.set_facecolor("#ffe4c4")
        self.axOmega = self.figOmega.add_subplot(111)
        self.canvasOmega = FigureCanvasTkAgg(self.figOmega, master=self.graphOmega)      
        self.canvasOmega.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvasOmega._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.axOmega.get_xaxis().set_visible(False)
        self.axOmega.get_yaxis().set_visible(False)
        for sides in ['top','bottom','left','right']:
            self.axOmega.spines[sides].set_visible(False)
        self.axOmega.set_facecolor("#ffe4c4")
        self.axOmega.text(0.25, 0.3, "$\displaystyle f_P$", fontsize = 20)  
        plt.rc('text', usetex=False)

        self.entryFrequency = tk.Entry(self, width=8)

        self.HzUnitButton = tk.Button( self, width=8, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitButtonPressed)
        self.kHzUnitButton = tk.Button(self, width=8, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitButtonPressed)
        self.MHzUnitButton = tk.Button(self, width=8, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitButtonPressed)

        # Widgets Placement
        self.graphOmega.grid(    row=4, column=0, sticky=N)
        self.entryFrequency.grid(row=4, column=1, sticky=E, ipadx=10)

        self.HzUnitButton.grid( row=4, column=2)
        self.kHzUnitButton.grid(row=4, column=3)
        self.MHzUnitButton.grid(row=4, column=4)

        ###########################################
        #   Damping Coefficient Inline Selector   #
        ###########################################
        
        # Widgets Definition
        self.graphDampCoeff = Canvas(self)
        plt.rc('text', usetex=True)
        self.figDampCoeff = matplotlib.figure.Figure(figsize=(0.8, 0.5))
        self.figDampCoeff.patch.set_facecolor("#ffe4c4")
        self.axDampCoeff = self.figDampCoeff.add_subplot(111)
        self.canvasDampCoeff = FigureCanvasTkAgg(self.figDampCoeff, master=self.graphDampCoeff)      
        self.canvasDampCoeff.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvasDampCoeff._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.axDampCoeff.get_xaxis().set_visible(False)
        self.axDampCoeff.get_yaxis().set_visible(False)
        for sides in ['top','bottom','left','right']:
            self.axDampCoeff.spines[sides].set_visible(False)
        self.axDampCoeff.set_facecolor("#ffe4c4")
        self.axDampCoeff.text(0.25, 0.3, "$\\xi$", fontsize = 15)  
        plt.rc('text', usetex=False)

        self.entryDampCoeff = tk.Entry(self, width=8)
        self.buttonDampCoeff = tk.Button(self, width=8, text="Enviar", font=config.SMALL_FONT, command=self.buttonDampCoeffPressed)

        # Widgets Placement
        self.graphDampCoeff.grid( row=5, column=0, sticky=N)
        self.entryDampCoeff.grid( row=5, column=1, sticky=E, ipadx=10)
        self.buttonDampCoeff.grid(row=5, column=2)

        ######################################
        #   Gain Parameter Inline Selector   #
        ######################################
        
        # Widgets Definition
        self.graphGainParam = Canvas(self)
        plt.rc('text', usetex=True)
        self.figGainParam = matplotlib.figure.Figure(figsize=(0.8, 0.5))
        self.figGainParam.patch.set_facecolor("#ffe4c4")
        self.axGainParam = self.figGainParam.add_subplot(111)
        self.canvasGainParam = FigureCanvasTkAgg(self.figGainParam, master=self.graphGainParam)      
        self.canvasGainParam.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvasGainParam._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.axGainParam.get_xaxis().set_visible(False)
        self.axGainParam.get_yaxis().set_visible(False)
        for sides in ['top','bottom','left','right']:
            self.axGainParam.spines[sides].set_visible(False)
        self.axGainParam.set_facecolor("#ffe4c4")
        self.axGainParam.text(0.25, 0.3, "$\displaystyle G_{BP\ }$", fontsize = 15)
        plt.rc('text', usetex=False)

        self.entryGainParam = tk.Entry(self, width=8)
        self.buttonGainParam = tk.Button(self, width=8, text="Enviar", font=config.SMALL_FONT, command=self.buttonGainParamPressed)

        # Widgets Placement
        self.graphGainParam.grid( row=6, column=0, sticky=N)
        self.entryGainParam.grid( row=6, column=1, sticky=E, ipadx=10)
        self.buttonGainParam.grid(row=6, column=2)

        ################################################
        #   Transient Parameter Type Inline Selector   #
        ################################################

        # Widgets Definition
        self.buttonGainBW = tk.Button(     self, width=30, text="Ganancia de banda pasante",
        font=config.SMALL_FONT, command=self.buttonGainBWPressed, relief=FLAT, bg="#ffe4c4")
        self.buttonGainMax = tk.Button(self, width=20, text="Ganancia máxima", 
        font=config.SMALL_FONT, command=self.buttonGainMaxPressed)

        # Widgets Placement
        self.buttonGainBW.grid(     row=7, column=0, columnspan=3)  
        self.buttonGainMax.grid(row=7, column=3, columnspan=2)        

        #self.insertMNParamText = tk.Label(
            #self, width=55, text="For the multiple Notch, insert the parameters below",
            #font=config.SMALL_FONT, background="#ffe4c4")

        #self.insertMNParamText.grid(row=6, column=0, columnspan=5, ipadx=3, ipady=5, sticky=N+E+W)

        dictInput["filterType"] = "Pasa bajos"

        ############################################
        #   Notch Zero Frequency Inline Selector   #
        ############################################

        # Widgets Definition
        #self.labelNZFrequency = tk.Label(self, width=8, text="Zero Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
        #self.entryNZFrequency = tk.Entry(self, width=8)

        #self.HzUnitNZButton = tk.Button( self, width=8, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitNZButtonPressed)
        #self.kHzUnitNZButton = tk.Button(self, width=8, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitNZButtonPressed)
        #self.MHzUnitNZButton = tk.Button(self, width=8, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitNZButtonPressed)

        # Widgets Placement
        #self.labelNZFrequency.grid(row=7, column=0, sticky=W, ipady=10)
        #self.entryNZFrequency.grid(row=7, column=1, sticky=E, ipadx=10)

        #self.HzUnitNZButton.grid( row=7, column=2)
        #self.kHzUnitNZButton.grid(row=7, column=3)
        #self.MHzUnitNZButton.grid(row=7, column=4)

        ######################################################
        #   Notch Zero Damping Coefficient Inline Selector   #
        ######################################################
        
        # Widgets Definition
        #self.labelNZDampCoeff = tk.Label(self, width=8, text="Damping Coeff", font=config.SMALL_FONT, bg="#ffe4c4")
        #self.entryNZDampCoeff = tk.Entry(self, width=8)
        #self.buttonNZDampCoeff = tk.Button(self, width=8, text="Send", font=config.SMALL_FONT, command=self.buttonNZDampCoeffPressed)

        # Widgets Placement
        #self.labelNZDampCoeff.grid( row=8, column=0, sticky=W, ipady=10)
        #self.entryNZDampCoeff.grid( row=8, column=1, sticky=E, ipadx=10)
        #self.buttonNZDampCoeff.grid(row=8, column=2)

        ############################################
        #   Notch Pole Frequency Inline Selector   #
        ############################################

        # Widgets Definition
        #self.labelNPFrequency = tk.Label(self, width=8, text="Pole Frequency", font=config.SMALL_FONT, bg="#ffe4c4")
        #self.entryNPFrequency = tk.Entry(self, width=8)

        #self.HzUnitNPButton = tk.Button( self, width=8, text="Hz",  font=config.SMALL_FONT, command=self.HzUnitNPButtonPressed)
        #self.kHzUnitNPButton = tk.Button(self, width=8, text="kHz", font=config.SMALL_FONT, command=self.kHzUnitNPButtonPressed)
        #self.MHzUnitNPButton = tk.Button(self, width=8, text="MHz", font=config.SMALL_FONT, command=self.MHzUnitNPButtonPressed)

        # Widgets Placement
        #self.labelNPFrequency.grid(row=9, column=0, sticky=W, ipady=10)
        #self.entryNPFrequency.grid(row=9, column=1, sticky=E, ipadx=10)

        #self.HzUnitNPButton.grid( row=9, column=2)
        #self.kHzUnitNPButton.grid(row=9, column=3)
        #self.MHzUnitNPButton.grid(row=9, column=4)

        ######################################################
        #   Notch Pole Damping Coefficient Inline Selector   #
        ######################################################
        
        # Widgets Definition
        #self.labelNPDampCoeff = tk.Label(self, width=15, text="Damping Coeff", font=config.SMALL_FONT, bg="#ffe4c4")
        #self.entryNPDampCoeff = tk.Entry(self, width=5)
        #self.buttonNPDampCoeff = tk.Button(self, width=8, text="Send", font=config.SMALL_FONT, command=self.buttonNPDampCoeffPressed)

        # Widgets Placement
        #self.labelNPDampCoeff.grid( row=10, column=0, sticky=W, ipady=10)
        #self.entryNPDampCoeff.grid( row=10, column=1, sticky=E, ipadx=10)
        #self.buttonNPDampCoeff.grid(row=10, column=2)

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

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac{\ 1 \ }\
            {(\\frac{s}{\omega_P})^2+2\cdot\\xi\cdot(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.12, 0.1, self.filterText, fontsize = 15) 
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Pasa bajos"
    
    def buttonHighPassPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac{\ s^2 \ }\
            {(\\frac{s}{\omega_P})^2+2\cdot\\xi\cdot(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.12, 0.1, self.filterText, fontsize = 15) 
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Pasa altos"

    def buttonAllPassPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=FLAT,   bg="#ffe4c4")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac\
            {(\\frac{s}{\omega_P})^2-2\cdot\\xi\cdot(\\frac{s}{\omega_P})+1}\
            {(\\frac{s}{\omega_P})^2+2\cdot\\xi\cdot(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.12, 0.1, self.filterText, fontsize = 15) 
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Pasa todo"

    def buttonBandPassPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac{\ s \ }\
            {(\\frac{s}{\omega_P})^2+2\cdot\\xi\cdot(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.12, 0.1, self.filterText, fontsize = 15) 
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Pasa banda"
    
    def buttonSingNotchPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=FLAT,   bg="#ffe4c4")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac{(\\frac{s}{\omega_P})^2+1}\
            {(\\frac{s}{\omega_P})^2+2\cdot\\xi\cdot(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.12, 0.1, self.filterText, fontsize = 15) 
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Single Notch"

    def buttonMultNotchPressed(self):
        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=FLAT,   bg="#ffe4c4")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac\
            {(\\frac{s}{\omega_Z})^2\pm 2\cdot\\xi\cdot(\\frac{s}{\omega_Z})+1}\
            {(\\frac{s}{\omega_P})^2+2\cdot\\xi\cdot(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.12, 0.1, self.filterText, fontsize = 15) 
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Multiple Notch"  

    #################################################
    #   Frequency Unit Buttons' Callback Functions  #
    #################################################

    def HzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=FLAT,   bg="#ffe4c4")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        try:
            dictInput["frequencyValue"] = float(self.entryFrequency.get())
        except(ValueError):
            self.title.config(text="Entregar una frecuencia de corte que sea de tipo float", fg="#ff0000")
            self.HzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        dictInput["frequencyUnit"] = "Hz"
        dictInput["frequencyUnitFactor"] = 1

    def kHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        try:
            dictInput["frequencyValue"] = float(self.entryFrequency.get())
        except(ValueError):
            self.title.config(text="Entregar una frecuencia de corte que sea de tipo float", fg="#ff0000")
            self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        dictInput["frequencyUnit"] = "kHz"
        dictInput["frequencyUnitFactor"] = 1000

    def MHzUnitButtonPressed(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=FLAT,   bg="#ffe4c4")

        try:
            dictInput["frequencyValue"] = float(self.entryFrequency.get())
        except(ValueError):
            self.title.config(text="Entregar una frecuencia de corte que sea de tipo float", fg="#ff0000")
            self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        dictInput["frequencyUnit"] = "MHz"
        dictInput["frequencyUnitFactor"] = 1000000
    
    ############################################################
    #   Notch Zero Frequency Unit Buttons' Callback Functions  #
    ############################################################

    #def HzUnitNZButtonPressed(self):
        #self.HzUnitNZButton.config( relief=FLAT,   bg="#ffe4c4")
        #self.kHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        #self.MHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")

        #try:
            #dictInput["frequencyNZValue"] = float(self.entryNZFrequency.get())
        #except(ValueError):
            #self.title.config(text="Please insert a float cutoff zero frequency value", fg="#ff0000")
            #self.HzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        #else:
            #self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        #dictInput["frequencyNZUnitFactor"] = 1

    #def kHzUnitNZButtonPressed(self):
        #self.HzUnitNZButton.config( relief=RAISED, bg="#f0f0f0")
        #self.kHzUnitNZButton.config(relief=FLAT,   bg="#ffe4c4")
        #self.MHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")

        #try:
            #dictInput["frequencyNZValue"] = float(self.entryNZFrequency.get())
        #except(ValueError):
            #self.title.config(text="Please insert a float cutoff zero frequency value", fg="#ff0000")
            #self.kHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        #else:
            #self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        #dictInput["frequencyNZUnitFactor"] = 1000

    #def MHzUnitNZButtonPressed(self):
        #self.HzUnitNZButton.config( relief=RAISED, bg="#f0f0f0")
        #self.kHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        #self.MHzUnitNZButton.config(relief=FLAT,   bg="#ffe4c4")

        #try:
            #dictInput["frequencyNZValue"] = float(self.entryNZFrequency.get())
        #except(ValueError):
            #self.title.config(text="Please insert a float cutoff zero frequency value", fg="#ff0000")
            #self.MHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        #else:
            #self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        #dictInput["frequencyNZUnitFactor"] = 1000000

    ############################################################
    #   Notch Pole Frequency Unit Buttons' Callback Functions  #
    ############################################################

    #def HzUnitNPButtonPressed(self):
        #self.HzUnitNPButton.config( relief=FLAT,   bg="#ffe4c4")
        #self.kHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        #self.MHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")

        #try:
            #dictInput["frequencyNPValue"] = float(self.entryNPFrequency.get())
        #except(ValueError):
            #self.title.config(text="Please insert a float cutoff pole frequency value", fg="#ff0000")
            #self.HzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        #else:
            #self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        #dictInput["frequencyNPUnitFactor"] = 1

    #def kHzUnitNPButtonPressed(self):
        #self.HzUnitNPButton.config( relief=RAISED, bg="#f0f0f0")
        #self.kHzUnitNPButton.config(relief=FLAT,   bg="#ffe4c4")
        #self.MHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")

        #try:
            #dictInput["frequencyNPValue"] = float(self.entryNPFrequency.get())
        #except(ValueError):
            #self.title.config(text="Please insert a float cutoff pole frequency value", fg="#ff0000")
            #self.kHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        #else:
            #self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        #dictInput["frequencyNPUnitFactor"] = 1000

    #def MHzUnitNPButtonPressed(self):
        #self.HzUnitNPButton.config( relief=RAISED, bg="#f0f0f0")
        #self.kHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        #self.MHzUnitNPButton.config(relief=FLAT,   bg="#ffe4c4")

        #try:
            #dictInput["frequencyNPValue"] = float(self.entryNPFrequency.get())
        #except(ValueError):
            #self.title.config(text="Please insert a float cutoff pole frequency value", fg="#ff0000")
            #self.MHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        #else:
            #self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

        #dictInput["frequencyNPUnitFactor"] = 1000000

    ##############################################
    #   Gain Parameter Button Callback Function  #
    ##############################################

    def buttonGainParamPressed(self):
        self.buttonGainParam.config(relief=FLAT, bg="#ffe4c4")
        try:
            dictInput["gainParam"] = float(self.entryGainParam.get())
        except(ValueError):
            self.title.config(text="Entregar una ganancia de BP que sea de tipo float", fg="#ff0000")
            self.buttonGainParam.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

    ###########################################################
    #   Gain Parameter Type Buttons' Callback Functions  #
    ###########################################################

    def buttonGainBWPressed(self):
        self.buttonGainBW.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonGainMax.config(relief=RAISED, bg="#f0f0f0")
        self.axGainParam.clear()
        plt.rc('text', usetex=True)
        self.axGainParam.text(0.25, 0.3, "$\displaystyle G_{BP\ }$", fontsize = 15)
        self.canvasGainParam.draw()
        plt.rc('text', usetex=False)
        dictInput["gainParamType"] = "gainBW"

    def buttonGainMaxPressed(self):
        self.buttonGainMax.config(relief=FLAT,   bg="#ffe4c4")
        self.buttonGainBW.config(     relief=RAISED, bg="#f0f0f0")
        self.axGainParam.clear()
        plt.rc('text', usetex=True)
        self.axGainParam.text(0.25, 0.3, "$\displaystyle G_{MAX\ }$", fontsize = 15)  
        self.canvasGainParam.draw()
        plt.rc('text', usetex=False)
        dictInput["gainParamType"] = "gainMax"

    ##############################################################
    #   Notch Zero Damping Coefficient Button Callback Function  #
    ##############################################################

    #def buttonNZDampCoeffPressed(self):
        #self.buttonNZDampCoeff.config(relief=FLAT, bg="#ffe4c4")
        #dictInput["NZdampCoeff"] = float(self.entryNZDampCoeff.get())

    ##############################################################
    #   Notch Pole Damping Coefficient Button Callback Function  #
    ##############################################################

    #def buttonNPDampCoeffPressed(self):
        #self.buttonNPDampCoeff.config(relief=FLAT, bg="#ffe4c4")
        #dictInput["NPdampCoeff"] = float(self.entryNPDampCoeff.get())

    ######################################################
    #   Damping Coefficient Buttons' Callback Functions  #
    ######################################################

    def buttonDampCoeffPressed(self):
        self.buttonDampCoeff.config(relief=FLAT, bg="#ffe4c4")
        try:
            dictInput["dampCoeff"] = float(self.entryDampCoeff.get())
        except(ValueError):
            self.title.config(text="Entregar una ganancia de BP que sea de tipo float", fg="#ff0000")
            self.buttonDampCoeff.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Seleccionar el filtro de segundo orden", fg="#000000")

    ######################################
    #   Reset Buttons' Relief Function   #
    ######################################

    def resetButtons(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        # self.HzUnitNZButton.config( relief=RAISED, bg="#f0f0f0")
        # self.kHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")
        # self.MHzUnitNZButton.config(relief=RAISED, bg="#f0f0f0")

        # self.HzUnitNPButton.config( relief=RAISED, bg="#f0f0f0")
        # self.kHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")
        # self.MHzUnitNPButton.config(relief=RAISED, bg="#f0f0f0")

        self.buttonLowPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config(  relief=RAISED, bg="#f0f0f0")
        self.buttonBandPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonSingNotch.config(relief=RAISED, bg="#f0f0f0")
        self.buttonMultNotch.config(relief=RAISED, bg="#f0f0f0")

        self.buttonDampCoeff.config( relief=RAISED, bg="#f0f0f0")
        # self.buttonNZDampCoeff.config(relief=RAISED, bg="#f0f0f0")
        # self.buttonNPDampCoeff.config(relief=RAISED, bg="#f0f0f0")

        self.buttonGainParam.config(relief=RAISED, bg="#f0f0f0")

    def focus(self):
        pass
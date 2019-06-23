import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib

class MenuFirstOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self, width=55, text="Seleccionar el filtro de primer orden",
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

        # Widgets Placement
        self.buttonLowPass.grid( row=1, column=1, ipadx=3)
        self.buttonHighPass.grid(row=1, column=2, ipadx=3)
        self.buttonAllPass.grid( row=1, column=3, ipadx=3)

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
        self.graphFilter.grid(row=2, column=0, columnspan=5, sticky=N)

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
        self.graphOmega.grid(row=3, column=0, sticky=N)
        self.entryFrequency.grid(row=3, column=1, sticky=E, ipadx=10)

        self.HzUnitButton.grid( row=3, column=2)
        self.kHzUnitButton.grid(row=3, column=3)
        self.MHzUnitButton.grid(row=3, column=4)

        ######################################
        #   BandWidth Gain Inline Selector   #
        ######################################
        
        # Widgets Definition
        self.graphGainBW = Canvas(self)
        plt.rc('text', usetex=True)
        self.figGainBW = matplotlib.figure.Figure(figsize=(0.8, 0.5))
        self.figGainBW.patch.set_facecolor("#ffe4c4")
        self.axGainBW = self.figGainBW.add_subplot(111)
        self.canvasGainBW = FigureCanvasTkAgg(self.figGainBW, master=self.graphGainBW)      
        self.canvasGainBW.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvasGainBW._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.axGainBW.get_xaxis().set_visible(False)
        self.axGainBW.get_yaxis().set_visible(False)
        for sides in ['top','bottom','left','right']:
            self.axGainBW.spines[sides].set_visible(False)
        self.axGainBW.set_facecolor("#ffe4c4")
        self.axGainBW.text(0.25, 0.3, "$\displaystyle G_{BP\ }$", fontsize = 15)  
        plt.rc('text', usetex=False)

        self.entryGainBW = tk.Entry(self, width=8)
        self.buttonGainBW = tk.Button(self, width=8, text="Enviar", font=config.SMALL_FONT, command=self.buttonGainBWPressed)

        # Widgets Placement
        self.graphGainBW.grid( row=4, column=0, sticky=N)
        self.entryGainBW.grid( row=4, column=1, sticky=E, ipadx=10)
        self.buttonGainBW.grid(row=4, column=2)

        ################################
        #   Describe Parameters Line   #
        ################################

        # Widgets Definition
        self.graphDescribe = Canvas(self)
        plt.rc('text', usetex=True)
        self.figDescribe = matplotlib.figure.Figure(figsize=(5, 0.5))
        self.figDescribe.patch.set_facecolor("#ffe4c4")
        self.axDescribe = self.figDescribe.add_subplot(111)
        self.canvasDescribe = FigureCanvasTkAgg(self.figDescribe, master=self.graphDescribe)      
        self.canvasDescribe.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvasDescribe._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.axDescribe.get_xaxis().set_visible(False)
        self.axDescribe.get_yaxis().set_visible(False)
        for sides in ['top','bottom','left','right']:
            self.axDescribe.spines[sides].set_visible(False)
        self.axDescribe.set_facecolor("#ffe4c4")
        self.axDescribe.text(0, 0, "$\displaystyle f_P=2\pi\omega_P\ \ \
            ;\ \ G_{BP\ }$: ganancia de banda pasante", fontsize = 14)  
        plt.rc('text', usetex=False)   

        # Widgets Placement
        self.graphDescribe.grid( row=5, column=0, columnspan=5, sticky=N)   

    ##############################################
    #   Filter Type Buttons' Callback Functions  #
    ##############################################

    def buttonLowPassPressed(self):
        self.buttonLowPass.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonHighPass.config(relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config( relief=RAISED, bg="#f0f0f0")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac{\ 1\ }{(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.25, 0.1, self.filterText, fontsize = 15)  
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Pasa bajos"
    
    def buttonHighPassPressed(self):
        self.buttonLowPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config(relief=FLAT,   bg="#ffe4c4")
        self.buttonAllPass.config( relief=RAISED, bg="#f0f0f0")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac{\ s\ }{(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.25, 0.1, self.filterText, fontsize = 15)  
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Pasa altos"

    def buttonAllPassPressed(self):
        self.buttonLowPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config(relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config( relief=FLAT,   bg="#ffe4c4")

        self.axFilter.clear()
        plt.rc('text', usetex=True)
        self.filterText = "$\displaystyle H(s)=K\cdot\\frac{(\\frac{s}{\omega_P})-1}{(\\frac{s}{\omega_P})+1}$"
        self.axFilter.text(0.25, 0.1, self.filterText, fontsize = 15) 
        self.canvasFilter.draw()
        plt.rc('text', usetex=False)

        dictInput["filterType"] = "Pasa todo"

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
            self.title.config(text="Seleccionar el filtro de primer orden", fg="#000000")

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
            self.title.config(text="Seleccionar el filtro de primer orden", fg="#000000")

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
            self.title.config(text="Seleccionar el filtro de primer orden", fg="#000000")

        dictInput["frequencyUnit"] = "MHz"
        dictInput["frequencyUnitFactor"] = 1000000
    
    ###############################################
    #   Bandwidth Gain Button Callback Function   #
    ###############################################

    def buttonGainBWPressed(self):
        self.buttonGainBW.config(relief=FLAT, bg="#ffe4c4")
        try:
            dictInput["gainBW"] = float(self.entryGainBW.get())
        except(ValueError):
            self.title.config(text="Entregar una ganancia de BP que sea de tipo float", fg="#ff0000")
            self.buttonGainBW.config(relief=RAISED, bg="#f0f0f0")
        else:
            self.title.config(text="Seleccionar el filtro de primer orden", fg="#000000")

    ######################################
    #   Reset Buttons' Relief Function   #
    ######################################

    def resetButtons(self):
        self.HzUnitButton.config( relief=RAISED, bg="#f0f0f0")
        self.kHzUnitButton.config(relief=RAISED, bg="#f0f0f0")
        self.MHzUnitButton.config(relief=RAISED, bg="#f0f0f0")

        self.buttonLowPass.config( relief=RAISED, bg="#f0f0f0")
        self.buttonHighPass.config(relief=RAISED, bg="#f0f0f0")
        self.buttonAllPass.config( relief=RAISED, bg="#f0f0f0")

        self.buttonGainBW.config(relief=RAISED, bg="#f0f0f0")

    def focus(self):
        pass
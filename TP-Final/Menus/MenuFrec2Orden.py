import tkinter as tk
import Config
from UserInput import userInput
from Menus.MenuModo import MenuModo
import numpy as np

class MenuFrec2Orden(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
        self.valueF0 = 0
        self.valuex = 0
        self.valuey = 0

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Configuración parámetros Segundo Orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
#
        self.askFrec = tk.Label(          self,
            height=1,
            width=50,
            text="Ingrese frecuencia de corte (kHz)",
            font=Config.LARGE_FONT,
            background="#ffccd5")
        self.answFrec = tk.Entry(self,width=50)

        self.defaultText = tk.StringVar(self)
        self.defaultText.set("Defina el modo")
        self.ddlmode = tk.OptionMenu(self,self.defaultText,"Ganancia de Banda Pasante","Ganancia Máxima")
        self.answDdl = tk.Entry(self,width=50)

        self.asksing = tk.Label(          self,
            height=1,
            width=50,
            text="Ingrese [ω0,Q]",
            font=Config.LARGE_FONT,
            background="#ffccd5")
        self.answOmeg = tk.Entry(self,width=50)
        self.answQ = tk.Entry(self,width=50)
        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.askFrec.pack(side=tk.TOP, pady=30)
        self.answFrec.pack(side=tk.TOP, pady=40)
        self.ddlmode.pack(side=tk.TOP, fill=tk.BOTH)
        self.answDdl.pack(side=tk.TOP, pady=40)
        self.asksing.pack(side=tk.TOP, pady=30)
        self.answOmeg.pack(side=tk.TOP, pady=40)
        self.answQ.pack(side=tk.TOP, pady=40)

        self.buttonContinuar = tk.Button(
            self,
            height=2,
            width=50,
            text="Continuar",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.continuar
        )

        self.buttonContinuar.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

        self.buttonBack = tk.Button(  # Atras
            self,
            height=1,
            width=20,
            text="Back",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuSegundoOrden
        )
        self.buttonBack.pack(side=tk.TOP, fill=tk.BOTH)

    def continuar(self):
        # configuramos modos
        userInput["f0"] = np.asarray((self.answFrec.get())).astype(float) * 1000
        #Esto depende del modo en el que lo pusieron
        userInput["w0"]=self.answOmeg.get()
        userInput["q"] = self.answQ.get()
        #! Tengo que ver algun metodo para verificar el input
        self.controller.showFrame(MenuModo)

    def gotoMenuSegundoOrden(self):
        from Menus.MenuSegundoOrden import MenuSegundoOrden
        self.controller.showFrame(MenuSegundoOrden)

    def focus(self):
        pass

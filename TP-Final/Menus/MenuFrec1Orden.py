import tkinter as tk
import Config
from UserInput import userInput
from Menus.MenuModo import MenuModo
import numpy as np

class MenuFrec1Orden(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Selecciond e parametro 1er orden",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
#
        self.askFrecSing = tk.Label(          self,
            height=1,
            width=50,
            text="Ingrese frecuencia de Polo (kHz)",#mmmm no se si frecuencia
            font=Config.LARGE_FONT,
            background="#ffccd5")
        self.answFrecSing = tk.Entry(self,width=50)
        self.askFrecZero = tk.Label(
            self,
            height=1,
            width=50,
            text="Ingrese frecuencia de cero (kHz)",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        self.answFrecZero = tk.Entry(self,width=50)
        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.askFrecSing.pack(side=tk.TOP, pady=30)
        self.answFrecSing.pack(side=tk.TOP, pady=40)
        self.askFrecZero.pack(side=tk.TOP, fill=tk.BOTH)
        self.answFrecZero.pack(side=tk.TOP, pady=30)
        self.buttonContinuar = tk.Button(
            self,
            height=2,
            width=20,
            text="Continuar",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.continuar
        )
        self.buttonContinuar.pack(side=tk.RIGHT, pady=20 )
        self.buttonBack = tk.Button(  # Atras
            self,
            height=2,
            width=20,
            text="Volver",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuPrimerOrden,
        )
        self.buttonBack.pack(side=tk.LEFT, pady=20)

    def continuar(self):
        # configuramos modos
        userInput["fSing"] = np.asarray((self.answFrecSing.get())).astype(float) * 1000
        userInput["fZero"]=np.asarray((self.answFrecZero.get())).astype(float) * 1000
        self.controller.showFrame(MenuModo)

    def focus(self):
        pass

    def gotoMenuPrimerOrden(self):
        from Menus.MenuPrimerOrden import MenuPrimerOrden
        self.controller.showFrame(MenuPrimerOrden)

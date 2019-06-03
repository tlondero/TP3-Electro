import tkinter as tk
import Config


from UserInput import userInput
from Menus.MenuFrec1Orden import MenuFrec1Orden

class MenuPrimerOrden(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Primer Orden",
            font=Config.SMALL_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttonBack = tk.Button(  # Atras
            self,
            height=1,
            width=20,
            text="Volver",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuSelectOrder
        )
        self.button1LowPass = tk.Button(
            self,
            height=1,
            width=50,
            text="Pasa Bajos",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuPasaBajos

        )
        self.button1HighPass = tk.Button(
            self,
            height=3,
            width=20,
            text="Pasa Altos",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuPasaAltos
        )
        self.button1Singularity = tk.Button(
            self,
            height=3,
            width=20,
            text="Polos y Ceros Arbitrarios",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuArbitrario
        )
        self.button1LowPass.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)
        self.button1HighPass.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)
        self.button1Singularity.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)
        self.buttonBack.pack(side=tk.TOP, fill=tk.BOTH)

    def gotoMenuPasaBajos(self):
        self.controller.showFrame(MenuFrec1Orden)
        userInput["mode"] = "Pasa Bajos"

    def gotoMenuPasaAltos(self):
        self.controller.showFrame(MenuFrec1Orden)
        userInput["mode"] = "Pasa Altos"


    def gotoMenuArbitrario(self):
        self.controller.showFrame(MenuFrec1Orden) #ARREGLAR
        userInput["mode"] = "Polos Arbitrarios"

    def gotoMenuSelectOrder(self):
        from Menus.MenuSelectOrder import MenuSelectOrder
        self.controller.showFrame(MenuSelectOrder)

    def focus(self):
        pass

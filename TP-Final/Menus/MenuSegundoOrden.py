import tkinter as tk
import Config
from Menus.MenuFrec2Orden import MenuFrec2Orden
from UserInput import userInput


class MenuSegundoOrden(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=20,
            text="Segundo Orden",
            font=Config.SMALL_FONT,
            background="#ffccd5"
        )

        self.buttonBack = tk.Button(  # Atras
            self,
            height=1,
            width=20,
            text="Back",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuSelectOrder
        )

        self.button2LowPass = tk.Button( #Pasa bajos
            self,
            height=1,
            width=20,
            text="Pasa Bajos",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuPasaBajos
        )
        self.button2HighPass = tk.Button( #Pasa altos
            self,
            height=1,
            width=20,
            text="Pasa Altos",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuPasaAltos
        )
        self.buttonSingularity = tk.Button( #Polos arbitrarios
            self,
            height=1,
            width=20,
            text="Polos y Ceros Arbitrarios",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuArbitrario
        )

        self.button2HPNotch = tk.Button( #High-Pass Notch
            self,
            height=1,
            width=20,
            text="High-Pass Notch",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuHPNotch
        )
        self.button2NoFilter = tk.Button( #pasa to
            self,
            height=1,
            width=20,
            text="Pasa Todo",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuNoFilter
        )

        self.buttonBandPass = tk.Button( #Pasa banda
            self,
            height=1,
            width=20,
            text="Pasa Banda",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuBandPass
        )

        self.button2Notch = tk.Button( #Notch
            self,
            height=1,
            width=20,
            text="Notch",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuNotch
        )

        self.button2LPNotch = tk.Button( #Low-Pass Notch
            self,
            height=1,
            width=20,
            text="Low-Pass Notch",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuLPNotch
        )
        self.title.pack(side=tk.TOP, fill=tk.BOTH)
        self.button2NoFilter.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.button2LowPass.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.buttonBandPass.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.button2HighPass.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.button2LPNotch.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.button2Notch.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.button2HPNotch.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.buttonSingularity.pack(side=tk.TOP, expand=0, fill=tk.BOTH, pady=20)
        self.buttonBack.pack(side=tk.TOP, fill=tk.BOTH)

    def gotoMenuPasaBajos(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "Pasa Bajos"

    def gotoMenuPasaAltos(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "Pasa Altos"

    def gotoMenuArbitrario(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "Polos Arbitrarios"

    def gotoMenuHPNotch(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "HPNotch"

    def gotoMenuNotch(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "Notch"

    def gotoMenuBandPass(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "Pasa Banda"

    def gotoMenuLPNotch(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "LPNotch"

    def gotoMenuNoFilter(self):
        self.controller.showFrame(MenuFrec2Orden)
        userInput["mode"] = "Pasa Todo"

    def gotoMenuSelectOrder(self):
        from Menus.MenuSelectOrder import MenuSelectOrder
        self.controller.showFrame(MenuSelectOrder)

    def focus(self):
        pass


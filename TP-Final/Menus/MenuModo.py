import tkinter as tk
import Config
#from UserInput import userInput
#from Menus.MenuBode import MenuBode
#from Menus.MenuDiagrama import MenuDiagrama
#from Menus.MenuSignal import MenuSignal

class MenuModo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Modo",
            font=Config.SMALL_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttonBack = tk.Button(  # Atras
            self,
            height=1,
            width=20,
            text="Menu Principal",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuSelectOrder
        )
        self.buttonSignal = tk.Button(
            self,
            height=1,
            width=50,
            text="Señales de Entrada",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuSignal

        )
        self.buttonBode = tk.Button(
            self,
            height=3,
            width=20,
            text="Bode",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuBode
        )
        self.buttonDiagrama = tk.Button(
            self,
            height=3,
            width=20,
            text="Diagrama de Polos y Ceros",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuDiagrama
        )
        self.buttonSignal.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)
        self.buttonBode.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)
        self.buttonDiagrama.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=50)
        self.buttonBack.pack(side=tk.TOP, fill=tk.BOTH)

    def gotoMenuSignal(self):
        pass
 #       self.controller.showFrame(MenuSignal)
 #       userInput["Option"] = "Signal"

    def gotoMenuBode(self):
        pass
#        self.controller.showFrame(MenuBode)
#        userInput["Option"] = "Bode"


    def gotoMenuDiagrama(self):
        pass
#        self.controller.showFrame(MenuDiagrama)
#        userInput["Option"] = "Diagrama"

    def gotoMenuSelectOrder(self):
        from Menus.MenuSelectOrder import MenuSelectOrder
        self.controller.showFrame(MenuSelectOrder)

    def focus(self):
        pass

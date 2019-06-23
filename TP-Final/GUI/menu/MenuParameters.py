import tkinter as tk
from tkinter import *
import config
from userInput import dictInput

from menu.MenuFirstOrder import MenuFirstOrder
from menu.MenuSecondOrder import MenuSecondOrder

orderMenus = [
    MenuFirstOrder,
    MenuSecondOrder
]

class MenuParameters(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        self.controller = controller
        self.parent = parent

        ####################################
        #   System Order Inline Selector   #
        ####################################

        # Widgets Definition
        self.selectOrderText = tk.Label(
            self, width=55, text="Seleccionar el orden del sistema", font=config.SMALL_FONT, bg="#ffe4c4")
        
        self.buttonFirstOrder = tk.Button(
            self, width=27, text="Primer Orden", relief=FLAT,
            font=config.SMALL_FONT, bg="#ffe4c4", command=self.buttonFirstOrderPressed)
        self.buttonSecondOrder = tk.Button(
            self, width=27, text="Segundo Orden",
            font=config.SMALL_FONT, bg="#fff0bc", command=self.buttonSecondOrderPressed)

        # Widgets Placement
        self.selectOrderText.grid(row=0, column=0, columnspan=2, ipadx=2, ipady=5, sticky=E+W)

        self.buttonFirstOrder.grid( row=1, column=0, sticky=W)
        self.buttonSecondOrder.grid(row=1, column=1, sticky=E)

        #########################################
        #   Order Menus Containers Definition   #
        #########################################

        self.containOrderMenu = tk.Frame(self)
        self.containOrderMenu.grid(row=2, column=0, columnspan=2, sticky = E + W + N + S)

        self.orderMenus = {}

        for orderMenu in orderMenus:
            self.orderMenus[orderMenu] = orderMenu(self.containOrderMenu, self)
            self.orderMenus[orderMenu].grid_propagate(True)
            self.orderMenus[orderMenu].grid(row=0, column=0, sticky=E + W + N + S)
            self.orderMenus[orderMenu].config(bg="#ffe4c4")
        
        self.showOrderMenu(MenuFirstOrder)
        dictInput["order"] = "Primer"
     
    ######################################
    #   Order Menus Managing Functions   #
    ######################################

    def showOrderMenu(self, orderMenu):
        self.orderMenus[orderMenu].focus()
        orderMenu = self.orderMenus[orderMenu]
        orderMenu.tkraise()
        self.orderMenu = orderMenu

    def getCurrentOrderMenu(self):
        return self.orderMenu

    ##################################################
    #   Order Selection Buttons' Callback Functions  #
    ##################################################
    
    def buttonFirstOrderPressed(self):
        self.buttonFirstOrder.config( relief=FLAT,   bg="#ffe4c4")
        self.buttonSecondOrder.config(relief=RAISED, bg="#fff0bc")
        dictInput["order"] = "Primer"
        self.showOrderMenu(MenuFirstOrder)

    def buttonSecondOrderPressed(self):
        self.buttonFirstOrder.config( relief=RAISED, bg="#fff0bc")
        self.buttonSecondOrder.config(relief=FLAT,   bg="#ffe4c4")    
        dictInput["order"] = "Segundo"
        self.showOrderMenu(MenuSecondOrder)   

    ######################################
    #   Reset Buttons' Relief Function   #
    ######################################

    def resetButtons(self):
        for orderMenu in orderMenus:
            self.orderMenus[orderMenu].resetButtons()

    def focus(self):
        pass
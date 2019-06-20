import tkinter as tk
from tkinter import *

from menu.MenuMain import MenuMain
from curve.CurveMain import CurveMain

class UI(tk.Tk):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)

        self.protocol('WM_DELETE_WINDOW', self.exitFunction)
        self.title("GuidinVisualizer 3.2.5")
        self.resizable(width=False, height=False)

        self.containMenu  = tk.Frame(self, bd = 1, relief = SUNKEN)
        self.containCurve = tk.Frame(self, bd = 1, relief = SUNKEN)
                                                         
        self.containMenu.grid( row = 0, column = 0, sticky = E+W+N+S)
        self.containCurve.grid(row = 0, column = 1, sticky = E+W+N+S)

        self.menuFrame  = MenuMain(self.containMenu, self)
        self.menuFrame.config(bg="#ffe4c4")
        self.curveFrame = CurveMain(self.containCurve, self)

        self.menuFrame.grid( row = 0, column = 0, sticky = E + W + N + S)
        self.curveFrame.grid(row = 0, column = 0, sticky = E + W + N + S)

        self.menuFrame.focus()

        self.width = 1
        self.height = 1
        self.x_center = 1
        self.y_center = 1

    def run(self):
        self.update_idletasks()
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.x_center = (self.winfo_screenwidth() // 2) - (self.width // 2)
        self.y_center = (self.winfo_screenheight() // 2) - (self.height // 2) - 50

        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x_center, self.y_center))

        self.mainloop()

    def exitFunction(self):
        self.quit()
        self.destroy()

if __name__ == "__main__":
    UI().run()        
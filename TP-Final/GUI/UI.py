import tkinter as tk
from tkinter import *

from menu.MenuMain import MenuMain
from curve.CurveMain import CurveMain

class UI(tk.Tk):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)

        self.protocol('WM_DELETE_WINDOW', self.exitFunction)
        self.title("GuidinVisualizer 3.0.")
        self.resizable(width=False, height=False)

        self.containMenu  = tk.Frame(self, bd = 1, relief = SUNKEN)
        self.containCurve = tk.Frame(self, bd = 1, relief = SUNKEN)

        self.containMenu.grid( row = 0, column = 0, sticky = E + W + N + S)
        self.containCurve.grid(row = 0, column = 1, sticky = E + W + N + S)

        self.menuFrame  = MenuMain(self.containMenu, self)
        self.curveFrame = CurveMain(self.containCurve, self)

        self.menuFrame.grid( row = 0, column = 0, sticky = E + W + N + S)
        self.curveFrame.grid(row = 0, column = 0, sticky = E + W + N + S)

        self.menuFrame.focus()

    def run(self):
        self.mainloop()

    def exitFunction(self):
        self.quit()
        self.destroy()

if __name__ == "__main__":
    UI().run()        
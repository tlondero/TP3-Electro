import tkinter as tk
from tkinter import *
import config

from curve.CurveStepResponse import CurveStepResponse
from curve.CurveBode import CurveBode
from curve.CurveZerosAndPoles import CurveZerosAndPoles

curves = [
    CurveStepResponse,
    CurveBode,
    CurveZerosAndPoles
]

firstCurve = CurveStepResponse

class CurveMain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.buttonStepResponse = tk.Button(
            self,
            width = 22,
            text = "Step Response",
            font = config.SMALL_FONT,
            background = "#ffffff",
            relief = FLAT,
            command = self.buttonStepResponsePressed
        )

        self.buttonBode = tk.Button(
            self,
            width = 22,
            text = "Bode",
            font = config.SMALL_FONT,
            background = "#fff0bc",
            command = self.buttonBodePressed
        )

        self.buttonZerosAndPoles = tk.Button(
            self,
            width = 22,
            text = "Zeros And Poles",
            font = config.SMALL_FONT,
            background = "#fff0bc",
            command = self.buttonZerosAndPolesPressed
        )

        self.buttonStepResponse.grid( row=0, column=0, ipadx=3)
        self.buttonBode.grid(         row=0, column=1, ipadx=3)
        self.buttonZerosAndPoles.grid(row=0, column=2, ipadx=3)

        self.containCurve = tk.Frame(self)
        self.containCurve.grid(row=1, column=0, columnspan=3)

        self.curves = {}

        for curve in curves:
            self.curves[curve] = curve(self.containCurve, self)
            self.curves[curve].grid_propagate(True)
            self.curves[curve].grid(row=0, column=0, sticky=E + W + N + S)
        
        self.showCurve(firstCurve)

    #Menu managing functions
    
    def showCurve(self, curve):
        self.curves[curve].focus()
        curve = self.curves[curve]
        curve.tkraise()
        self.curve = curve

    def getCurrentCurve(self):
        return self.curve

    ##################################################
    #   Curve Selection Buttons' Callback Functions  #
    ##################################################
    
    def buttonStepResponsePressed(self):
        self.buttonStepResponse.config( relief=FLAT,   bg="#ffffff")
        self.buttonBode.config(         relief=RAISED, bg="#fff0bc")
        self.buttonZerosAndPoles.config(relief=RAISED, bg="#fff0bc")
        self.showCurve(CurveStepResponse)

    def buttonBodePressed(self):
        self.buttonStepResponse.config( relief=RAISED, bg="#fff0bc")
        self.buttonBode.config(         relief=FLAT,   bg="#ffffff")
        self.buttonZerosAndPoles.config(relief=RAISED, bg="#fff0bc")
        self.showCurve(CurveBode)

    def buttonZerosAndPolesPressed(self):
        self.buttonStepResponse.config( relief=RAISED, bg="#fff0bc")
        self.buttonBode.config(         relief=RAISED, bg="#fff0bc")
        self.buttonZerosAndPoles.config(relief=FLAT,   bg="#ffffff")  
        self.showCurve(CurveZerosAndPoles)
    
    def focus(self):
        pass        
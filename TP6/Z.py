import numpy as np
import matplotlib.pyplot as plt
import random


class CNum:
    def __init__(self, mod, phi, type):
        self.mod = mod
        self.phi = phi
        self.type = type
        self.color = '#' +"%06x" % random.randint(0, 0xFFFFFF)

    def graph(self):
        plt.polar([np.deg2rad(self.phi), 0], [self.mod, 0], c=self.color)
        plt.scatter(np.deg2rad(self.phi), self.mod, c=self.color)
        plt.plot(np.deg2rad(self.phi), self.mod, label=self.type, color=self.color)
        plt.legend()


def ej1(arrayOfSignals):
    plt.title("Diagrama fasorial de corriente")
    for x in arrayOfSignals:
        x.graph()
    plt.show()

ax = plt.subplot(111, polar=True)

#TENSIONES DE FASE
#Urs = CNum(140, 0, 'URS [V]')
#Ust = CNum(137.2, 120, 'UST [V]')
#Utr = CNum(137.5, -120, 'UTR [V]')

#R R R
#Ir = CNum(2.075, 0, 'IR [A]')
#Is = CNum(2.05, 96.348, 'IS [A]')
#It = CNum(3.7, -96.348, 'IT [A]')

#L L L
#Ir = CNum(1.55, 0, 'IR [A]')
#Is = CNum(2.2, 4.092, 'IS [A]')
#It = CNum(2.9, -4.092, 'IT [A]')

#R/L R/L R/L
#Ir = CNum(3, 0, 'IR [A]')
#Is = CNum(3.4, 2.934, 'IS [A]')
#It = CNum(4.5, -2.934, 'IT [A]')

#R R/L L
Ir = CNum(1.05, 0, 'IR [A]')
Is = CNum(2.95, -3.734, 'IS [A]')
It = CNum(4.15, 3.734, 'IT [A]')

#ej1([Urs, Ust, Utr])
ej1([Ir, Is, It])




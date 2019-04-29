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
    plt.title("Diagrama fasorial de tensión y corriente")
    for x in arrayOfSignals:
        x.graph()
    plt.show()


def ej2(S):
    S.graph()
    fq = -90
    fp = 0
    if S.phi > 0:
        fq = 90
    if S.phi > 90 or S.phi < -90:
        fp = 180
    Q = CNum(abs(S.mod * np.sin(np.deg2rad(S.phi))), fq,'Potencia Reactiva')
    P = CNum(abs(S.mod * np.cos(np.deg2rad(S.phi))), fp,'Potencia Activa')
    Q.graph()
    P.graph()
    plt.title("Diagrama fasorial de potencias")
    plt.show()


ax = plt.subplot(111, polar=True)
Z1 = CNum(3, 90, 'Corriente [A]')
Z2 = CNum(4, 135, 'Tension [V]')
Z3 = CNum(56, 145, 'Potencia Apartente')
#ej1([Z1, Z2])
ej2(Z3)



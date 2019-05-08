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
Z1 = CNum(280, 74.635, 'Corriente [mA]')
Z2 = CNum(99.5, 0, 'Tension [V]')
Z3 = CNum(460, 77.27, 'Corriente [mA]')
Z4 = CNum(98.5, 0, 'Tension [V]')
Z5 = CNum(920, 74.771, 'Corriente [mA]')
Z6 = CNum(96, 0, 'Tension [V]')
Z7 = CNum(116.11, 42.21, 'Potencia Apartente')
Z8=CNum(106.50, -84.94, 'Potencia Apartente')
Z9=CNum(54.86, 6.522, 'Potencia Apartente')
ej1([Z1,Z2])
ej1([Z3,Z4])
ej1([Z5,Z6])
ej2(Z7)
ej2(Z8)
ej2(Z9)




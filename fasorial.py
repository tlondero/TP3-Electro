import matplotlib.pyplot as plt     #si pongo plt, elegido arbitrariamente, sabe que me refiero a esa libreria
import numpy

def fasorial_1(r, theta, variable):

    ax = plt.subplot(111, polar=True)
    plt.title("Diagrama fasorial de tensión y corriente")

    plt.polar([numpy.pi * theta[0] / 180, 0], [r[0], 0])
    plt.scatter(numpy.pi * theta[0] / 180, r[0])
    ax.plot(theta[0], r[0], label=variable[0], color = 'blue')

    plt.polar([numpy.pi * theta[1] / 180, 0], [r[1], 0])
    plt.scatter(numpy.pi * theta[1] / 180, r[1])
    ax.plot(theta[1], r[1], label=variable[1], color='#ee8d18')

    ax.legend()
    plt.show()

def fasorial_2(r, theta, variable):

    ax = plt.subplot(111, polar=True)
    plt.title("Diagrama fasorial de potencias")

    plt.polar([numpy.pi * theta[0] / 180, 0], [r[0], 0])
    plt.scatter(numpy.pi * theta[0] / 180, r[0])
    ax.plot(theta[0], r[0], label=variable[0], color='#008b8b')

    plt.polar([numpy.pi * theta[1] / 180, 0], [r[1], 0])
    plt.scatter(numpy.pi * theta[1] / 180, r[1])
    ax.plot(theta[1], r[1], label=variable[1], color='#4b0082')

    plt.polar([numpy.pi * theta[2] / 180, 0], [r[2], 0])
    plt.scatter(numpy.pi * theta[2] / 180, r[2])
    ax.plot(theta[2], r[2], label=variable[2], color='#228b22')

    ax.legend()
    plt.show()

#modulo_1 = [3, 4]
#fase_1 = [90, 135]        #En grados
#variable_1 = ['Corriente (I)', 'Tensión (V)']
#fasorial_1(modulo_1, fase_1, variable_1)

modulo_2 = [1, numpy.sqrt(2), 1]
fase_2 = [90, 45, 0]
variable_2 = ['Potencia reacrtiva Q (VAR)', 'Potencia apartente S (VA)', 'Potencia activa P (W)']
fasorial_2(modulo_2, fase_2, variable_2)



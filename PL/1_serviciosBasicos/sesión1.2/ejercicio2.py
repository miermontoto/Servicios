# Modifica el programa anterior para que en lugar de imprimirlo en pantalla almacene los datos en una lista.
# Después imprime la lista.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi, 0.1)
y = np.sin(x)

lista = []
for i in range(len(x)):
    lista.append(y[i])

print(lista)

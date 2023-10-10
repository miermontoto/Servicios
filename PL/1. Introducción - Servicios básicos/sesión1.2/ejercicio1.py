# Escribe un programa que imprima en pantalla la función sin(x) para x evaluada entre 0 y pi, a intervalos regulares de 0.1

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

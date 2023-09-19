# Escribe fichero llamado seno.py que contenga una función que construya la lista descrita en el punto anterior y la devuelva como resultado.
# Llama a esta función seno() (no recibe parámetros).
# Documenta la función con docstrings.
# Escribe el fichero de modo que pueda ser ejecutado como programa principal o como módulo.
# Cuando es ejecutado como programa principal contendrá una “demo” que llama a la función anterior e imprime por pantalla la lista resultante.
import numpy as np
import matplotlib.pyplot as plt


def seno() -> list[float]:
    """
    Construye una lista con los valores de la función seno(x) para x evaluada entre 0 y pi, a intervalos regulares de 0.1
    """
    x = np.arange(0, np.pi, 0.1)
    y = np.sin(x)

    lista = []
    for i in range(len(x)):
        lista.append(y[i])

    return lista


if __name__ == "__main__":
    print("Demostración de la función seno()")
    print(seno())
else:
    print("Módulo seno cargado")

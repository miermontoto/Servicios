# Escribe una función que recibe una cadena como parámetro y devuelve un diccionario
# con las claves "a", "e", "i", "o", "u" y en cada clave el número de repeticiones
# de esa vocal en la cadena.

def cuenta_vocales_bucle(cadena: str) -> dict[str, int]:
    """
    Cuenta el número de vocales que hay en una cadena
    :param cadena: cadena de texto
    :return: diccionario con las vocales y el número de repeticiones
    """
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for letra in cadena:
        lower = letra.lower()
        if lower in vocales:
            vocales[lower] += 1

    return vocales


def cuenta_vocales_count(cadena: str) -> dict[str, int]:
    """
    Cuenta el número de vocales que hay en una cadena
    :param cadena: cadena de texto
    :return: diccionario con las vocales y el número de repeticiones
    """
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for vocal in vocales:
        vocales[vocal] = cadena.lower().count(vocal)

    return vocales


if __name__ == "__main__":
    print(cuenta_vocales_bucle("Hola Mundo"))
    print(cuenta_vocales_count("Hola Mundo"))

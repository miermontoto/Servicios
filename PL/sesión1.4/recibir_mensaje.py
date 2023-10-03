import socket


def uno(sock) -> str:
    """"
    Función que recibe bytes del socket hasta
    detectar el fin de línea de uno en uno.
    """

    buffer = []
    while True:
        caracter = sock.recv(1)
        if caracter == b"\n" or caracter == b"":
            break
        buffer.append(caracter)
    return b"".join(buffer).decode("utf8").replace("\r", "")


def readline(sock) -> str:
    """
    Función que recibe bytes del socket hasta
    detectar el fin de línea en bloque utilizando
    la función `readline()` de python.
    """

    f = sock.makefile(encoding="utf8", newline="\r\n")
    mensaje = f.readline()
    f.close()
    return mensaje.replace("\r\n", "")

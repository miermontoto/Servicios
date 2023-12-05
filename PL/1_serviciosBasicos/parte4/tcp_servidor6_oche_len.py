import ips_argv
import recibir_mensaje

import socket
import sys
import time


def recvall(sock, bytes) -> str:
    """
    Recibe una cantidad de bytes determinada por el parámetro `bytes` del
    socket `sock` y devuelve una cadena de texto con los datos recibidos.
    """

    data = b""
    while len(data) < bytes:
        paquete = sock.recv(bytes - len(data))
        if not paquete:
            return ""
        data += paquete
    return data.decode("utf8")


puerto = ips_argv.servidor(sys.argv)

# Creación del socket de escucha
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Podríamos haber omitido los parámetros, pues por defecto `socket()` en python
# crea un socket de tipo TCP

# Asignarle puerto
s.bind(("", puerto))

# Ponerlo en modo pasivo
s.listen(5)  # Máximo de clientes en la cola de espera al accept()

# Bucle principal de espera por clientes
while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    # Bucle de atención al cliente conectado
    while True:
        try:
            longitud = recibir_mensaje.uno(sd)
            print("Recibiendo %d bytes" % int(longitud))
            mensaje = sd.recv(int(longitud)).decode("utf8")

            if mensaje == "":
                print("Conexión cerrada por el cliente")
                sd.close()
                break

            linea = mensaje[::-1]

            newlen = "%d\n" % len(bytes(linea, "utf8"))
            print("Enviando %d bytes" % int(newlen))
            sd.sendall(bytes(newlen + linea + "\r\n", "utf8"))
        except ConnectionResetError:
            print("Cliente desconectado")
            sd.close()
            break

import ips_argv
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
    continuar = True
    # Bucle de atención al cliente conectado
    while continuar:
        datos = recvall(sd, 5)  # Observar que se lee del socket sd, no de s

        if datos == "":  # Si no se reciben datos, es que el cliente cerró el socket
            print("Conexión cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False
        elif datos == "FINAL":
            print("Recibido mensaje de finalización")
            sd.close()
            continuar = False
        else:
            print("Recibido mensaje: %s" % datos)

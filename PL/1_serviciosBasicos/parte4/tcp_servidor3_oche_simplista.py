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
    # Bucle de atención al cliente conectado
    while True:
        try:
            mensaje = sd.recv(80)  # Nunca enviará más de 80 bytes, aunque tal vez sí menos
            mensaje = str(mensaje, "utf8")  # Convertir los bytes a caracteres

            if mensaje == "":
                print("Conexión cerrada por el cliente")
                sd.close()
                break

            # Segundo, quitarle el "fin de línea" que son sus 2 últimos caracteres
            linea = mensaje[:-2]  # slice desde el principio hasta el final -2

            # Tercero, darle la vuelta
            linea = linea[::-1]

            # Finalmente, enviarle la respuesta con un fin de línea añadido
            # Observa la transformación en bytes para enviarlo
            sd.sendall(bytes(linea + "\r\n", "utf8"))
        except ConnectionResetError:
            print("Cliente desconectado")
            sd.close()
            break

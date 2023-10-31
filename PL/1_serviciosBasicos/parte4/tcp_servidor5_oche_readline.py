import ips_argv
import recibir_mensaje

import socket
import sys
import time


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
            mensaje = recibir_mensaje.readline(sd)

            if mensaje == "":
                print("Conexión cerrada por el cliente")
                sd.close()
                break

            linea = mensaje[::-1]

            # Finalmente, enviarle la respuesta con un fin de línea añadido
            # Observa la transformación en bytes para enviarlo
            sd.sendall(bytes(linea + "\r\n", "utf8"))
        except ConnectionResetError:
            print("Cliente desconectado")
            sd.close()
            break

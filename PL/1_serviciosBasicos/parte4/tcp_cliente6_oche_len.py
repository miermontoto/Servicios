import ips_argv
import recibir_mensaje

import lorem
import socket
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

# Creacion de socket
sock = socket.socket()

try:
	sock.connect((HOST, PORT))  # Conexión al servidor

	for _ in range(5):
		mensaje = f"{lorem.sentence()}\r\n"
		longitud = "%d\n" % len(bytes(mensaje, "utf8"))
		sock.send(bytes(longitud + mensaje, "utf8"))

		# recibir respuesta del servidor
		print(repr(recibir_mensaje.readline(sock)))
except socket.error as e:
	print("Socket error:", e)
finally:
	sock.close()  # Cierre del socket

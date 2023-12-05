import ips_argv
import recibir_mensaje

import lorem
import socket
import struct
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

# Creacion de socket
sock = socket.socket()

num = 5

try:
	sock.connect((HOST, PORT))  # Conexión al servidor

	for _ in range(num):
		mensaje = f"{lorem.sentence()}\r\n"
		longitud = struct.pack(">H", len(bytes(mensaje, "utf8")))
		sock.send(longitud + bytes(mensaje, "utf8"))

	for _ in range(num):
		# recibir respuesta del servidor
		print(repr(recibir_mensaje.readline(sock)))
except socket.error as e:
	print("Socket error:", e)
finally:
	sock.close()  # Cierre del socket

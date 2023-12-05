import ips_argv
import recibir_mensaje

import lorem
import socket
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

num = 5

# Creacion de socket
sock = socket.socket()

try:
	sock.connect((HOST, PORT))  # Conexión al servidor

	for _ in range(num):
		mensaje = f"{lorem.sentence()}\r\n"
		longitud = "%d\n" % len(bytes(mensaje, "utf8"))
		sock.send(bytes(longitud + mensaje, "utf8"))

	for _ in range(num):
		newlen = recibir_mensaje.uno(sock)
		newmsg = sock.recv(int(newlen)).decode("utf8")
		print(repr(newmsg))
except socket.error as e:
	print("Socket error:", e)
finally:
	sock.close()  # Cierre del socket

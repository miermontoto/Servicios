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
		string = f"{lorem.sentence()}\r\n".encode("utf8")
		sock.send(string)

		# recibir respuesta del servidor
		print(repr(recibir_mensaje.uno(sock)))
except socket.error as e:
	print("Socket error:", e)
except Exception as e:
	print("Error:", e)
finally:
	sock.close()  # Cierre del socket

import ips_argv
import lorem
import socket
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

# Creacion de socket
sock = socket.socket()

try:
	sock.connect((HOST, PORT))  # Conexión al servidor

	for _ in range(2):
		for _ in range(3):
			string = f"{lorem.sentence()[:25]}\r\n".encode("utf8")
			sock.send(string)

		for _ in range(3):
			print(repr(sock.recv(80).decode("utf8")))
except socket.error as e:
	print("Socket error:", e)
except Exception as e:
	print("Error:", e)
finally:
	sock.close()  # Cierre del socket

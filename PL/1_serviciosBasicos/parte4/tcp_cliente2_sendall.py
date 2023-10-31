import ips_argv
import socket
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

# Creacion de socket
sock = socket.socket()

try:
	sock.connect((HOST, PORT))  # Conexión al servidor

	string = b"ABCDE"
	for _ in range(5):
		sock.sendall(string)

	sock.send(b"FINAL")
except socket.error as e:
	print("Socket error:", e)
except Exception as e:
	print("Error:", e)
finally:
	sock.close()  # Cierre del socket

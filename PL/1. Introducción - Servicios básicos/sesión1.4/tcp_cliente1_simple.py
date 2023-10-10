import ips_argv
import socket
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

# Creacion de socket
sock = socket.socket()

try:
	sock.connect((HOST, PORT))  # Conexión al servidor

	for _ in range(5):
		string = b"ABCDE"
		sock.send(string)

	sock.send(b"FINAL")
except socket.error as e:
	print("Socket error:", e)
except Exception as e:
	print("Error:", e)
finally:
	# Cierre del socket
	sock.close()

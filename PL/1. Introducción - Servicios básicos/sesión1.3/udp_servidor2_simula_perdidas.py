import ips_argv
import random
import socket
import sys

PORT = ips_argv.servidor(sys.argv)

# Creacion de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

# Bucle de escucha
while True:
	data, addr = sock.recvfrom(1024)
	if random.randint(1, 2) == 1:
		print(f"[{addr[0]}:{addr[1]}] Paquete perdido")
		continue
	string = data.decode('utf-8')
	print(f"[{addr[0]}:{addr[1]}] {string}")
	if string == "exit":
		break

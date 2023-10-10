import ips_argv
import socket
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

# Creacion de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envío de mensaje a partir de entrada de teclado
while True:
	string = input("> ")
	res = sock.sendto(string.encode('utf-8'), (HOST, PORT))

	if string == "exit":
		break

	if res == 0:
		print("Error al enviar el mensaje")

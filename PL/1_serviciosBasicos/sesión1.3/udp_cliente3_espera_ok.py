import ips_argv
import socket
import sys

HOST, PORT = ips_argv.cliente(sys.argv)

# Creacion de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

i = 1
# Envío de mensaje a partir de entrada de teclado
while True:
	string = input("> ")
	string = f"{i}: {string}"
	res = sock.sendto(string.encode('utf-8'), (HOST, PORT))

	if string == "exit":
		break

	i += 1
	if res == 0:
		print("Error al enviar el mensaje")

	sock.settimeout(0.1)
	try:
		datagrama, origen = sock.recvfrom(1024)  # Tamaño máximo a recibir
		datagrama = datagrama.decode("utf8")
		if datagrama == "OK":
			print("Recibida confirmación")
		else:
			print("Recibido datagrama no esperado")
	except socket.timeout:
		print("ERROR. El datagrama de confirmación no llega")
	except:    # Otras posibles excepciones dejamos que las maneje el usuario
		raise

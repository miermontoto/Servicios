import ips
import sys


def servidor(argv):
	if len(argv) != 2 and len(argv) != 1:
		print(f"Uso: python {argv[0]} <puerto>")
		sys.exit(1)

	puerto = argv[1] if len(argv) == 2 else "9999"

	if not ips.check_port(puerto):
		print("El puerto debe ser un número válido")
		sys.exit(1)

	print(f"Abriendo puerto {puerto}")
	return int(puerto)


def cliente(argv):
	if len(argv) != 3 and len(argv) != 1:
		print(f"Uso: python {argv[0]} <nodo> <puerto>")
		sys.exit(1)

	nodo = argv[1] if len(argv) == 3 else "localhost"
	puerto = argv[2] if len(argv) == 3 else "9999"

	if not ips.check_ip(nodo) or not ips.check_port(puerto):
		print("El nodo y el puerto deben ser números válidos")
		sys.exit(1)

	print(f"Conectando con {nodo}:{puerto}")
	return nodo, int(puerto)

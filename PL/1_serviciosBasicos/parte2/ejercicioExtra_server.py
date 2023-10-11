# Crea un programa de Python que gestione la conexión a clientes remoto a través de la línea de comandos.
# 1. El programa debe tomar argumentos de la línea de comandos para determinar el puerto por el que escuchar.
# 2. Si no se proporcionan argumentos, el programa debe abrir el puerto 9999.
# 3. El programa debe imprimir un mensaje que indique qué nodo está abriendo.

import sys
import ips

if len(sys.argv) != 2 and len(sys.argv) != 1:
	print(f"Uso: python {sys.argv[0]} <puerto>")
	sys.exit(1)

puerto = sys.argv[1] if len(sys.argv) == 2 else "9999"

if not ips.check_port(puerto):
	print("El puerto debe ser un número válido")
	sys.exit(1)

print(f"Abriendo puerto {puerto}")

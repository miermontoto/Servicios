# Crea un programa de Python que gestione la conexión a un servidor remoto a través de la línea de comandos.
# 1. El programa debe tomar argumentos de la línea de comandos para determinar el nodo de destino y puerto.
# 2. Si no se proporcionan argumentos, el programa debe establecer la conexión predeterminada a "localhost" en el puerto 9999.
# 3. Si se proporcionan argumentos en la línea de comandos, el programa debe tomar el primer argumento como el nodo de destino y el segundo argumento como el puerto.
# 4. El programa debe imprimir un mensaje que indique a qué nodo y puerto se enviarán los datos.

import sys
import ips


if len(sys.argv) != 3 and len(sys.argv) != 1:
	print(f"Uso: python {sys.argv[0]} <nodo> <puerto>")
	sys.exit(1)

nodo = sys.argv[1] if len(sys.argv) == 3 else "localhost"
puerto = sys.argv[2] if len(sys.argv) == 3 else "9999"

if not ips.check_ip(nodo) or not ips.check_port(puerto):
	print("El nodo y el puerto deben ser números válidos")
	sys.exit(1)

print(f"Conectando con {nodo}:{puerto}")

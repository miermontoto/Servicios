def check_ip(ip: str) -> bool:
	"""
	Comprueba si una cadena es una dirección IP válida
	:param ip: cadena de texto
	:return: True si es una dirección IP válida, False en caso contrario
	"""

	if ip == "localhost": return True

	octetos = ip.split(".")
	if len(octetos) != 4:
		return False

	for octeto in octetos:
		if not octeto.isdigit():
			return False

		if int(octeto) < 0 or int(octeto) > 255:
			return False

	return True


def check_port(puerto: str) -> bool:
	"""
	Comprueba si una cadena es un puerto válido
	:param puerto: cadena de texto
	:return: True si es un puerto válido, False en caso contrario
	"""

	if not puerto.isdigit():
		return False

	if int(puerto) < 1024 or int(puerto) > 65535:
		return False

	return True

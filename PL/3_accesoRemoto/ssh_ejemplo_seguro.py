import paramiko
import time
import base64
import getpass

client = paramiko.SSHClient()
inputkey = getpass.getpass("Introduce la clave privada: ")
key = paramiko.Ed25519Key(data=base64.decodebytes(bytes(inputkey, 'utf8')))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)
user = input("Introduce el username: ")
password = getpass.getpass("Introduce la clave de usuario: ")
client.connect('localhost', username=user, password=password)
print("Conectado!!")

# Ejecutar comando remoto, redireccionando sus salidas
stdin, stdout, stderr = client.exec_command('ls')

# Mostrar resultado de la ejecución (rstrip quita los retornos de carro)
for line in stdout:
    print(line.rstrip())
time.sleep(1)  # Dar tiempo a que se vacie el buffer
client.close()

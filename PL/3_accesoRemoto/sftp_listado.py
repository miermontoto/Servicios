import paramiko
import time
import getpass

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
user = input('username: ')
password = getpass.getpass()
client.connect('localhost', username=user, password=password)
print("Conectado!!")

sftp = client.open_sftp()
listado = sftp.listdir()
for nombre in listado:
    print(nombre)

print(sftp.stat(listado.pop(0)))

client.close()

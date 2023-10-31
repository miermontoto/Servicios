import paramiko
import time
import getpass
from stat import S_ISDIR

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
user = input('username: ')
password = getpass.getpass()
client.connect('localhost', username=user, password=password)
print("Conectado!!")

sftp = client.open_sftp()
listado = sftp.listdir()

for nombre in listado:
    try:
        if not S_ISDIR(sftp.stat(nombre).st_mode):
            print(f"Descargando {nombre}...")
            # sftp.get(nombre, nombre)
    except Exception: pass
client.close()

# Consulta la documentación del módulo telnetlib, y en particular
# copia el ejemplo que aparece al final, con el nombre telnet1_ejemplo.py
# y prueba a ejecutarlo desde Unix y desde Windows, si tienes python
# instalado en Windows. Cuando lo ejecutes desde Windows deberás cambiar
# “localhost” por la IP del servidor Unix.

import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('utf8') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf8') + b"\n")

tn.write(b"ls\n")
tn.read_until(b"%")
print(tn.read_until(b"%").decode('utf8'))
tn.write(b"exit\n")
print(tn.read_all().decode('utf8'))

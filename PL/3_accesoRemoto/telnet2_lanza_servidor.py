import telnetlib
import getpass
import time

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
tn.write(user.encode('utf8') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf8') + b"\n")

tn.read_until(b'%')
tn.write(b"ps -ef\n")
if "udp_servidor3_con_ok.py" in tn.read_until(b'%').decode('utf8'):
    print("El servidor ya está en ejecución")
    exit(1)

tn.write(b"nohup python ~/udp_servidor3_con_ok.py &\n")
print("Esperando...")
time.sleep(10)
tn.write(b"exit\n")
tn.write(b"exit\n")
print(tn.read_all().decode('utf8'))

import socket

s = socket.socket()
s.connect(("localhost", 23))
respuesta = s.recv(1024)

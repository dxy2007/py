import socket
client = socket.socket()
ip = ('127.0.0.1',8888)
client.connect(ip)
data = client.recv(1024)
print(data.decode())
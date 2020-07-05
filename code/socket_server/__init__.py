import socket
sk = socket.socket()

ip = ('127.0.0.1',8888)

sk.bind(ip)
sk.listen(5)
print('正在接收数据....')
conn, address = sk.accept()
msg = "hello world"
conn.send(msg.encode())
conn.close()
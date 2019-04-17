import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b''
flag = 0

while True:
    data = mysock.recv(3000)
    if len(data) < 1: break
    count = count + len(data)
    #print(len(data), count)
    if flag == 0:
        print(data)
    flag += 1
    picture = picture + data
print(count)
mysock.close()

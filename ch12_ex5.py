import socket
import re
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('baidu.com', 80))
cmd = 'GET https://www.baidu.com/robots.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)
message = data.decode()
print(len(message))
header_end_pos = message.find('\r\n\r\n') + 4
print(message[header_end_pos:])  #received a blank line
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

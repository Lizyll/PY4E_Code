import socket

url = input('Enter - ')
hlst = url.split('/')
for n in hlst:
    if not n.startswith('www'): continue
    HOST = n[4:]
print(HOST)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, 80))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
print(cmd)
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode())
mysock.close()

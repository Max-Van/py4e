import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count=0

while True:
    data = mysock.recv(1024)
    if len(data) < 1:
        break
    #print(data.decode(),end='')
    print(data.decode())
    count += 1
    print('Retrieving data for the ', count, 'times.')


mysock.close()

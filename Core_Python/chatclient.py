## A client that send and receives messages

import socket

host = '127.0.0.1'
port = 9500

s = socket.socket()

s.connect((host, port))

## Enter data at client
str = input('Enter data: ')

## continue as long as 'exit' not entered by user

while str != 'exit':
    ## send data from client to server
    s.send(str.encode())
    
    ## receive response from server
    data = s.recv(1024)
    data = data.decode()
    print('From server: ',data)
    
    ## enter data
    str = input('Enter data: ')
s.close()
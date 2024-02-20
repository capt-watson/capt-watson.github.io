import socket

host = 'localhost'
port = 6767

##v create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

filename = input('Enter filename: ')

## send the file to server
s.send(filename.encode())       ## Here 's' represents the 'server' machine.

## receive file content from server
content = s.recv(1024)
print(content.decode())

## disconnect the client
s.close()

#~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python> Python Fileclient.py
#~ Enter filename: myfile.txt
#~ Brooke Shield Loves me.
#~ I love her too!
#~ She is hot!!

#~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python>
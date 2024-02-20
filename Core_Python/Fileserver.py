import socket

host = 'localhost'
port = 6767

## Create a TCP socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)         ## Max 1 connection is accepted

c,addr = s.accept()     ## Here 'c' represents 'client' machine

print('A Client accepted connection')

## Accept file from client
fname = c.recv(1024)

## convert file name into normal string
fname = str(fname.decode())

print('File %s received from client' % fname)

try:
    f = open(fname, 'rb')
    content = f.read()
    
    ## send file to client
    c.send(content)
    print('File content sent to client')
    
    f.close()
except FileNotFoundError:
    c.send('File does not exist')
c.close()

#~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python> Python Fileserver.py
#~ A Client accepted connection
#~ File myfile.txt received from client
#~ File content sent to client
#~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python>
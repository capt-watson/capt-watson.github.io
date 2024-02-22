## A server that receives and sends messages

# import socket

# host = '127.0.0.1'
# port = 9500

# ## Create a server side socket
# s = socket.socket()
# s.bind((host,port))

# s.listen(1)

# ## wait till a client connects
# c,addr = s.accept()
# print('A client connected')

# ## Server runs continuously

# while True:
#     ## receive data from client
#     data = c.recv(1024)
    
#     ## if client send empty string, come out
#     if not data:
#         break
#     print('From client: ',str(data.decode()))
    
#     ## enter response data from server
#     data1 = input('Enter response: ')
    
#     ## send that data to client
#     c.send(data1.encode())
    
# ## close the connection
# c.close()

#% if get error: 

#% 's.bind((host,port))
#% OSError: [WinError 10048] Only one usage of each socket address (protocol/network
#% address/port) is normally permitted'

#% change the port address as the current port may be in use by another process.
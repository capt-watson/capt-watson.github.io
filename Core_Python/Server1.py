# #@ TCP/IP Server

# #! Create a TCP/IP server program that sends messages to client.

# import socket

# host = 'localhost'
# port = 5000

# ## Create a socket at server side using TCP/IP protocol
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ## Bind the socket with server and port number
# s.bind((host,port))

# ## Allow maximum 1 connection to the socket
# s.listen(1)

# ## wait till a client accepts a connection
# c,addr = s.accept()  ## here c represents 'connection obj' used for sending msg
# ## addr is the address of the client that has accepted the connection
        
# ## display client address
# print('Connection from: ',str(addr))

# ## send message to client after encoding into binary string.
# c.send(b'Hello Veronica, How are you?')
# msg = 'Love you, bye'
# c.send(msg.encode()) 

# ## disconnect the server
# c.close()               

# #~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python> python Server1.py
# #~ Connection from:  ('127.0.0.1', 55026)
# #~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python>
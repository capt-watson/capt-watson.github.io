# #@ UDP Client

# #! Create a UDP client that receives messages from the server

# import socket

# host = 'localhost'
# port = 5000

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ## connect it to server with host and port number
# s.bind((host, port))

# ## receive message string from server, at a time 1024 B
# msg,addr = s.recvfrom(1024)

# try:
#     ## let the socket block after 5 seconds if the server disconnects.
#     s.settimeout(5)
    
#     ## repeat as long as message strings are not empty
#     while msg:
#         print('Received: ',msg.decode())
#         msg, addr = s.recvfrom(1024)
# except socket.timeout:
#     print('Timeout is over and hence terminating...')

# ## Disconnect the client
# s.close()

# #~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python> Python Client2.py
# #~ Received:  Hello, Betty! How are you
# #~ Received:  Hasta la vista
# #~ Timeout is over and hence terminating...
# #~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python> Python Client2.py
# #@ TCP/IP Client

# #! Create a TCP/IP program that receives messages from a server

# import socket

# host = 'localhost'
# port = 5000

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ## connect to server and port number
# s.connect((host, port))

# ## Receive a message from server, only 1024 B at a time
# msg = s.recv(1024)

# ## repeat as long as strings are not empty
# while msg:
#     print('Received: ',msg.decode())
#     msg = s.recv(1024)  ## recursive function

# ## Disconnect the client
# s.close()

# #~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python> python Client1.py
# #~ Received:  Hello Veronica, How are you?
# #~ Received:  Love you, bye
# #~ PS C:\Users\shekh\Projects\Python_Tutorials\Core_Python>
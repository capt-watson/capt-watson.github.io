# #@ UDP Server

# #! Create a UDP server that sends messages to the client.

# import socket
# import time

# host = 'localhost'
# port = 5000

# ## Create a socket at server side to use UDP protocol
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ## let the server waits for 5 seconds
# time.sleep(5)

# ## send message to client after encoding into binary string
# s.sendto(b'Hello, Betty! How are you', (host, port))
# msg = 'Hasta la vista'
# s.sendto(msg.encode(), (host, port))

# ## Disconnect the server
# s.close()

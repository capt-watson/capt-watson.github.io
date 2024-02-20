#! Protocols is a way to establish a connection and help send/receive data in a
#! standard format.

#@ Protocols
#! Two types of protocol models

#! TCP/IP protocol
#! UDP

#@ TCP/IP protocol

#! TCP/IP = Transmission Control Protocol/Internet protocol

#@ TCP/IP model has five layers:

#% Application Layer

#% TCP

#% IP

#% Data Link Layer

#% Physical layer

#! Application Layer is the topmost layer of the TCP/IP model that directly
#! interacts with an application(or data).

#! This layer receives data from the application and formats the data.

#& Then this data goes to the next layer called 'TCP' in the form of continuous
#& stream of bytes. 

#& TCP upon receiving the data from the application layer, will divide it into small
#& segments called 'packets'. A packet contains a group of bytes of data.

#! These packets are then sent to IP layer.
#! IP layer inserts the packets into envelopes called 'frames'. 
#! Each frame contains a packet, the IP address of destination computer, the IP address
#! of source computer and some additional bits useful in error detection & correction.

#& These frames are then sent to Data link layer which dispatches them to correct
#& destination computer on the network.

#! The last layer, which is called the Physical Layer is used to physically transmit
#! data on network using appropriate hardware..

#@ DNS ('Domain Name Service or system)

#! DNS is a service that maps the IP addresses with corresponding website names.

#! On internet, IP addresses of 4 bytes are used and this version is called IP address
#! version 4.

#! The next new version of IP address is version 6, which uses 16 bytes to identify a
#! computer.

#% TCP/IP that takes care of bits sent and whether all the bits are received duly by
#% the destination computer.

#% Hence TCP/IP is called 'connection oriented reliable protocol'. Every transmitted
#% bit is accountable in this protocol.

#! HTTP (Hyper Text Transfer Protocol) is the most widely used protocol on Internet,
#! which is used to transfer web pages (.html files) from one computer to another
#! computer on Internet.

#% FTP (File Transfer Protocol) is useful to download or upload files from and to
#% server.

#! SMTP (Simple Mail Transfer Protocol) is useful to send mails on network.

#% POP (Post Office Protocol) is useful receive mails into the mail boxes.

#! NNTP (Network News Transfer Protocol) is used to transfer news articles on the
#! Internet.

#@ User Datagram Protocol (UDP)

#! Transfers data in a connection less and unreliable manner.
#! It will not check how many bits are sent or how many bits are actually received
#! at the other side.
#! Data sent may not be received in the same order.

#@ Sockets

#% A socket connecting network is created at each end of the communication. 
#% A socket has specific address.
#% This address is composed of an IP address and a port number.

#% The server creates a socket, attaches it to a network port address and then waits for
#% for the client to contact it.

#% The client creates a socket and then attempts to connect to the server socket.
#% When the connection is established, transfer of data takes place.

#% Port number takes 2 bytes and can be from 0 to 65,535. 

#% Establishing communication between a server and a client using sockets is called
#% 'socket programming'.

#% A new port number is used for each new socket.

#% New port number allotted depends upon the service provided on that socket.

#& The port number from 0 to 1023 are used by our computer system for various applications
#& (or services) and hence these port numbers are avoided in our networking programming.

#! To create a socket, Python provides socket module.
#! socket() function of socket module is useful to create a socket object as:

#% s = socket.socket(address_family, type)

#! Here, address_family indicates which version of the IP address should be used e.g.
#! whether version 4 or version 6 should be used.

#% socket.AF_INET     ## Internet protocol (IPV4) - This is default
#% socket.AF_INET6    ## Internet protocol (IPV6)

#! the second argument above is 'type' which represents the type of protocol to be used,
#! whether TCP/IP or UDP. 

#% socket.SOCK_STREAM   ## for TCP - This is default
#% socket.SOCK_DGRAM    ## for UDP

#@ Knowing IP address

#! To know the IP address of a website, 'gethostbyname()' function is used in socket
#! module. For e.g.

#% addr = socket.gethostbyname('www.google.co.in')

#! will return the IP address of google.co.in in website into 'addr' variable.
#! if no such website found on internet, it returns 'gaierror' (Get Address Information
#! Error)

#! Find the IP address of a website.

# import socket

# ## take the server name
# host = 'www.google.co.in'

# try:
#     # Know the IP address of the website
#     addr = socket.gethostbyname(host)
#     print('IP Address: %s' % addr)
# except socket.gaierror:
#     print('The website does not exist')

# #~ IP Address: 142.250.193.195

#@ URL

#! URL (Uniform Resource Locator) represents the address that is specified to access
#! some information or resources on internet.

#% http://www.dreamtechpress.com:80/Index.html

#! Explanation:

#~ Server to use http://

#~ Server name or IP address of the server (www.dreamtechpress.com)

#~ Port number (optional) (:80).

#~ File referred - generally index.html or home.html file

#! when a URL is given, one can parse the URL and find out all parts of the URL with
#! the help of urlparse() function of urllib.parse module in Python.

#! urlparse() function returns a tuple containing the parts of the URL.

#% tpl = urllib.parse.urlparse('urlstring')

#! tpl.scheme = this gives the protocol name used in the URL.

#! tpl.netloc = this gives website name on the net with port number if present.

#! tpl.path = this gives the path of the webpage.

#! tpl.port = gives the port number.

#! Retrieve different parts of the URL and display them.

# import urllib.parse

# url = 'http://www.dreamtechpress.com:80/engineering/computer-science.html'

# ## get tuple with parts of the URL.
# tpl = urllib.parse.urlparse(url)

# ## Display the contents of the tuple.

# print('Scheme= ',tpl.scheme)
# print('Net Location= ',tpl.netloc)
# print('Path= ',tpl.path)
# print('Parameters= ',tpl.params)
# print('Port Number= ',tpl.port)
# print('Total url = ',tpl.geturl())



#@ Reading source code of a web page

#% file = urllib.request.urlopen('https://www.python.org/')

#! One can use read() method on the 'file' object to read the data of the file object.

#! Read the source code of a web page

# import urllib.request

# file = urllib.request.urlopen('https://www.python.org/')

# print(file.read())


#@ Downloading a web page from Internet

#! Download a web page from Internet and save it on our computer.

# import urllib.request

# try:
#     ## store the url of the page into a file object.
#     file = urllib.request.urlopen('https://www.open-audit.org/')
    
#     ## read data from file and store into content object
#     content = file.read()
# except urllib.request.HTTPError:
#     print('The web page does not exit')
#     exit()
#     ## open a file for writing
# f = open('myfile.html', 'wb')   ## wb - write binary file. 'rb' means read binary file.

# f.write(content)

# f.close()

#@ Downloading an Image from Internet

#! Download an image from Internet

# import urllib.request

# ## copy the image url

# url = 'https://static.toiimg.com/thumb/msid-107786629,imgsize-1325828,width-400,resizemode-4/107786629.jpg'

# ## download the image as myimage.jpg file in the current directory
# download = urllib.request.urlretrieve(url, 'myimage.jpg')

#@ TCP/IP Server

#! Create a TCP/IP server program that sends messages to client.

import socket

host = 'localhost'
port = 5000

## Create a socket at server side using TCP/IP protocol
s = socket.socket()

## Bind the socket with server and port number
s.bind(host, port)

## Allow maximum 1 connection to the socket
s.listen(1)

## wait till a client accepts a connection
c,addr = s.accept()  ## here c represents 'connection obj' used for sending msg
        ## addr is the address of the client that has accepted the connection
        
## display client address
print('Connection from: ',str(addr))

## send message to client after encoding into binary string.
c.send(b'Hello Veronica, How are you?')
msg = 'Love you, bye'
c.send(msg.encode()) 

## disconnect the server
c.close                  

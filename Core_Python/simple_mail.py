import smtplib
from email.mime.text import MIMEText

## MIME = Multi-purpose Internet Mail Extensions

## body = represents mail body text

body = '''This is my Text email. This is sent to you from my Python program.
          I think you appreciated me'''

## create MIMEText class object with body text

msg = MIMEText(body)

## from which address the email is sent
fromaddr = 'abcde@gmail.com'

## To which address the email is sent
toaddr = 'vwxyz@gmail.com'

## store the addresses into the msg object
msg['from'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'SQ 228 Flight Delayed'

## connect to gmail.com server using 587 port number
server = smtplib.SMTP('smtp.gmail.com', 587)

## put the smtp connection in TLS mode. TLS = Transport Layer Security
server.starttls()

## login to server with your correct password

server.login(fromaddr, 'rpxl gjec rhmp bsas') ## Use app specific password

## send the message to the server
server.send_message(msg)
print('Mail sent')

## close connection with the server
server.quit()

#~ Mail sent

import socket
import sys

PORT = 1234 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created: port %s" %PORT)
except socket.error as err:
    print("Socket failed to create: %s" %err)

s.bind(('',PORT))

s.listen()

while(True):
    print('Ready for connection')
    (c, addr) = s.accept()
    print ('Got connection from %s' % (str(addr)))
    c.send(b'Thank you for connecting')

    message = ''
   
    while (str(message) != "b'Logout'"):
        message, clientAddress = c.recvfrom(2048)
        print(str(message)[2:-1])
        #s.sendall(message)
    c.close()








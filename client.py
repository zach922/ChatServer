import socket
import sys 

HOST = '127.0.0.1'
PORT = 1234

def communication(socket):
    exitCommand = "Logout"
    userName = input("Enter User Name: ")
    userText = ""   

    while(userText != exitCommand):
        userText = ""
        userText = input("> ")
        if (userText.lower() == 'logout'):
            socket.send(b'Logout')
        else:
            socket.send(bytes(userName + "> " + userText, 'utf-8'))

#Create Socket Client
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Socket successfully created: port %s" %PORT)
    
    ack = s.recv(2048)
    print(str(ack)[2:-1])

    communication(s)
except socket.error as err:
    print("Client failed to connect: %s" %err)
except KeyboardInterrupt:
    s.send(b'Logout')
    print ("\nLogging out")



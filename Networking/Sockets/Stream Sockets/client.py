############################################################
#
#    stream socket client
#
############################################################

import socket, sys



def sendAndReceive(clientSocket):
    message = "This is a message from a client: "
    clientSocket.send(message)
    response = clientSocket.recv(100) # blocking call
    print "CLIENT:", response
    sys.stdout.flush()

def connectToServer():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 7001))
    print "Server IP,port = {}".format(clientSocket.getpeername())
    print "Client IP,port = {}".format(clientSocket.getsockname())
    return clientSocket

clientSocket = connectToServer()
sendAndReceive(clientSocket)
clientSocket.close()

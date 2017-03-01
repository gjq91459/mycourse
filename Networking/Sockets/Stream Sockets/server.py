############################################################
#
#    stream socket server
#
############################################################

import socket, sys
from threading import Thread


def setupListeningSocket():
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    listenSocket.bind(('', 7001))
    listenSocket.listen(5) # set up backlog buffer
    print "Server Listening on IP,port = {}".format(listenSocket.getsockname())
    return listenSocket

def communicateWithClient(newSocket, messageNo):
    print "Server IP,port = {}".format(newSocket.getsockname())
    print "Client IP,port = {}".format(newSocket.getpeername())
    
    # wait for message and echo
    message = newSocket.recv(100)
    print "SERVER:", message
    sys.stdout.flush()
    
    # send response and close socket immediately
    message = "This is the response from the server"
    response = "This is response number {0} from the server".format(messageNo)
    newSocket.send(response)

def main():
    try:
        listenSocket = setupListeningSocket()
        messageNo = 1
        print "Server starting"
        while True:
            # accept client connections
            newSocket, remoteIPandPORT = listenSocket.accept()
            print "SERVER: opened a new client connection:", remoteIPandPORT
            sys.stdout.flush()
            clientThread = Thread(target=communicateWithClient, args=(newSocket, messageNo))
            messageNo = messageNo + 1
            clientThread.start()
    except KeyboardInterrupt as e:
        print "Server shutting down"
        listenSocket.close()

main()

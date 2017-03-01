import socket, sys

remoteServerIP = '0.0.0.0'

for port in range(1, 8000):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = clientSocket.connect_ex((remoteServerIP, port))
    if result == 0:
        print "Port {}: Open".format(port)
    clientSocket.close()

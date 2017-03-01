import select
import socket
import time

def pollSockets():
    readList, writeList, errorList = select.select( [sd1, sd2, sd3], [ ], [ ], 0)
    sockets = {id(eval(name)):name for name in ('sd1', 'sd2', 'sd3')}
    for sd in readList:
        print sockets[id(sd)], sd.recvfrom(100)
    print "----------"


sd0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sd1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sd2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sd3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sd0.bind (( '', 7000))
sd1.bind (( '', 7001))
sd2.bind (( '', 7002))
sd3.bind (( '', 7003))

# sd0 is a writing socket
# sd1, sd2, sd3 are reading sockets
sd0.sendto('aaaa', ('localhost', 7001))
sd0.sendto('aaaa', ('localhost', 7001))
sd0.sendto('bbbb', ('localhost', 7002))
sd0.sendto('bbbb', ('localhost', 7002))
sd0.sendto('bbbb', ('localhost', 7002))
sd0.sendto('bbbb', ('localhost', 7002))
sd0.sendto('cccc', ('localhost', 7003))

pollSockets()
pollSockets()
pollSockets()
pollSockets()

1
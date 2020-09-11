import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost',10000)
print(sys.stderr,"starting up on {} port {}".format(server_address[0],server_address[1]) )
s.bind(server_address)
while (True):
    print(sys.stderr,"waiting to recieve message")
    data, address =  s.recvfrom(4096)
    print(sys.stderr,"received {} bytes from {}".format(len(data),address))
    print(sys.stderr, data)
    if data:
        sent = s.sendto(data,address)
        print(sys.stderr, "sent {} bytes back to {}".format(sent,address))
        
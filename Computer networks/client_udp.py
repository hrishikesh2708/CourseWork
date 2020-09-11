import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost',10000)

message = input("Enter the Message You want to pass:")
try:
    print(sys.stderr,"sending {}".format(message))
    sent = s.sendto(message.encode(), server_address)
    print(sys.stderr, "waiting to receive")
    data, server = s.recvfrom(4096)
    print(sys.stderr,"received {}".format(data))
finally:
    print(sys.stderr,"closing socket")
    s.close()
        
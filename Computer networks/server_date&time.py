import sys
import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# machine = socket.gethostname()
# print(machine)
# port = 5050
s.bind((socket.gethostname(),5050))
s.listen(3)
while (True):
    client, address = s.accept()
    print("got connection request form client {}".format(str(address)))
    t=time.ctime(time.time())+ "\r\n"
    client.send(t.encode('ascii'))
    client.close()
    
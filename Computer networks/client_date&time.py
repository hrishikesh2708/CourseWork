import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),5050))
print("connection established")
time = s.recv(1024)
s.close()

print("the thime from the server is {}".format(time.decode('ascii')))
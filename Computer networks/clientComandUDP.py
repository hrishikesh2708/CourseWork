import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port=1488
s.connect((host,port))
print("connected to the server:",host)
while True:
    m=input(str("Command: "))	
    s.sendto(m.encode(),(host,port))
    if(m=="exit"):
        break;
    msgFromServ = s.recvfrom(1024)
    msg = "Output: {}".format(msgFromServ[0].decode())
    print(msg)
s.close()
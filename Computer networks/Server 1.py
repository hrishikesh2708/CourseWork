import socket

HOST = '127.0.0.1' 
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Connection established!!")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                break
            msg = input("Enter Msg: ")    
            conn.sendall(msg.encode())
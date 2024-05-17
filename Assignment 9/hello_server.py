import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 123

s.bind(('',port))

s.listen(5)

while True:
    c,addr = s.accept()

    c_msg = c.recv(1024).decode()

    print(f"Received {c_msg} from client")

    c.send("Hello".encode())

    c.close()

    break

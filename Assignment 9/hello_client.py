import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 123

s.connect(("127.0.0.1",port))

s.send("Hello".encode())

s_msg = s.recv(1024).decode()

print(f"Received {s_msg} from server")
s.close()
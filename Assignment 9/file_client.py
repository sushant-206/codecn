
import socket
file_path = input("Enter path of the file\n")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 123

s.connect(("127.0.0.1",port))

data = ''
with open(file_path,"r") as file:
    data = file.read()

if data:
    s.send(data.encode())
else:
    print("Empty File!")


s_msg = s.recv(1024).decode()

print(s_msg)
s.close()


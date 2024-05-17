import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 123

s.bind(('',port))

s.listen(5)

while True:
    c,addr = s.accept()

    data = c.recv(1024).decode()

    c_msg = 'File transferred successfully!'
    if data:
        print("File received from client")
        with open("output.txt","w") as file:
            file.write(data)
    else:
        c_msg = "File transfer failed no data received"


    c.send(c_msg.encode())

    c.close()

    break

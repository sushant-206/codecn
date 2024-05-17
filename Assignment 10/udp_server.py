import socket
MTU = 1500
ext = [".py",".txt",".mp3",".mp4"]
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

port = 123

s.bind(('',port))

idx = 0
while True:
    data, addr = s.recvfrom(MTU)

    if data == b"END":
        break

    if data == b"transmission started":
        with open(f"output{ext[idx]}", "wb") as file:
            while True:
                data, addr = s.recvfrom(MTU)
                if data == b"transmission completed":
                    break
                file.write(data)
        print("File received!")
        c_msg = 'File transferred successfully!'
        s.sendto(c_msg.encode(), addr)
        idx += 1
    else:
        c_msg = "File transfer failed: No data received"
        s.sendto(c_msg.encode(), addr)

s.close()

        






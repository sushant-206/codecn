import socket
MTU = 1500
file_paths = []
print("Enter path of script file, text file, audio file and video file one by one")
for idx in range(0, 4):
    file_paths.append(input())
for file_path in file_paths:
    with open(file_path, "rb") as file:
        data = file.read()
    port = 123
    if data:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        start_msg = "transmission started".encode()
        end_msg = "transmission completed".encode()
        s.sendto(start_msg, ("127.0.0.1", port))
        if len(data) <= MTU:
            s.sendto(data, ("127.0.0.1", port))
            s.sendto(end_msg, ("127.0.0.1", port))
        else:
            num_packets = (len(data) - 1) // MTU + 1  # Calculate total packets
            for packet_num in range(num_packets):
                start = packet_num * MTU
                end = min((packet_num + 1) * MTU, len(data))
                packet = data[start:end]
                s.sendto(packet, ("127.0.0.1", port))
            s.sendto(end_msg, ("127.0.0.1", port))
        s_msg, addr = s.recvfrom(MTU)
        print(s_msg.decode())
    else:
        print("Empty File!")
s.sendto("END".encode(),("127.0.0.1", port))
s.close()


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

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
        s.sendto(start_msg, ("192.168.56.1", port))
        if len(data) <= MTU:
            s.sendto(data, ("192.168.56.1", port))
            s.sendto(end_msg, ("192.168.56.1", port))
        else:
            num_packets = (len(data) - 1) // MTU + 1  # Calculate total packets
            for packet_num in range(num_packets):
                start = packet_num * MTU
                end = min((packet_num + 1) * MTU, len(data))
                packet = data[start:end]
                s.sendto(packet, ("192.168.56.1", port))
            s.sendto(end_msg, ("192.168.56.1", port))

        s_msg, addr = s.recvfrom(MTU)
        print(s_msg.decode())
    else:
        print("Empty File!")
s.sendto("END".encode(),("192.168.56.1", port))
s.close()
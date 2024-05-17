import socket

PORT = 9010
IP_ADDRESS = "192.168.6.106"

clientSocket = socket.socket()

clientSocket.connect((IP_ADDRESS,PORT))

clientSocket.send("Hello".encode())

print(f"{clientSocket.recv(1024).decode()}")

clientSocket.close()
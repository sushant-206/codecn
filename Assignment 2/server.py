import socket

PORT = 9010
IP_ADDRESS = "192.168.6.106"


serverSocket = socket.socket()

serverSocket.bind((IP_ADDRESS,PORT))

serverSocket.listen(5)
print("Waiting for client")

while True:
    conn , addr = serverSocket.accept()
    print("Client connected from ",addr)

    print(f"{conn.recv(1024).decode()} from {addr}")

    conn.send("Your message is received".encode())

    conn.close()

    break;
    







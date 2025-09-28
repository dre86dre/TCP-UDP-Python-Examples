# UDP Example (Faster but Unreliable)

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 65433))

print("UDP Server is listening on port 65433...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print("Received:", data.decode(), "from", addr)
    server_socket.sendto(b"Hello from UDP server!", addr)
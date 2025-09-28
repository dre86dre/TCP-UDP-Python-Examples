# TCP Example (Reliable Chat)

import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 65432)) # localhost, port 65432
server_socket.listen()

print("TCP Server is listening on port 65432...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024) # receive up to 1024 bytes
    if not data:
        break
    print("Received:", data.decode())
    conn.sendall(b"Hello from TCP server!") # send reply

conn.close()

# Run this file in the terminal
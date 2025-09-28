import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(b"Hello UDP Server!", ("127.0.0.1", 65433))
data, server = client_socket.recvfrom(1024)

print("Server says:", data.decode())
client_socket.close()
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "192.168.1.7"
port = 1234
sock.connect((ip, port)) # get connected with server

print("\n Connected with server")

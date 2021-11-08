import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET --> Ipv4, Sock_stream --> TCP
ip = "192.168.1.7"
port = 1234

server.bind((ip, port))
server.listen()
print(f"\n Server is listening at IP : {ip} and PORT : {port}")
client = server.accept()
print(client)

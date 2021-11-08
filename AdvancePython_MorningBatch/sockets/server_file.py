
import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1234

server.bind((ip, port))  # defined the IP and PORT of server
server.listen()
print(f"\n Server is ready to listen at IP {ip} and PORT {port}")

client_socket, client_addr = server.accept()

print(f"\n Client is running at IP {client_addr[0]} and PORT {client_addr[1]}")
client_socket.send("Your Request is accepted".encode())  # encode --> to convert in bytes mode

cmsg = client_socket.recv(1024).decode()
print(f"\n Client --> {cmsg}") 


path = client_socket.recv(1024).decode() # receiving the file path which the client wants
if os.path.exists(path) and os.path.isfile(path):
    client_socket.send("Sharing file.....".encode())
    with open(path, 'rb') as fp:
        data = fp.readline()
        while data:    
            client_socket.send(data)
            data = fp.readline()
        print("\n File send successfully....")
else:
    client_socket.send("File Does Not Exist... Please check the filename.....".encode())

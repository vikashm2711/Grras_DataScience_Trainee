
import socket

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

break_cond = ['bye', 'bubye', 'tata', 'see you', 'c u', 'ttyl', 'talk to you later']
exit = False
while True:
    # Taking input from server and sending it to client
    smsg = input("\n Server --> ")
    client_socket.send(smsg.encode())
    for i in break_cond:
        if i in smsg.strip().lower():
            print("\n Server want to discontinue....")
            client_socket.close() # releasing the port of the socket
            exit = True
            break
    if exit:
        break
    # Recieving msgs from client
    cmsg = client_socket.recv(1024).decode()
    print("\n CLient --> ", cmsg)
    for i in break_cond:
        if i in cmsg.strip().lower():
            print("\n Client want to discontinue....")
            client_socket.close() # releasing the port of the socket
            exit = True
            break
    if exit:
        break

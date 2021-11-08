
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # that will be working at client side
# and will help to connect with server
ip = input("\n Server IP --> ") # server IP
port = int(input("\n Server PORT --> "))  # server PORT

sock.connect((ip, port))  # connecting with server IP and PORT

smsg = sock.recv(1024).decode()
print(f"\n Server --> {smsg}")

sock.send("Thankyou for accepting request".encode())

path = input("\n Enter the filename/path_of_file which you want : ")
sock.send(path.encode())
ext = os.path.split(path)[1].split(".")[-1]

smsg = sock.recv(1024).decode()
print(f"\n Server --> {smsg}")

if "not exists" not in smsg.lower():
    path = input("\n Enter the path where you want to save the file(without extension) : ")
    path += "." + ext
    with open(path, 'wb') as fp:
        data = sock.recv(2048)
        while data:
            fp.write(data)
            data = sock.recv(2048)
        print("\n File Created Successfully.")

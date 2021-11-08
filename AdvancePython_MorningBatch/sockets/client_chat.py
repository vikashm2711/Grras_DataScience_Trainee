
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # that will be working at client side
# and will help to connect with server
ip = socket.gethostbyname(socket.gethostname())  # server IP
port = 1234  # server PORT

sock.connect((ip, port))  # connecting with server IP and PORT

smsg = sock.recv(1024).decode()
print(f"\n Server --> {smsg}")

sock.send("Thankyou for accepting request".encode())
break_cond = ['bye', 'bubye', 'tata', 'see you', 'c u', 'ttyl', 'talk to you later']
exit = False
while True:
    # Receiving Messages from server
    smsg = sock.recv(1024).decode()
    print("\n Server --> ", smsg)
    for i in break_cond:
        if i in smsg.strip().lower():
            print("\n Server want to discontinue....")
            exit = True
            break
    if exit:
        break
       
    # Sending msgs to server
    cmsg = input("\n Client --> ")
    sock.send(cmsg.encode())
    for i in break_cond:
        if i in cmsg.strip().lower():
            print("\n Client want to discontinue....")
            exit = True
            break
    if exit:
        break

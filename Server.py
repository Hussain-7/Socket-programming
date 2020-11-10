import socket
import threading
import time


HEADER=64
PORT = 5050
# SERVER = "192.168.137.1"
# This is best to run server on any computer no need to change ip again and again
SERVER=socket.gethostbyname(socket.gethostname()); 
Address = (SERVER, PORT)
FORMAT='utf-8'
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Address)
DISCONNECT_MESSAGE="!DISCONNECT"
def handle_client(conn, addr):
    print(f"[NEW CONNECTION]  {addr} connected.")
    connected = True
    while connected:
        # paramater of recv is no of bytes
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                 connected = False
                 break
                 break
    
            print(f"[{addr}] messaged : {msg}")
            msg = msg.upper()
            
            conn.send(msg.encode())

    conn.close()




def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        #we wait haere wiatinh for a connection and when connection accurs its address is stored in addr and the actual object in conn
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Amount of threads represent amount of client created and since there is one thread always running the start thread thats why we subtract 1
        print(f"[Active CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] server is starting....")
start()
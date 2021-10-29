import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'New connection: {addr}')

    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'{addr}: {msg}')

    conn.close()

def start():
    server.listen()
    print(f'Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        therad = threading.Thread(target=handle_client, args=(conn, addr))
        therad.start()
        print(f"\n{threading.active_count() - 1} active connections")
        conn.send('Message from server client test'.encode(FORMAT))

print("Server is starting...")
start()
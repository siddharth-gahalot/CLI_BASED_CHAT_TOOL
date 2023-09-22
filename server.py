import socket
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("LOCALHOST",5555))

server.listen()
all_clients = {}

def client_thread(client):
    while True:
        try:
            msg = client.recv(1024)
            for c in all_clients:
                c.send(msg)
        except:
            for c in all_clients:
                if c != client:
                    c.send(f"{name} HAS LEFT THE CHAT".encode())
            del all_clients[client]
            client.close()
            break

while True:
    print("WAITING FOR CONNECTION.....")
    client , address = server.accept()
    print("CONNECTION ESTABLISHED <>")
    name = client.recv(1024).decode()
    all_clients[client] = name
    
    for c in all_clients:
        if c != client:
            c.send(f"{name} HAS JOINED THE CHAT".encode())
    
    thread = Thread(target = client_thread,args = (client,))
    thread.start()
    
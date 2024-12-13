import socket
import threading
from cli_functions import *

server_side_title()

host = str(input('Insert the host IP ([1] default): '))
if(host == '1'):
    host = '127.0.0.1'

port = int(input(('Insert the port number: ')))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
print("Server has sucessfully initialized")
print(f"IP: {host}, PORT: {port}\n")
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("\n"'{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:

        client, address = server.accept()
        print("> The server has initialized!\n")
        print("> Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("> Nickname is: {}".format(nickname))
        broadcast("> {} joined in the chat!".format(nickname).encode('ascii'))
        client.send('> Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
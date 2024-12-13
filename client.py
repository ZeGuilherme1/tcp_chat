import socket
import threading
from cli_functions import *

client_side_title()

nickname = input("> Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = str(input('> Insert the IP ([1] default): '))
if(ip == '1'):
    ip = '127.0.0.1'

port = int(input('> Insert the port: '))
clean_terminal()

client.connect((ip, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive.thread = threading.Thread(target=receive)
receive.thread.start()

write.thread = threading.Thread(target=write)
write.thread.start()



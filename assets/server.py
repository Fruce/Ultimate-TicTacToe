import socket
import threading
s = socket.socket()
print('Socket created')
s.bind(('0.0.0.0',9999))
s.listen(2)
client = []
print('Waiting for connections')
def listen():
    while True:
        c, addr = s.accept()
        client.append(c)
        print('Connected with', addr)
def chat1():
    while True:
        if len(client)>1:
            client[1].send(client[0].recv(2048))
        else:
            continue
t = threading.Thread(target=listen)
t1 = threading.Thread(target=chat1)
t.start()
t1.start()
while True:
    if len(client)>1:
        client[0].send(client[1].recv(2048))
    else:
        continue
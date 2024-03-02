
# Server to receive messages from a single client and send them back

import socket as s

# HOST = 'localhost'    # for localhost, '127.0.0.1' and '::1' can be used too
HOST = '0.0.0.0'    # to connect from anywhere on the network. Have to configure socket permissions first though (chmod 666) and have to configure port forwarding to get internet traffic.
PORT = 65432       # inoreder to get connections from outside, this port should be forwarded

sck = s.socket(s.AF_INET, s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

sck.bind((HOST, PORT))
sck.listen()
# sck.accept()    # to receive multiple connections, put the accept call into a loop

# to receive only one communication
conn, addr = sck.accept()
data = conn.recv(1024)
print("Connection received from {} : {}".format(addr[0], addr[1]))
conn.sendall("Hi, Welcome to the server!".encode())
print("Waiting for an incoming message...")

while data:
    print(data.decode())
    data = conn.recv(1024)
# print('closing connection')
# conn.close()
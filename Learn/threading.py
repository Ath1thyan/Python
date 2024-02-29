import requests
import threading
import time

def make_request(url):
    while True:
        r = requests.get('http://www.google.com')
        print("Response code from thread #{}: {}".format(name, str(r.status_code)))


if __name__ == '__main__':
    threads = 16
    while threads >= 1:
        print("Thread ID #{} starting...".format(threads))
        t = threading.Thread(target=make_request, args=(threads,))
        threads-=1
        t.start()
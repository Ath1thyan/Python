import requests
import threading
import time

def make_request(url):
    r = requests.get('http://www.google.com')
    print("Response code: " + r.status_code)


if __name__ == '__main__':
    while True:
        make_request()
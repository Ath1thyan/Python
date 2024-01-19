from flask import Flask
import os

app = Flask(__name__)
basename = '/iotcloud'

@app.route(basename + '/')
def index():
   return "Welcome"

def echo(anystring):
    # return os.popen('echo hello').read()
    return anystring
app.add_url_rule(basename + '/echo/<anystring>', 'echo', echo)

if __name__ == '__main__':
    app.run()
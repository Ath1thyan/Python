from flask import Flask
import os

app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return "Hello World"

@app.route('/')
def index():
   return "Welcome"

@app.route('/whoami')
def whoami():
   return os.popen('whoami').read()

def man_ls():
   return "<pre>" + os.popen('man ls').read() + "</pre>"
app.add_url_rule('/cpuinfo', 'man_ls', man_ls)

if __name__ == '__main__':
   app.run(debug=True)
from flask import Flask , redirect, url_for, request, render_template
import os
import math
import jinja2

app = Flask(__name__)

@app.route('/helloworld')
def helloworld():
   return render_template('helloworld.html')

@app.route('/hello')
def hello_world():
   return "Hello World"

@app.route('/')
def index():
   return "Welcome"

@app.route('/whoami', methods = ['GET', 'POST'])
def whoami():
   return os.popen('whoami').read()

@app.route('/isadmin')
def isadmin():
   if whoami()=='root\n':     # \n is added because in terminal, whomai results with a new line character   # instead we can use whoami().strip() == 'root':
      return "yes"
   else:
      return "no"

def manls():
   if isadmin() == "yes":
      return redirect(url_for('error/1000'))
      # return redirect(url_for('error', errorcode=1000))
   else:
      return "<pre>" + os.popen('man ls').read() + "</pre>"    
app.add_url_rule('/ls', 'manls', manls)

@app.route('/error/<int:errorcode>')
def error(errorcode):
   if (errorcode == 1000):
      return "Running as root user"
   elif errorcode == 1001:
      return "No such file or directory"
   else:
      return "unknown error"
   
@app.route('/math/sqrt')
def math_sqrt():
   return {
      "result" : str(math.sqrt(int(request.form['num'])))
   }

if __name__ == '__main__':
   app.run(debug=True)
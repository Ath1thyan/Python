from flask import Flask
import math

app = Flask(__name__)

# @app.route('/<name>')     # To route the site
def hello(name):
   return f"Hello {name}"
app.add_url_rule('/<name>', 'hello', hello)     # We can use this instead of using @app.route

@app.route('/')
def index():
   return "Welcome"

@app.route('/isadmin')
def isadmin():
   return whoami()=='root'

@app.route('/power/<int:a>/<int:b>')
def power(a,b):
    try:
        return "{} to the power of {} is {}".format(a, b, math.pow(a,b))
    except:
        return "Try for lower number"
if __name__ == '__main__':
   app.run(debug=True)
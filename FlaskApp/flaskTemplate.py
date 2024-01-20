from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return "Hello World"



@app.route('/')
def index():
   return "welcome"

@app.route('/helloworld')
def helloworld():
   return render_template('helloworld.html')

if __name__ == '__main_':
    app.run(debug=True)
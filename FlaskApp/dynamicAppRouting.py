from flask import Flask

app = Flask(__name__)

# @app.route('/<name>')     # To route the site
def hello(name):
   return f"Hello {name}"
app.add_url_rule('/<name>', 'hello', hello)     # We can use this instead of using @app.route

@app.route('/')
def index():
   return "Welcome"

if __name__ == '__main__':
   app.run(debug=True)
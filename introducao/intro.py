from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return '<h1>Hello world!!!</h1>'

@app.route('/about')
def about():
    return '<p>About</p>'

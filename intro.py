from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def holle_world():
    return '<p>Hello world!!</p>'

@app.route('/about')
def about():
    return '<h1>About</h1>'
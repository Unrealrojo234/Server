from flask import Flask, render_template
import random , threading

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align:center;color:rebeccapurple'>Happy Birthday Server</h1>"



@app.route('/<to>/<sender>/<age>/<bg>')
def hello(to = None, sender = None,age = None,bg = None):
    return render_template('index.html', receiver = to, sender = sender,age=age,bg=bg)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# Dynamic !
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


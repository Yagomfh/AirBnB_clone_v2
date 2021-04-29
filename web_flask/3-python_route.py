#!/usr/bin/python3
"""Flask module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Main page rout"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route def"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """c_text route"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """python/text route"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
""" import modules"""


from flask import Flask
from urllib.parse import unquote
fl = Flask(__name__)


@fl.route('/', strict_slashes=False)
def say_hellow():
    """ new function"""
    return "Hello HBNB!"


@fl.route('/hbnb', strict_slashes=False)
def hbnb():
    """new tab"""
    return "HBNB"


@fl.route('/c/<text>', strict_slashes=False)
def c(text):
    """new function"""
    new = unquote(text.replace('_', ' '))
    return "C {}".format(new)


@fl.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@fl.route('/python/<text>', strict_slashes=False)
def python(text):
    """new function"""
    new = text.replace('_', ' ')
    return "Python {}".format(new)


if __name__ == '__main__':
    fl.run(host='0.0.0.0', port=5000)

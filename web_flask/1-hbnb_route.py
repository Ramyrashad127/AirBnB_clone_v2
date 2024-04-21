#!/usr/bin/python3
""" import modules"""



from flask import Flask
fl = Flask(__name__)


@fl.route('/', strict_slashes=False)
def say_hellow():
    """ new function"""
    return "Hello HBNB!"


@fl.route('/hbnb', strict_slashes=False)
def hbnb():
    """new tab"""
    return "HBNB"


if __name__ == '__main__':
    fl.run(host='0.0.0.0', port=5000)

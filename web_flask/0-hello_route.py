#!/usr/bin/python3
from flask import Flask


"""import flask"""
fl = Flask(__name__)


@fl.route('/', strict_slashes=False)
def say_hellow():
    """ new function"""
    return "Hello HBNB!"


if __name__ == '__main__':
    fl.run(host='0.0.0.0', port=5000)

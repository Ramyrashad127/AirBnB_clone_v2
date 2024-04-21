#!/usr/bin/python3
""" import modules"""


from flask import Flask, render_template
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


@fl.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """print a number"""
    if(isinstance(n, int)):
        return "{} is a number".format(n)


@fl.route('/number_template/<int:n>', strict_slashes=False)
def show(n):
    """html file"""
    if(isinstance(n, int)):
        return render_template('5-number.html', number=n)


@fl.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd(n):
    """odd number"""
    if(isinstance(n, int)):
        if(n % 2 == 0):
            return render_template(
                '6-number_odd_or_even.html', number=n, odd_or_even='even')
        else:
            return render_template(
                '6-number_odd_or_even.html', number=n, odd_or_even='odd')


if __name__ == '__main__':
    fl.run(host='0.0.0.0', port=5000)

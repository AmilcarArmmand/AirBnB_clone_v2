#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Route of '/' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Route of '/hbnb' """
    return 'HBNB'
if __name__ == "__main__":
    """Externally visible server"""
    app.run(host='0.0.0.0', port='5000')

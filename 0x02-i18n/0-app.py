#!/usr/bin/env python3
'''
0. Basic Flask app
'''
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def basic()-> str:
    '''
    Basic app that displays template messages
    under 'title' annd 'h1' tags 
    '''
    tittle = "Welcome to Holberton"
    message = "Hello world"

    return render_template("0-index.html", tittle=tittle, message=message)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__) # initialize Flask with name of the module
manager = Manager(app) # initialize CLI manager

@app.route('/')
def index():
    return "Welcome to MSTPit!"


if __name__ == "__main__":
    manager.run()

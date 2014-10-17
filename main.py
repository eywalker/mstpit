from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__) # initialize Flask with name of the module
manager = Manager(app) # initialize CLI manager
bootstrap = Bootstrap(app) # initialize bootstrap templates

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    manager.run()

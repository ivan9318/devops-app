#download the module from flask
from flask import Flask

#We create the constructor
app=Flask(__name__)

#We are going to mention which url we need to use
@app.route('/')
def hello_world():
    return "Hello world"

#main driver
if __name__=='__main__':
    app.run()
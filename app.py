#download the module from flask
from flask import Flask,render_template

#We create the constructor
app=Flask(__name__)

#We are going to mention which url we need to use
@app.route('/index')
def hello_world():
    return render_template("index.html")

#main driver
if __name__=='__main__':
    app.run()
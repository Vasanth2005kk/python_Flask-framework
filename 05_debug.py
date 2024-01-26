# this not titile() notin python program this identified the web useing the debug method 
#console locked in open for (debugger PIN: 909-132-752) in output print it.

import flask

app=flask.Flask(__name__)

@app.route("/<name>")
def index(name):
    return "<h1> hellow {} </h1>".format(name.titile())


# or

@app.route("/user/<name>")
def user(name):
    return "<h1>your name is {}</h1>".format(name[50])

app.run(debug=True)

#not working for debug

#app.run(debug=Flase) or app.run()

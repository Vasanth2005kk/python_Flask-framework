'''
1. a varible in the route<varible>
2. a parameter pussed in to the function

eg:
 @app.route("/page_name/<name>)
 def functon_name(name):
    ---------------
    ---------------
    ---------------
    return '''

#sample program in example 


import flask 

app=flask.Flask(__name__)

@app.route("/<name>")
def username_print(name):
    #return "<h1>wellocome for {}</h1>".format(name)
    return f"<h1>wellocme for {name} </h1>"

app.run(debug=True)

#or
'''
import flask 

app=flask.Flask(__name__)

@app.route("/")
def index():
    return "<h1>hoem page</h1>"

@app.route("/user/<name>")
def username_print(name):
    #return "<h1>wellocome for {}</h1>".format(name)
    return f"<h1>wellocme for {name} </h1>"

app.run(debug=True)'''
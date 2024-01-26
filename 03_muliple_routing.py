from flask import Flask

app=Flask(__name__)

@app.route("/") #this webpage home 
def index():
    return "<center><h1>HOME PAGE</h1></center>"

@app.route("/call") #contacts 
def call():
    return "<h1>call : +91 8220921078 <br> my phone number </h1>"
@app.route("/about")

def about():
    return "<h1>about page</h1>"

if __name__=="__main__":
    app.run(debug=True)
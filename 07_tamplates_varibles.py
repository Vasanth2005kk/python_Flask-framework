import flask

app=flask.Flask(__name__)

@app.route("/<name>")
def index(name):
    list_1=["vasanth","hari","siva","ragu","ranjith","vicky","santhosh"]
    dic={
        "name":name,
        "age":18,
        "city":"parikkal"
    }
    return flask.render_template("07_tamplates_varibles.html",user_name=name,list_of_names=list_1,dic=dic)


if __name__=="__main__":
    app.run(debug=True)
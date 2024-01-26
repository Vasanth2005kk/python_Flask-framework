#render_template in create floder name in ==(templates) not letter changed not working for rander_tamplate
#why
#setof the HTML code in access in for render_template
 
import flask

app=flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("06_template.html")

app.run(debug=True)

import flask

app=flask.Flask(__name__)

@app.route("/")
def home():
    subjcet=["tamil","english","maths","science","social science"]
    return flask.render_template("08_template_control_for_loop.html",subjcets=subjcet)

if __name__=="__main__":
    app.run(debug=True)

'''
    <!--
        <center>
        <h1>Template Control For Loop</h1>
        <hr>
        <h1>for loop access HTML</h1>
        <h3>{% for i in stored_datas%}</h3>
        <h3>print == {{i}}</h3>
        <h3>for loop finshing {% forend %}</h3>
        <hr>
    </center>
    -->
'''
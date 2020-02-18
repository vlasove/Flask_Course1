from flask import Flask 
app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return "<h1>Hello Bob!</h1>"

app.run(port=8080, debug=True)
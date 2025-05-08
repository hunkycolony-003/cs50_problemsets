# Using a single route when the form is in 'GET' method

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",)
def index():
    name = request.args.get("name")
    if name == "" or name:
        return render_template("greet.html", name=name)
    return render_template("index.html")

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello</h1>"

@app.route("/greet")
def great():
    name = request.args.get("name","Guest")
    return f"<h1>hello {name}</h1>"

@app.route("/about")
def about():
    return render_template("about.html", title = "About me")
        
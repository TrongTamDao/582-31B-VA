# What is templating?
# Flask uses Jinja templates for rending HTML, and you should note that Jinja autoescapes rendered user input in HTML by default

# Why templates?
# Templates allow:
# 1. cleaner HTML files
# 2. dynamic placehodlers
# 3. loops and conditions
# 4. separation between Python logic and page structure

from flask import Flask, render_template, request # import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    # render_template tells Flask to render an HTML template
    return render_template("home.html", title ="Welcom", message="Hello from Flask template")
    # title and message are passed from Python into the template inside HTML file {{variable_name}} outputs values in Jinja templates
    
@app.route("/games")
def games():
    # prepare the list
    game_list = ["Street figher", "Tetris", "Pac-Man"]
    
    #send the list as a parameter
    return render_template("games.html",games=game_list)

# looking at request data (read data from the URL)
@app.route("/greet")
def greet():
    # flask can read name from the request
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}</h1>"

@app.route("/welcome")
def welcome():
    name = request.args.get("name", "Tam")
    program = request.args.get("program", "Web designer")
    return f"<h1>{name} studies in the {program} program.</h1>"


# So in this example, you've learned the core Flask workflow:

# @app.route(...) → defines a URL.
# A function handles the request.
# render_template() sends data to HTML.
# {{ variable }} displays data in templates.
# {% for %} loops through lists in templates.
# request.args.get() reads values from the URL.
# Flask returns HTML back to the browser.
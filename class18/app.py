from flask import Flask

app = Flask(__name__) # create application object. __name__is commonly used here so Flask knows where to look for resources

# The browser displays interface
# the backend receives requests
# the backend decide what data or page should send back
# the backed may validate input, apply business rules, talk to a database, render template and return a response.

# IMPORTANT: never name your file flask.py
# associate the URL path with the function below
@app.route("/")
def hello():
    return "<h1>Hello, Flask!</h1>" # returns the response to the browser

@app.route("/about")
def about():
    name = "Jane"
    return f"<h1>About</h1> <p>This is about page for {name}</p>"

@app.route("/contact")
def contact():
    return "<h1>Contact</h1> <p>Contact us here</p>"

# Request - response cycle:
# 1. browser requests an URL
# 2. Flask receives the request
# 3. Flask match a route
# 4. Python function runs
# 5. response is return
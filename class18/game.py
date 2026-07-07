from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>testing</p>"

@app.route("/games")
def games():
    games_list = ""

    for i in range(1,4):
        games_list += f"<li>Game {i}</li>"

    return f"""
    <h1>Games List:</h1>
    <ul>{games_list}</ul>
    """
    # return "<ul><li>Game 1</li><li>Game 2</li><li>Game 3</li></ul>"

@app.route("/students")
def students():
    return "welcome to students page"
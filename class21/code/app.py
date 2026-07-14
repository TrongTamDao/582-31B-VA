from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///albums.db"#1 error
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) #2 error


class Album(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(120),
        nullable=False
    )

    artist = db.Column(
        db.String(120),
        nullable=False
    )

    genre = db.Column(
        db.String(80),
        nullable=False
    )

    year = db.Column(
        db.String(4),
        nullable=False
    )

    stock = db.Column(
        db.Integer,
        nullable=False,
        default=0 #3 error
    )

    @property
    def in_stock(self):
        return self.stock > 0 #4 error

    def __repr__(self):
        return str(self.id) #5 error


with app.app_context(): #6 error
    db.create_all()


@app.route("/")
def index():
    genre = request.args.get("genre", "") #7 error

    if genre:
        albums = Album.query.filter_by(
            genre=genre #8 error
        ).all()
    else:
        albums = Album.query.all() #8 error

    return render_template(
        "index.html",
        albums=albums, #9 error
        selected_genre=genre
    )


@app.route(
    "/albums/add",
    methods=["GET", "POST"] #10 error
)
def add_album():
    if request.method == "POST":
        album = Album(
            title=request.form["album_name"],
            artist=request.form["artist"],
            genre=request.form["genre"],
            year=request.form["year"],
            stock=request.form["stock"]
        )
        db.session.add(album) #11 error
        db.session.commit()

        return redirect(
            url_for("index") #12 error
        )

    return render_template(
        "add_album.html"
    )


@app.route(
    "/albums/<int:album_id>/edit",
    methods=["GET", "POST"]
)
def edit_album(album_id):
    album = Album.query.get_or_404(album_id)

    if request.method == "POST":
        album.title = request.form["title"]
        album.artist = request.form["artist"]
        album.genre = request.form["genre"]
        album.year = request.form["year"]
        album.stock = request.form["amount"]

        return redirect(
            url_for(
                "edit_album",
                id=album.id
            )
        )

    return render_template(
        "add_album.html",
        album=album
    )


@app.route(
    "/albums/<int:album_id>/delete",
    methods=["GET"]
)
def delete_album(album_id):
    album = Album.query.get_or_404(album_id)

    db.session.delete(album)

    return redirect(
        url_for("index")
    )


if __name__ == "__main__":
    app.run(debug=True)
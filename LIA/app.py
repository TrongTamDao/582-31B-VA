"""Shelf — a personal reading-list application.

Run locally with:

    python app.py

The application is built by `create_app()` rather than at import time. That
keeps configuration in one place, avoids module-level mutable state, and lets
a test suite build an isolated instance with a different database.
"""

import os

from flask import Flask, redirect, render_template, url_for
from flask_login import LoginManager, current_user

from auth import auth_bp
from books import books_bp
from models import (
    MAX_AUTHOR_LENGTH,
    MAX_EMAIL_LENGTH,
    MAX_NOTE_LENGTH,
    MAX_TITLE_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_PASSWORD_LENGTH,
    ReadingStatus,
    User,
    db,
)

#: Fallback used only for local development. In any real deployment the key
#: must come from the environment, since a predictable key lets an attacker
#: forge session cookies.
DEV_SECRET_KEY = "dev-only-change-me"

DATABASE_FILENAME = "shelf.db"


def create_app(database_uri=None):
    """Build and configure the Flask application.

    :param database_uri: Optional SQLAlchemy URI. Defaults to a SQLite file
        next to this module. Tests can pass an in-memory URI instead.
    :returns: A configured :class:`~flask.Flask` instance.
    """
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", DEV_SECRET_KEY)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri or f"sqlite:///{DATABASE_FILENAME}"
    # Off by default in newer versions, but set explicitly: the signalling it
    # enables costs memory and this application does not use it.
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    _configure_login(app)
    _register_blueprints(app)
    _register_template_globals(app)
    _register_error_handlers(app)

    @app.route("/")
    def index():
        """Send visitors to their shelf, or to the login page if signed out."""
        if current_user.is_authenticated:
            return redirect(url_for("books.list_books"))
        return redirect(url_for("auth.login"))

    with app.app_context():
        db.create_all()

    return app


def _configure_login(app):
    """Wire up Flask-Login."""
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Where `@login_required` sends anonymous visitors.
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please sign in to view your shelf."
    login_manager.login_message_category = "error"

    @login_manager.user_loader
    def load_user(user_id):
        """Reload a user from the id stored in the session cookie."""
        return db.session.get(User, int(user_id))


def _register_blueprints(app):
    """Attach the feature blueprints to the application."""
    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)


def _register_template_globals(app):
    """Expose shared constants to every template.

    Injecting the limits means the `maxlength` attributes in the markup are
    generated from the same constants the server validates against, so the two
    can never disagree.
    """

    @app.context_processor
    def inject_constants():
        return {
            "READING_STATUSES": ReadingStatus.ALL,
            "MAX_USERNAME_LENGTH": MAX_USERNAME_LENGTH,
            "MAX_EMAIL_LENGTH": MAX_EMAIL_LENGTH,
            "MIN_PASSWORD_LENGTH": MIN_PASSWORD_LENGTH,
            "MAX_TITLE_LENGTH": MAX_TITLE_LENGTH,
            "MAX_AUTHOR_LENGTH": MAX_AUTHOR_LENGTH,
            "MAX_NOTE_LENGTH": MAX_NOTE_LENGTH,
        }


def _register_error_handlers(app):
    """Render friendly pages instead of the default error output."""

    @app.errorhandler(404)
    def not_found(error):
        return render_template("error.html", code=404,
                               message="That page could not be found."), 404

    @app.errorhandler(500)
    def server_error(error):
        # Roll back so a failed transaction cannot leak into the next request.
        db.session.rollback()
        return render_template("error.html", code=500,
                               message="Something went wrong on our end."), 500


if __name__ == "__main__":
    create_app().run(debug=True)

"""Database models for Shelf.

Defines the two entities in the application and the one-to-many
relationship between them:

    User 1 ──────── * Book

A user owns many books; every book belongs to exactly one user.
"""

from datetime import datetime, timezone

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


# ─── Field length limits ──────────────────────────────────────────────────────
# These are the single source of truth for length rules. They are imported by
# the validators (server-side checks) and injected into templates so the
# `maxlength` attributes in the HTML can never drift out of sync with the
# rules enforced on the server.

MAX_USERNAME_LENGTH = 50
MAX_EMAIL_LENGTH = 120
MAX_PASSWORD_HASH_LENGTH = 255

MIN_USERNAME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8

MAX_TITLE_LENGTH = 100
MAX_AUTHOR_LENGTH = 100
MAX_NOTE_LENGTH = 1000


class ReadingStatus:
    """The three states a book can be in.

    Grouped in a class rather than left as loose strings so that the valid
    values, their display order, and the default are defined in one place.
    """

    WANT_TO_READ = "Want to read"
    READING = "Reading"
    FINISHED = "Finished"

    #: Every permitted status, in the order they should appear in a dropdown.
    ALL = (WANT_TO_READ, READING, FINISHED)

    #: The status assigned to a newly added book.
    DEFAULT = WANT_TO_READ


def _utc_now():
    """Return the current time as a timezone-aware UTC datetime.

    Used as a column default. Passed as a callable (not called here) so that
    SQLAlchemy evaluates it at insert time rather than at import time.
    """
    return datetime.now(timezone.utc)


class User(db.Model, UserMixin):
    """A registered account.

    Inherits `UserMixin` to satisfy the interface Flask-Login expects
    (`is_authenticated`, `is_active`, `is_anonymous`, `get_id`).

    Passwords are never stored. Only a salted hash is persisted, written
    through `set_password` and verified through `check_password`.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_USERNAME_LENGTH), unique=True, nullable=False)
    email = db.Column(db.String(MAX_EMAIL_LENGTH), unique=True, nullable=False)
    password_hash = db.Column(db.String(MAX_PASSWORD_HASH_LENGTH), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=_utc_now, nullable=False)

    # `cascade="all, delete-orphan"` means deleting a user also deletes their
    # books, so no orphaned rows are left behind.
    books = db.relationship(
        "Book",
        back_populates="owner",
        cascade="all, delete-orphan",
        lazy="select",
    )

    def set_password(self, password):
        """Hash `password` and store the result.

        The plain-text password is discarded; only the hash is kept.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Return True if `password` matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username!r}>"


class Book(db.Model):
    """A single entry in one user's reading list."""

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(MAX_TITLE_LENGTH), nullable=False)
    author = db.Column(db.String(MAX_AUTHOR_LENGTH), nullable=False)
    note = db.Column(db.String(MAX_NOTE_LENGTH), nullable=True)
    status = db.Column(
        db.String(20), nullable=False, default=ReadingStatus.DEFAULT
    )
    created_at = db.Column(db.DateTime(timezone=True), default=_utc_now, nullable=False)

    # The owning user. This is set from `current_user` when a book is created,
    # never from user-supplied form data.
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship("User", back_populates="books")

    def is_owned_by(self, user):
        """Return True if `user` is the owner of this book.

        Centralising the ownership test here keeps the comparison consistent
        everywhere it is needed and makes the intent explicit at call sites.
        """
        return self.user_id == user.id

    def __repr__(self):
        return f"<Book {self.title!r} owner_id={self.user_id}>"

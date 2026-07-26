"""Reading-list routes: list, create, edit and delete books.

Every route in this blueprint is protected by `@login_required`, and every
route that touches a specific book resolves it through `_get_owned_book`,
which refuses to return a book belonging to somebody else.
"""

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from models import Book, ReadingStatus, db
from validators import validate_book

books_bp = Blueprint("books", __name__, url_prefix="/books")

#: Where to go after a successful create, edit or delete.
LIST_ENDPOINT = "books.list_books"


def _get_owned_book(book_id):
    """Fetch a book by id, but only if it belongs to the current user.

    Filtering by `user_id` in the query itself — rather than fetching the row
    and comparing afterwards — means another user's book is never loaded into
    memory at all. A book that exists but belongs to someone else produces a
    404 rather than a 403, so the response does not reveal that the id is real.

    Aborts with 404 if no matching book is found.
    """
    book = Book.query.filter_by(id=book_id, user_id=current_user.id).first()

    if book is None:
        abort(404)

    return book


def _read_book_form():
    """Pull the book fields out of the submitted form.

    Shared by the create and edit routes so the field names and the
    whitespace handling are written once.

    Returns a dict matching the `Book` attribute names, so it can be used
    both to populate a new record and to re-render the form after an error.
    """
    return {
        "title": request.form.get("title", "").strip(),
        "author": request.form.get("author", "").strip(),
        # An empty note is stored as None rather than "" so that "no note"
        # has exactly one representation in the database.
        "note": request.form.get("note", "").strip() or None,
        "status": request.form.get("status", ReadingStatus.DEFAULT),
    }


@books_bp.route("/")
@login_required
def list_books():
    """Show every book belonging to the signed-in user.

    The query is scoped to `current_user`, so there is no way to see another
    account's list from this page.
    """
    books = (
        Book.query.filter_by(user_id=current_user.id)
        .order_by(Book.created_at.desc())
        .all()
    )

    return render_template("books.html", books=books)


@books_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_book():
    """Add a book to the current user's list."""
    if request.method == "POST":
        fields = _read_book_form()
        errors = validate_book(**fields)

        if errors:
            for error in errors:
                flash(error, "error")
            # `book=fields` lets the shared template redisplay the submitted
            # values; a dict works here because the template only reads keys
            # that both a dict and a Book instance expose.
            return render_template("book_form.html", book=fields, is_edit=False)

        # The owner comes from the session, never from the form — a user
        # cannot create a book on somebody else's shelf.
        book = Book(**fields, user_id=current_user.id)

        db.session.add(book)
        db.session.commit()

        flash(f"Added “{book.title}” to your shelf.", "success")
        return redirect(url_for(LIST_ENDPOINT))

    return render_template("book_form.html", book=None, is_edit=False)


@books_bp.route("/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    """Update one of the current user's books.

    Changing the id in the URL to another user's book yields a 404 because
    `_get_owned_book` scopes the lookup to the signed-in account.
    """
    book = _get_owned_book(book_id)

    if request.method == "POST":
        fields = _read_book_form()
        errors = validate_book(**fields)

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("book_form.html", book=fields, is_edit=True, book_id=book_id)

        # Assign field by field so `user_id` can never be overwritten by a
        # crafted form submission.
        for attribute, value in fields.items():
            setattr(book, attribute, value)

        db.session.commit()

        flash(f"Updated “{book.title}”.", "success")
        return redirect(url_for(LIST_ENDPOINT))

    return render_template("book_form.html", book=book, is_edit=True, book_id=book_id)


@books_bp.route("/<int:book_id>/delete", methods=["POST"])
@login_required
def delete_book(book_id):
    """Remove one of the current user's books.

    POST-only so the deletion cannot be triggered by following a link.
    """
    book = _get_owned_book(book_id)
    title = book.title

    db.session.delete(book)
    db.session.commit()

    flash(f"Removed “{title}” from your shelf.", "success")
    return redirect(url_for(LIST_ENDPOINT))

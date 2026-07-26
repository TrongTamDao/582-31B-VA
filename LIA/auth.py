"""Authentication routes: registration, login and logout.

Kept in its own blueprint so that account handling is separate from the
reading-list feature and each module stays small enough to read at a glance.
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from models import User, db
from validators import validate_registration

auth_bp = Blueprint("auth", __name__)

#: Where to send a user once they are authenticated.
HOME_ENDPOINT = "books.list_books"


def _redirect_if_logged_in():
    """Return a redirect response if the visitor is already signed in.

    Registration and login pages are meaningless to an authenticated user, so
    both routes call this first. Returning the response (rather than issuing
    the redirect here) lets the caller decide by returning it directly.
    """
    if current_user.is_authenticated:
        return redirect(url_for(HOME_ENDPOINT))
    return None


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Create a new account.

    On GET, render an empty form. On POST, validate the submission and either
    re-render the form with errors and the previously entered values, or
    create the account and sign the new user in.
    """
    already_signed_in = _redirect_if_logged_in()
    if already_signed_in:
        return already_signed_in

    if request.method == "POST":
        # `.strip()` so that a field of only spaces counts as blank.
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        errors = validate_registration(username, email, password, confirm_password)

        if errors:
            for error in errors:
                flash(error, "error")
            # Re-render with the submitted values so the user does not have to
            # retype everything. Passwords are deliberately not echoed back.
            return render_template("register.html", username=username, email=email)

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash(f"Welcome to Shelf, {user.username}! Your account has been created.", "success")
        return redirect(url_for(HOME_ENDPOINT))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Sign an existing user in."""
    already_signed_in = _redirect_if_logged_in()
    if already_signed_in:
        return already_signed_in

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()

        # A single message for both "no such user" and "wrong password" so the
        # form cannot be used to discover which usernames exist.
        if user is None or not user.check_password(password):
            flash("Incorrect username or password.", "error")
            return render_template("login.html", username=username)

        login_user(user)
        flash(f"Signed in as {user.username}.", "success")
        return redirect(url_for(HOME_ENDPOINT))

    return render_template("login.html")


@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    """Sign the current user out.

    POST-only: a link that logs you out on GET can be triggered by any page
    that embeds it as an image or is prefetched by the browser.
    """
    logout_user()
    flash("You have been signed out.", "success")
    return redirect(url_for("auth.login"))

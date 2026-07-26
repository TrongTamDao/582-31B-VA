"""Server-side validation helpers.

The HTML forms use `required` and `maxlength`, but browser validation is only
a convenience: it can be bypassed by editing the page or by posting directly.
Every rule enforced in the markup is therefore re-checked here.

Each public function returns a list of human-readable error strings. An empty
list means the input is valid. Returning errors rather than raising keeps the
routes flat and lets a form report every problem at once instead of one at a
time.
"""

import re

from models import (
    MAX_AUTHOR_LENGTH,
    MAX_EMAIL_LENGTH,
    MAX_NOTE_LENGTH,
    MAX_TITLE_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_PASSWORD_LENGTH,
    MIN_USERNAME_LENGTH,
    ReadingStatus,
    User,
)

#: Deliberately permissive. Real address validity can only be proven by sending
#: mail to it, so this rejects obvious typos without blocking unusual addresses.
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

#: Usernames are used in URLs and greetings, so restrict them to characters
#: that are unambiguous and safe to display.
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+$")


def _check_required_text(value, field_label, max_length):
    """Validate one required text field.

    Shared by every required field so the "blank" and "too long" rules are
    written once rather than repeated per field.

    Returns a list containing at most one error message.
    """
    if not value:
        return [f"{field_label} is required."]

    if len(value) > max_length:
        return [f"{field_label} may not exceed {max_length} characters."]

    return []


def validate_registration(username, email, password, confirm_password):
    """Validate a registration submission.

    Checks format and length first, then queries for uniqueness only if the
    value is otherwise well-formed — there is no point asking the database
    about a username that was already rejected.
    """
    errors = []

    # ── Username ──
    username_errors = _check_required_text(username, "Username", MAX_USERNAME_LENGTH)
    if username_errors:
        errors += username_errors
    elif len(username) < MIN_USERNAME_LENGTH:
        errors.append(f"Username must be at least {MIN_USERNAME_LENGTH} characters.")
    elif not USERNAME_PATTERN.match(username):
        errors.append("Username may only contain letters, numbers, dots, hyphens and underscores.")
    elif User.query.filter_by(username=username).first():
        errors.append("That username is already taken.")

    # ── Email ──
    email_errors = _check_required_text(email, "Email", MAX_EMAIL_LENGTH)
    if email_errors:
        errors += email_errors
    elif not EMAIL_PATTERN.match(email):
        errors.append("Please enter a valid email address.")
    elif User.query.filter_by(email=email).first():
        errors.append("An account already exists for that email address.")

    # ── Password ──
    if not password:
        errors.append("Password is required.")
    elif len(password) < MIN_PASSWORD_LENGTH:
        errors.append(f"Password must be at least {MIN_PASSWORD_LENGTH} characters.")
    elif password != confirm_password:
        errors.append("The two passwords do not match.")

    return errors


def validate_book(title, author, note, status):
    """Validate a book submission (used for both creating and editing)."""
    errors = []

    errors += _check_required_text(title, "Title", MAX_TITLE_LENGTH)
    errors += _check_required_text(author, "Author", MAX_AUTHOR_LENGTH)

    # The note is optional, so only the length rule applies.
    if note and len(note) > MAX_NOTE_LENGTH:
        errors.append(f"Note may not exceed {MAX_NOTE_LENGTH} characters.")

    # Guard against a hand-crafted POST containing an arbitrary status value.
    if status not in ReadingStatus.ALL:
        errors.append("Please choose a valid reading status.")

    return errors

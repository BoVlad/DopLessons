from functools import wraps
from flask import session, redirect, url_for, request


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


def login_forbidden(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") and session.get("user_role"):
            return f(*args, **kwargs)
        return redirect(url_for("login"))
    return decorated_function


def user_in_session():
    return bool(session.get("user_id"))


def get_user_role():
    if user_in_session:
        return session.get("user_role")
    else:
        return None

    
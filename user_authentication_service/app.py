#!/usr/bin/env python3
"""App module
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """Endpoint returning a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users",  methods=['POST'], strict_slashes=False)
def register_user():
    """ Endpoint to register a user.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """ Endpoint to log in a user.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):

        session_id = AUTH.create_session(email)
        response = make_response(jsonify({"email": email,
                                          "message": "logged in"}))
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """ Endpoint to log out a user.
    """
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        response = make_response(redirect('/'))
        response.set_cookie('session_id', '', expires=0)
        return response
    else:
        abort(403)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile():
    """ Endpoint to get a user's profile information.
    """
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

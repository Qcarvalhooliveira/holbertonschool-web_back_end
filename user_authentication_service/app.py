#!/usr/bin/env python3
"""App module
"""

from flask import Flask, jsonify, request, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

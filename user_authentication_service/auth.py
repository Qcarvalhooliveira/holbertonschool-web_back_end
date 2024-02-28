#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with a randomly-generated salt
    and returns the salted, hashed password.
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """ Generates a new UUID and returns its string representation.
    """
    return str(uuid.uuid4())


class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializes a new instance of the class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user with a given email and password.

            Args:
                email (str): The email address of the new user.
                password (str): The plaintext password of the new user.

            Returns:
                User: The instance of the newly created User object.
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates if a given email and password correspond to a valid user.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

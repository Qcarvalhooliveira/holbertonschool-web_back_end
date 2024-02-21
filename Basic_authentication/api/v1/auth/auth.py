#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth():
    """ Class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required for the given path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves the Authorization header from the request.
        """
        return None

    def current_user(self, request=None) -> User:
        """ Retrieves the current user from the request.
        """
        return None

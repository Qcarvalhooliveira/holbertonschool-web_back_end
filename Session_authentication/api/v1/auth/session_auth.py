#!/usr/bin/env python3
"""
Authentication module for the API
"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Class to manage session authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID for a user_id.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie value.
        """

        cookie = self.session_cookie(request)

        session_user_id = self.user_id_for_session_id(cookie)

        user_id = User.get(session_user_id)

        return user_id
    
    def destroy_session(self, request=None):
        """Deletes the user session / logout."""
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True

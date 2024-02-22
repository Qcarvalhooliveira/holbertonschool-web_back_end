#!/usr/bin/env python3
"""
Authentication module for the API
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Class to manage basic authentication."""
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts the Base64 part of the Authorization header.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        base64_part = authorization_header[6:]
        return base64_part

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Returns the decoded value of a Base64 string."""
        if base64_authorization_header is None \
           or not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None

#!/usr/bin/env python3
""" doc doc doc"""

from base64 import b64decode
from typing import Optional
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """doc doc doc"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """doc doc doc"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        value = authorization_header.split(' ')[1]
        return value

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """doc doc doc"""
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded_base64 = b64decode(base64_authorization_header)
            decoded_base64 = encoded_base64.decode('utf-8')
        except Exception:
            return None
        return decoded_base64

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str)
    """doc doc doc"""

    if __name__ == "__main__":
        a = BasicAuth()

        print(a.decode_base64_authorization_header(None))
        print(a.decode_base64_authorization_header(89))
        print(a.decode_base64_authorization_header("Holberton School"))
        print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
        print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
        print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))

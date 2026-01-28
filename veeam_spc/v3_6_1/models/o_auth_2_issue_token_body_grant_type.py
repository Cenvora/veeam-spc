from enum import Enum


class OAuth2IssueTokenBodyGrantType(str, Enum):
    AS = "as"
    AUTHORIZATION_CODE = "authorization_code"
    MFA = "mfa"
    PASSWORD = "password"
    PUBLIC_KEY = "public_key"
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)

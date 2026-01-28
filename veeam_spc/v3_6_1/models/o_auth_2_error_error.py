from enum import Enum


class OAuth2ErrorError(str, Enum):
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    INVALID_REQUEST = "invalid_request"
    INVALID_SCOPE = "invalid_scope"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"

    def __str__(self) -> str:
        return str(self.value)

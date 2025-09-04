from enum import Enum


class IdentityProviderType(str, Enum):
    SAML2 = "SAML2"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

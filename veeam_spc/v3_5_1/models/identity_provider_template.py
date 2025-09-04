from enum import Enum


class IdentityProviderTemplate(str, Enum):
    ADFS = "ADFS"
    CUSTOM = "Custom"
    KEYCLOAK = "Keycloak"
    OKTA = "Okta"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

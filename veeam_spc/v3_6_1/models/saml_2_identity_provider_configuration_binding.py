from enum import Enum


class Saml2IdentityProviderConfigurationBinding(str, Enum):
    ARTIFACT = "Artifact"
    HTTPPOST = "HttpPost"
    HTTPREDIRECT = "HttpRedirect"

    def __str__(self) -> str:
        return str(self.value)

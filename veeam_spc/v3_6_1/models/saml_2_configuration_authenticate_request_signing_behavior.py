from enum import Enum


class Saml2ConfigurationAuthenticateRequestSigningBehavior(str, Enum):
    ALWAYS = "Always"
    IFIDPWANTAUTHNREQUESTSSIGNED = "IfIdpWantAuthnRequestsSigned"
    NEVER = "Never"

    def __str__(self) -> str:
        return str(self.value)

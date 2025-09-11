from enum import Enum


class Saml2ServiceCertificateConfigurationUse(str, Enum):
    BOTH = "Both"
    ENCRYPTION = "Encryption"
    SIGNING = "Signing"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class Saml2ServiceCertificateConfigurationStatus(str, Enum):
    CURRENT = "Current"
    FUTURE = "Future"

    def __str__(self) -> str:
        return str(self.value)

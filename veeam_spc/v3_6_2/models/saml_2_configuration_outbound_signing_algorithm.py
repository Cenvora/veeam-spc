from enum import Enum


class Saml2ConfigurationOutboundSigningAlgorithm(str, Enum):
    RSASHA1 = "RsaSha1"
    RSASHA256 = "RsaSha256"
    RSASHA384 = "RsaSha384"
    RSASHA512 = "RsaSha512"

    def __str__(self) -> str:
        return str(self.value)

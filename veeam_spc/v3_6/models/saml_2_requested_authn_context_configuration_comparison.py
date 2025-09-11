from enum import Enum


class Saml2RequestedAuthnContextConfigurationComparison(str, Enum):
    BETTER = "Better"
    EXACT = "Exact"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"

    def __str__(self) -> str:
        return str(self.value)

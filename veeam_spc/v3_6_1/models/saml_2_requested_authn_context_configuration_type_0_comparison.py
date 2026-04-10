from enum import Enum


class Saml2RequestedAuthnContextConfigurationType0Comparison(str, Enum):
    BETTER = "Better"
    EXACT = "Exact"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"

    def __str__(self) -> str:
        return str(self.value)

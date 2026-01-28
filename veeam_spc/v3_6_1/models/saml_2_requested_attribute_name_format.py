from enum import Enum


class Saml2RequestedAttributeNameFormat(str, Enum):
    BASIC = "Basic"
    UNSPECIFIED = "Unspecified"
    URI = "Uri"

    def __str__(self) -> str:
        return str(self.value)

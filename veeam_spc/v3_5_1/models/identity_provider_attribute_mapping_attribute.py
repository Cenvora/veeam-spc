from enum import Enum


class IdentityProviderAttributeMappingAttribute(str, Enum):
    ADDRESS = "Address"
    FIRSTNAME = "FirstName"
    LASTNAME = "LastName"
    NAME = "Name"
    PHONE = "Phone"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class Saml2ContactPersonConfigurationType(str, Enum):
    ADMINISTRATIVE = "Administrative"
    BILLING = "Billing"
    OTHER = "Other"
    SUPPORT = "Support"
    TECHNICAL = "Technical"

    def __str__(self) -> str:
        return str(self.value)

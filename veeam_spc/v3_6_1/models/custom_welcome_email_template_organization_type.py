from enum import Enum


class CustomWelcomeEmailTemplateOrganizationType(str, Enum):
    COMPANY = "Company"
    RESELLER = "Reseller"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class GetCustomWelcomeEmailTemplatesOrganizationType(str, Enum):
    COMPANY = "Company"
    RESELLER = "Reseller"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class PatchCustomWelcomeEmailTemplateOrganizationType(str, Enum):
    COMPANY = "Company"
    RESELLER = "Reseller"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

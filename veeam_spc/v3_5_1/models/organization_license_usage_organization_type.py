from enum import Enum


class OrganizationLicenseUsageOrganizationType(str, Enum):
    COMPANY = "Company"
    PROVIDER = "Provider"
    RESELLER = "Reseller"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

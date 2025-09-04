from enum import Enum


class OrganizationCurrentLicenseUsageOrganizationType(str, Enum):
    COMPANY = "Company"
    PROVIDER = "Provider"
    RESELLER = "Reseller"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

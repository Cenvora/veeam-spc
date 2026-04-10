from enum import Enum


class VdcVaultSubscriptionManagedOrganizationType(str, Enum):
    CLIENT = "Client"
    PROVIDER = "Provider"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

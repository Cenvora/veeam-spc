from enum import Enum


class VdcVaultSubscriptionType(str, Enum):
    AWS = "Aws"
    AZURE = "Azure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

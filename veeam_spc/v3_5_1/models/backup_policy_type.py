from enum import Enum


class BackupPolicyType(str, Enum):
    CLIENT = "Client"
    PREDEFINED = "Predefined"
    PROVIDER = "Provider"
    RESELLER = "Reseller"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

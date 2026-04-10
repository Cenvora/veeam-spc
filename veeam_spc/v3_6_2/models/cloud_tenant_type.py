from enum import Enum


class CloudTenantType(str, Enum):
    GENERAL = "General"
    UNKNOWN = "Unknown"
    VCD = "VCD"

    def __str__(self) -> str:
        return str(self.value)

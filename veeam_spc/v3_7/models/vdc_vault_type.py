from enum import Enum


class VdcVaultType(str, Enum):
    STANDARD = "Standard"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

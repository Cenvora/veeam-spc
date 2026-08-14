from enum import Enum


class VdcVaultPlatform(str, Enum):
    AWS = "Aws"
    AZURE = "Azure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

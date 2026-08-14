from enum import Enum


class VdcStorageVaultStatusReadonly(str, Enum):
    ACTIVE = "Active"
    DELETING = "Deleting"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ResellerStatus(str, Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

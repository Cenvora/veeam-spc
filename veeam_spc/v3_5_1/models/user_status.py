from enum import Enum


class UserStatus(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

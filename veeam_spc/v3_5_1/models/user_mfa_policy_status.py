from enum import Enum


class UserMfaPolicyStatus(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    ENABLEDBYINHERITANCE = "EnabledByInheritance"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

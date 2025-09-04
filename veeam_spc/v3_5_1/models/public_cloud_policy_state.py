from enum import Enum


class PublicCloudPolicyState(str, Enum):
    DISABLED = "Disabled"
    DISABLING = "Disabling"
    ENABLED = "Enabled"
    ENABLING = "Enabling"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

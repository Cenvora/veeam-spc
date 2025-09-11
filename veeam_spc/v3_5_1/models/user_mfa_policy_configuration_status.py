from enum import Enum


class UserMfaPolicyConfigurationStatus(str, Enum):
    CONFIGURED = "Configured"
    NOTCONFIGURED = "NotConfigured"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

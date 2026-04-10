from enum import Enum


class VdcVaultConfigurationStatus(str, Enum):
    CONFIGURED = "Configured"
    ERROR = "Error"
    NOTCONFIGURED = "NotConfigured"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

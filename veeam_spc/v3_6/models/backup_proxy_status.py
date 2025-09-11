from enum import Enum


class BackupProxyStatus(str, Enum):
    ERROR = "Error"
    HEALTHY = "Healthy"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

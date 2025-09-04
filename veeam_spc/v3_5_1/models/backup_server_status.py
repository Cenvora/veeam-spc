from enum import Enum


class BackupServerStatus(str, Enum):
    HEALTHY = "Healthy"
    INACCESSIBLE = "Inaccessible"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

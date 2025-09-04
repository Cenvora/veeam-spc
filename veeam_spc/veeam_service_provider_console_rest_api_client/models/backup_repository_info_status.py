from enum import Enum


class BackupRepositoryInfoStatus(str, Enum):
    ERROR = "Error"
    HEALTHY = "Healthy"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

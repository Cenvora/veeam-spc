from enum import Enum


class BackupServerCdpReplicationJobObjectStatus(str, Enum):
    FAILED = "Failed"
    INPROGRESS = "InProgress"
    PENDING = "Pending"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

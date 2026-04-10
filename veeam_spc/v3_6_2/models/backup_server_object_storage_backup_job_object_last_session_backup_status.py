from enum import Enum


class BackupServerObjectStorageBackupJobObjectLastSessionBackupStatus(str, Enum):
    FAILED = "Failed"
    RUNNING = "Running"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

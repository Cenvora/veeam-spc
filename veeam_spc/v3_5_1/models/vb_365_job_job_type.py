from enum import Enum


class Vb365JobJobType(str, Enum):
    BACKUPJOB = "BackupJob"
    COPYJOB = "CopyJob"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

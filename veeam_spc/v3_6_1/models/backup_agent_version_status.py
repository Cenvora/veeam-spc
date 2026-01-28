from enum import Enum


class BackupAgentVersionStatus(str, Enum):
    OUTOFDATE = "OutOfDate"
    UNKNOWN = "Unknown"
    UPTODATE = "UpToDate"

    def __str__(self) -> str:
        return str(self.value)

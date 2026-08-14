from enum import Enum


class BackupAgentStatus(str, Enum):
    ACTIVE = "Active"
    NOTRUNNING = "NotRunning"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

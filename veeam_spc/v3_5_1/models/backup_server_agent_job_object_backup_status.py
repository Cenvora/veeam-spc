from enum import Enum


class BackupServerAgentJobObjectBackupStatus(str, Enum):
    FAILED = "Failed"
    NONE = "None"
    RUNNING = "Running"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

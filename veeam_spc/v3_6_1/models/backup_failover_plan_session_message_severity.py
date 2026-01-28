from enum import Enum


class BackupFailoverPlanSessionMessageSeverity(str, Enum):
    FAILED = "Failed"
    NONE = "None"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

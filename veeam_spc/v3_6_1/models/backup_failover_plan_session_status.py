from enum import Enum


class BackupFailoverPlanSessionStatus(str, Enum):
    FAILED = "Failed"
    NONE = "None"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

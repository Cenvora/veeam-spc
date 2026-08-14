from enum import Enum


class BackupServerJobRetentionLimitType(str, Enum):
    DAYS = "Days"
    NONE = "None"
    RESTOREPOINTS = "RestorePoints"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupServerJobTargetType(str, Enum):
    CLOUD = "Cloud"
    LOCAL = "Local"
    NONE = "None"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

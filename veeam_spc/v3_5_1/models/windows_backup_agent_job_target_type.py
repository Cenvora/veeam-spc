from enum import Enum


class WindowsBackupAgentJobTargetType(str, Enum):
    CLOUD = "Cloud"
    LOCAL = "Local"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

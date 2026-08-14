from enum import Enum


class WindowsServerJobRetentionSettingsRetentionMode(str, Enum):
    DAYS = "Days"
    RESTOREPOINTS = "RestorePoints"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

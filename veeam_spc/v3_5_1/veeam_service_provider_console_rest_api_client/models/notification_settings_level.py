from enum import Enum


class NotificationSettingsLevel(str, Enum):
    ALL = "all"
    DISABLED = "disabled"
    SUMMARY = "summary"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

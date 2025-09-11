from enum import Enum


class VOneServerAlarmsSynchronizationStatus(str, Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"
    ERROR = "Error"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class LinuxActiveFullSettingsScheduleType(str, Enum):
    MONTHLY = "Monthly"
    NOTSCHEDULED = "NotScheduled"
    UNKNOWN = "Unknown"
    WEEKLY = "Weekly"

    def __str__(self) -> str:
        return str(self.value)

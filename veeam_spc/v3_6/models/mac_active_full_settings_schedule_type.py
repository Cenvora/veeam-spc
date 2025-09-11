from enum import Enum


class MacActiveFullSettingsScheduleType(str, Enum):
    MONTHLY = "Monthly"
    NOTSCHEDULED = "NotScheduled"
    UNKNOWN = "Unknown"
    WEEKLY = "Weekly"

    def __str__(self) -> str:
        return str(self.value)

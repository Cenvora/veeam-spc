from enum import Enum


class LinuxJobScheduleSettingsScheduleType(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    NOTSCHEDULED = "NotScheduled"
    PERIODICALLY = "Periodically"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

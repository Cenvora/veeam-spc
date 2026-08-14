from enum import Enum


class WindowsServerJobScheduleSettingsScheduleType(str, Enum):
    CONTINUOUSLY = "Continuously"
    DAILY = "Daily"
    MONTHLY = "Monthly"
    NOTSCHEDULED = "NotScheduled"
    PERIODICALLY = "Periodically"

    def __str__(self) -> str:
        return str(self.value)

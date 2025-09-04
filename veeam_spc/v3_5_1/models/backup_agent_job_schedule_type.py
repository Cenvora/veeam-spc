from enum import Enum


class BackupAgentJobScheduleType(str, Enum):
    CONTINUOUSLY = "Continuously"
    DAILY = "Daily"
    MONTHLY = "Monthly"
    NOTSCHEDULED = "NotScheduled"
    PERIODICALLY = "Periodically"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

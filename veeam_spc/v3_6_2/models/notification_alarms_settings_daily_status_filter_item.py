from enum import Enum


class NotificationAlarmsSettingsDailyStatusFilterItem(str, Enum):
    ACKNOWLEDGED = "Acknowledged"
    ERROR = "Error"
    INFO = "Info"
    RESOLVED = "Resolved"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

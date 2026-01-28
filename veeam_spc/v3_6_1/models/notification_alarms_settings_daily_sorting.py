from enum import Enum


class NotificationAlarmsSettingsDailySorting(str, Enum):
    BYALARMNAME = "ByAlarmName"
    BYOBJECTNAME = "ByObjectName"
    BYSTATUS = "ByStatus"
    BYTIME = "ByTime"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

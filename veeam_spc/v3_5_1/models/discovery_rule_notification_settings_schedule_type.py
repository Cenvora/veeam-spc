from enum import Enum


class DiscoveryRuleNotificationSettingsScheduleType(str, Enum):
    DAYS = "Days"
    WEEKS = "Weeks"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class MacMonthlyScheduleSettingsMonthlyMode(str, Enum):
    DAY = "Day"
    DAYOFWEEK = "DayOfWeek"
    LASTDAYOFMONTH = "LastDayOfMonth"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

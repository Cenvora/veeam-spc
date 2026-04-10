from enum import Enum


class WindowsMonthlyScheduleCalendarWithDaySettingsMonthlyMode(str, Enum):
    DAY = "Day"
    DAYOFWEEK = "DayOfWeek"
    LASTDAYOFMONTH = "LastDayOfMonth"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

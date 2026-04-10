from enum import Enum


class BackupServerJobScheduleOptionsMonthlyDayNumberInMonth(str, Enum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    ONDAY = "OnDay"
    SECOND = "Second"
    THIRD = "Third"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

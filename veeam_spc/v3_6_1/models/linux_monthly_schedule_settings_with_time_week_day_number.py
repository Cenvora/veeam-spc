from enum import Enum


class LinuxMonthlyScheduleSettingsWithTimeWeekDayNumber(str, Enum):
    EVERY = "Every"
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"

    def __str__(self) -> str:
        return str(self.value)

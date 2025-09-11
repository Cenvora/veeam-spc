from enum import Enum


class MacMonthlyScheduleSettingsWeekDayNumber(str, Enum):
    EVERY = "Every"
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"

    def __str__(self) -> str:
        return str(self.value)

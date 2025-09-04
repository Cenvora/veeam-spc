from enum import Enum


class WindowsDailyScheduleSettingsDailyMode(str, Enum):
    EVERYDAY = "Everyday"
    SPECIFICDAYS = "SpecificDays"
    WEEKDAYS = "WeekDays"

    def __str__(self) -> str:
        return str(self.value)

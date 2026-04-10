from enum import Enum


class LinuxDailyScheduleSettingsDailyMode(str, Enum):
    EVERYDAY = "Everyday"
    SPECIFICDAYS = "SpecificDays"
    WEEKDAYS = "WeekDays"

    def __str__(self) -> str:
        return str(self.value)

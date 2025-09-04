from enum import Enum


class Vb365CopyJobSchedulePolicyDailyType(str, Enum):
    EVERYDAY = "Everyday"
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    UNKNOWN = "Unknown"
    WEDNESDAY = "Wednesday"
    WEEKENDS = "Weekends"
    WORKDAYS = "Workdays"

    def __str__(self) -> str:
        return str(self.value)

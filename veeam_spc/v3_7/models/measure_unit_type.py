from enum import Enum


class MeasureUnitType(str, Enum):
    BYTES = "Bytes"
    DAYS = "Days"
    GB = "GB"
    HOURS = "Hours"
    KB = "KB"
    MB = "MB"
    MINUTES = "Minutes"
    MONTHS = "Months"
    NONE = "None"
    PB = "PB"
    SECONDS = "Seconds"
    TB = "TB"
    UNITS = "Units"
    UNKNOWN = "Unknown"
    WEEKS = "Weeks"

    def __str__(self) -> str:
        return str(self.value)

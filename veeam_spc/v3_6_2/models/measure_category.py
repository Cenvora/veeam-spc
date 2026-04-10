from enum import Enum


class MeasureCategory(str, Enum):
    NONE = "None"
    SIZE = "Size"
    TIME = "Time"
    UNITS = "Units"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

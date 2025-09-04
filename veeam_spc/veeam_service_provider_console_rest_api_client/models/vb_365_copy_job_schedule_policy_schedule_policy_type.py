from enum import Enum


class Vb365CopyJobSchedulePolicySchedulePolicyType(str, Enum):
    DAILYATTIME = "DailyAtTime"
    IMMEDIATE = "Immediate"
    PERIODICALLY = "Periodically"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class Vb365CopyJobSchedulePolicyPeriodicallyEvery(str, Enum):
    HOURS1 = "Hours1"
    HOURS12 = "Hours12"
    HOURS2 = "Hours2"
    HOURS4 = "Hours4"
    HOURS8 = "Hours8"
    MINUTES10 = "Minutes10"
    MINUTES15 = "Minutes15"
    MINUTES30 = "Minutes30"
    MINUTES5 = "Minutes5"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

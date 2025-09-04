from enum import Enum


class CompanySiteResourceThrottlingUnit(str, Enum):
    KBYTEPERSEC = "KbytePerSec"
    MBITPERSEC = "MbitPerSec"
    MBYTEPERSEC = "MbytePerSec"

    def __str__(self) -> str:
        return str(self.value)

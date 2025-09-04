from enum import Enum


class ResellerQuotaThrottlingUnit(str, Enum):
    KBYTEPERSEC = "KbytePerSec"
    MBITPERSEC = "MbitPerSec"
    MBYTEPERSEC = "MbytePerSec"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupServerConsumptionLimitKindNullable(str, Enum):
    PB = "PB"
    TB = "TB"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

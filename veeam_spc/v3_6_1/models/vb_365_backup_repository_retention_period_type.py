from enum import Enum


class Vb365BackupRepositoryRetentionPeriodType(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    UNKNOWN = "Unknown"
    YEARLY = "Yearly"

    def __str__(self) -> str:
        return str(self.value)

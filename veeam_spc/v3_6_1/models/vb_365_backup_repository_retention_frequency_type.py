from enum import Enum


class Vb365BackupRepositoryRetentionFrequencyType(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

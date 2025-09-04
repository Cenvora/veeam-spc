from enum import Enum


class Vb365BackupJobSchedulePolicySchedulePolicyType(str, Enum):
    DAILY = "Daily"
    MANUALONLY = "ManualOnly"
    PERIODICALLY = "Periodically"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

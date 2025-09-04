from enum import Enum


class BackupServerObjectStorageBackupJobRetentionUnit(str, Enum):
    DAYS = "Days"
    HOURS = "Hours"
    MINUTES = "Minutes"
    MONTHS = "Months"
    YEARS = "Years"

    def __str__(self) -> str:
        return str(self.value)

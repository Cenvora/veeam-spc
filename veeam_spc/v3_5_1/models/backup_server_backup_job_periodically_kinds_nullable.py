from enum import Enum


class BackupServerBackupJobPeriodicallyKindsNullable(str, Enum):
    DAYS = "Days"
    HOURS = "Hours"
    MINUTES = "Minutes"
    SECONDS = "Seconds"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupServerBackupJobDailyKinds(str, Enum):
    EVERYDAY = "Everyday"
    SELECTEDDAYS = "SelectedDays"
    WEEKDAYS = "WeekDays"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupServerBackupJobDayNumberInMonthNullable(str, Enum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    ONDAY = "OnDay"
    SECOND = "Second"
    THIRD = "Third"

    def __str__(self) -> str:
        return str(self.value)

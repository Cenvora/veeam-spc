from enum import Enum


class MacGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth(str, Enum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"

    def __str__(self) -> str:
        return str(self.value)

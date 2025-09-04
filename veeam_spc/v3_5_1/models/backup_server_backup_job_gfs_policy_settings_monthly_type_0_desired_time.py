from enum import Enum


class BackupServerBackupJobGFSPolicySettingsMonthlyType0DesiredTime(str, Enum):
    FIFTH = "Fifth"
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"

    def __str__(self) -> str:
        return str(self.value)

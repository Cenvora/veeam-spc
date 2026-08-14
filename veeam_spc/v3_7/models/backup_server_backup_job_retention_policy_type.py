from enum import Enum


class BackupServerBackupJobRetentionPolicyType(str, Enum):
    DAYS = "Days"
    RESTOREPOINTS = "RestorePoints"

    def __str__(self) -> str:
        return str(self.value)

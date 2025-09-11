from enum import Enum


class BackupServerBackupJobRetainLogBackupsType(str, Enum):
    KEEPONLYDAYS = "keepOnlyDays"
    UNTILBACKUPDELETED = "untilBackupDeleted"

    def __str__(self) -> str:
        return str(self.value)

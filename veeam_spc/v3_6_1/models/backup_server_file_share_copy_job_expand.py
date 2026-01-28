from enum import Enum


class BackupServerFileShareCopyJobExpand(str, Enum):
    BACKUPSERVERJOB = "BackupServerJob"

    def __str__(self) -> str:
        return str(self.value)

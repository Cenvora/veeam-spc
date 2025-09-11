from enum import Enum


class BackupServerBackupVmJobExpand(str, Enum):
    BACKUPSERVERJOB = "BackupServerJob"

    def __str__(self) -> str:
        return str(self.value)

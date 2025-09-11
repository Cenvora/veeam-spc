from enum import Enum


class BackupServerReplicationVmJobExpand(str, Enum):
    BACKUPSERVERJOB = "BackupServerJob"

    def __str__(self) -> str:
        return str(self.value)

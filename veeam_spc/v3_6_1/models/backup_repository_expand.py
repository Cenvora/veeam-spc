from enum import Enum


class BackupRepositoryExpand(str, Enum):
    BACKUPREPOSITORYINFO = "BackupRepositoryInfo"

    def __str__(self) -> str:
        return str(self.value)

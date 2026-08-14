from enum import Enum


class BackupServerWinLocalRepositoryExpand(str, Enum):
    BACKUPREPOSITORY = "BackupRepository"

    def __str__(self) -> str:
        return str(self.value)

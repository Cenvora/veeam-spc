from enum import Enum


class BackupServerVeeamVaultRepositoryExpand(str, Enum):
    BACKUPREPOSITORY = "BackupRepository"

    def __str__(self) -> str:
        return str(self.value)

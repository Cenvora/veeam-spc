from enum import Enum


class BackupServerBackupJobBackupOracleLogsSettings(str, Enum):
    DELETEEXPIREDGBS = "deleteExpiredGBs"
    DELETEEXPIREDHOURS = "deleteExpiredHours"
    PRESERVE = "preserve"

    def __str__(self) -> str:
        return str(self.value)

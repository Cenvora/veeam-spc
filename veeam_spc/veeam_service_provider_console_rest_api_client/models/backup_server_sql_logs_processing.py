from enum import Enum


class BackupServerSQLLogsProcessing(str, Enum):
    BACKUP = "backup"
    NEVERTRUNCATE = "neverTruncate"
    PRESERVE = "preserve"
    TRUNCATE = "truncate"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupServerTransactionLogsSettings(str, Enum):
    COPYONLY = "copyOnly"
    PROCESS = "process"

    def __str__(self) -> str:
        return str(self.value)

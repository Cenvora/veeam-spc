from enum import Enum


class ProtectedComputerManagedByBackupServerBackupJobKind(str, Enum):
    BACKUP = "Backup"
    COPY = "Copy"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

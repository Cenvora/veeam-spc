from enum import Enum


class BackupJobOperationModeReadonly(str, Enum):
    SERVER = "Server"
    UNKNOWN = "Unknown"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ProtectedComputerManagedByBackupServerOperationMode(str, Enum):
    SERVER = "Server"
    UNKNOWN = "Unknown"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)

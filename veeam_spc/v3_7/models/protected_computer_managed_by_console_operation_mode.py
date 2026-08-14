from enum import Enum


class ProtectedComputerManagedByConsoleOperationMode(str, Enum):
    SERVER = "Server"
    UNKNOWN = "Unknown"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)

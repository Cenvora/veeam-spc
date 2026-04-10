from enum import Enum


class ProtectedComputerManagedByConsoleJobTargetType(str, Enum):
    CLOUD = "Cloud"
    LOCAL = "Local"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

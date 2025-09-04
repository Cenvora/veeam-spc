from enum import Enum


class ProtectedVirtualMachineBackupTargetType(str, Enum):
    CLOUD = "Cloud"
    LOCAL = "Local"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupAgentOperationMode(str, Enum):
    SERVER = "Server"
    UNKNOWN = "Unknown"
    UNLICENSED = "UnLicensed"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)

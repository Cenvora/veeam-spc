from enum import Enum


class BackupServerAgentLicense(str, Enum):
    LIMITED = "Limited"
    SERVER = "Server"
    UNKNOWN = "Unknown"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)

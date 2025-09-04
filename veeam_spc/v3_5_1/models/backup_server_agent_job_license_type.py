from enum import Enum


class BackupServerAgentJobLicenseType(str, Enum):
    LIMITED = "Limited"
    SERVER = "Server"
    UNKNOWN = "Unknown"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)

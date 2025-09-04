from enum import Enum


class BackupServerBackupServerRoleType(str, Enum):
    CLIENT = "Client"
    CLOUDCONNECT = "CloudConnect"
    HOSTED = "Hosted"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

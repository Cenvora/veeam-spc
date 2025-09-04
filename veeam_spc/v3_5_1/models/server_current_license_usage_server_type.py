from enum import Enum


class ServerCurrentLicenseUsageServerType(str, Enum):
    BACKUPANDREPLICATION = "BackupAndReplication"
    CLOUDCONNECT = "CloudConnect"
    UNKNOWN = "Unknown"
    VB365 = "VB365"
    VONE = "VONE"
    VSPC = "VSPC"

    def __str__(self) -> str:
        return str(self.value)

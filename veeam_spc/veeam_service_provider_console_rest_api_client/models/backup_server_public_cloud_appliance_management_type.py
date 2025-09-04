from enum import Enum


class BackupServerPublicCloudApplianceManagementType(str, Enum):
    BYBACKUPSERVER = "ByBackupServer"
    BYCONSOLE = "ByConsole"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

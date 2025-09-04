from enum import Enum


class BackupAgentInstallationType(str, Enum):
    BROKEN = "Broken"
    FULL = "Full"
    INSTALLING = "Installing"
    RESTRICTED = "Restricted"
    UNINSTALLING = "Uninstalling"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

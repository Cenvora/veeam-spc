from enum import Enum


class DiscoveredComputerBackupAgentInstallationStatus(str, Enum):
    INSTALLED = "Installed"
    NOTINSTALLED = "NotInstalled"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

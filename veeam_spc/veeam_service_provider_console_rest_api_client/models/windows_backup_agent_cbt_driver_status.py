from enum import Enum


class WindowsBackupAgentCbtDriverStatus(str, Enum):
    ERROR = "Error"
    INSTALLED = "Installed"
    INSTALLING = "Installing"
    NOTINSTALLED = "NotInstalled"
    UNINSTALLING = "Uninstalling"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

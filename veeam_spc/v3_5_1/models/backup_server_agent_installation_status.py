from enum import Enum


class BackupServerAgentInstallationStatus(str, Enum):
    FAILED = "Failed"
    INSTALLED = "Installed"
    NOTINITIALIZED = "NotInitialized"
    NOTINSTALLED = "NotInstalled"
    REBOOTREQUIRED = "RebootRequired"
    UNKNOWN = "Unknown"
    UNSUPPORTEDOS = "UnsupportedOs"

    def __str__(self) -> str:
        return str(self.value)

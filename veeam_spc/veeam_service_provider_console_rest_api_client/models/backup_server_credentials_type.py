from enum import Enum


class BackupServerCredentialsType(str, Enum):
    LINUX = "Linux"
    STANDARD = "Standard"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

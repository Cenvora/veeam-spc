from enum import Enum


class BackupServerMountServerSettingsType(str, Enum):
    BOTH = "Both"
    LINUX = "Linux"
    UNKNOWN = "Unknown"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)

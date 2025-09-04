from enum import Enum


class LinuxBackupSourceBackupMode(str, Enum):
    ENTIRECOMPUTER = "EntireComputer"
    FILESFOLDERS = "FilesFolders"
    UNKNOWN = "Unknown"
    VOLUME = "Volume"

    def __str__(self) -> str:
        return str(self.value)

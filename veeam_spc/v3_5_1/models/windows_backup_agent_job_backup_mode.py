from enum import Enum


class WindowsBackupAgentJobBackupMode(str, Enum):
    ENTIRECOMPUTER = "EntireComputer"
    FILE = "File"
    UNKNOWN = "Unknown"
    VOLUME = "Volume"

    def __str__(self) -> str:
        return str(self.value)

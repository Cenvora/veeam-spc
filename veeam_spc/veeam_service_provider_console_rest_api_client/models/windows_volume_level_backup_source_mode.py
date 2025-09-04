from enum import Enum


class WindowsVolumeLevelBackupSourceMode(str, Enum):
    EXCLUSIONMODE = "ExclusionMode"
    INCLUSIONMODE = "InclusionMode"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

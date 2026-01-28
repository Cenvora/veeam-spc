from enum import Enum


class BackupServerFileTapeJobObjectSourceType(str, Enum):
    DIRECTORY = "Directory"
    FILE = "File"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupAgentGuiMode(str, Enum):
    FULL = "Full"
    READONLY = "ReadOnly"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

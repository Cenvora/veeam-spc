from enum import Enum


class BackupPolicyAccessMode(str, Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"

    def __str__(self) -> str:
        return str(self.value)

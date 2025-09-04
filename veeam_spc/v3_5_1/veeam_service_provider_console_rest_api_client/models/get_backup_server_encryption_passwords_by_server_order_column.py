from enum import Enum


class GetBackupServerEncryptionPasswordsByServerOrderColumn(str, Enum):
    HINT = "Hint"
    MODIFICATIONTIME = "ModificationTime"

    def __str__(self) -> str:
        return str(self.value)

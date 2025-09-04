from enum import Enum


class BackupServerEncryptionTypeNullable(str, Enum):
    BYKMS = "ByKms"
    BYUSERPASSWORD = "ByUserPassword"

    def __str__(self) -> str:
        return str(self.value)

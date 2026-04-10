from enum import Enum


class GetBackupServerCredentialsByServerOrderColumn(str, Enum):
    DESCRIPTION = "Description"
    USERNAME = "Username"

    def __str__(self) -> str:
        return str(self.value)

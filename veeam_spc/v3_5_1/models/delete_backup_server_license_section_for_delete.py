from enum import Enum


class DeleteBackupServerLicenseSectionForDelete(str, Enum):
    ALL = "All"
    INSTANCE = "Instance"
    SOCKET = "Socket"

    def __str__(self) -> str:
        return str(self.value)

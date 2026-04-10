from enum import Enum


class BackupServerRepositoryConnectionType(str, Enum):
    DIRECT = "Direct"
    SELECTEDGATEWAY = "SelectedGateway"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

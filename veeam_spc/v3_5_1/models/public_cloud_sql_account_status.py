from enum import Enum


class PublicCloudSqlAccountStatus(str, Enum):
    AVAILABLE = "Available"
    REMOVING = "Removing"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

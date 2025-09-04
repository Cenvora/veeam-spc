from enum import Enum


class ProtectedCloudDatabasePlatform(str, Enum):
    AMAZON = "Amazon"
    AZURE = "Azure"
    GOOGLE = "Google"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

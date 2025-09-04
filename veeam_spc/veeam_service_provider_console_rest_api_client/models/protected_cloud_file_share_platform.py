from enum import Enum


class ProtectedCloudFileSharePlatform(str, Enum):
    AMAZON = "Amazon"
    AZURE = "Azure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

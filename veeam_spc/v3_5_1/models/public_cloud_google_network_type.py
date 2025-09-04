from enum import Enum


class PublicCloudGoogleNetworkType(str, Enum):
    SHARED = "Shared"
    STANDALONE = "Standalone"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

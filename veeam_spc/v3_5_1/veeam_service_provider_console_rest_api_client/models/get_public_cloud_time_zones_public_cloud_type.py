from enum import Enum


class GetPublicCloudTimeZonesPublicCloudType(str, Enum):
    AWS = "AWS"
    AZURE = "Azure"
    GOOGLE = "Google"

    def __str__(self) -> str:
        return str(self.value)

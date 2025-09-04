from enum import Enum


class BackupServerPublicCloudAppliancePlatform(str, Enum):
    AMAZON = "Amazon"
    AZURE = "Azure"
    GOOGLE = "Google"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

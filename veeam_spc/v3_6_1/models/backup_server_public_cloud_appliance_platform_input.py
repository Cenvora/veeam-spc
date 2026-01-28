from enum import Enum


class BackupServerPublicCloudAppliancePlatformInput(str, Enum):
    AMAZON = "Amazon"
    AZURE = "Azure"
    GOOGLE = "Google"

    def __str__(self) -> str:
        return str(self.value)

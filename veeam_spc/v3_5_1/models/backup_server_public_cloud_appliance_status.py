from enum import Enum


class BackupServerPublicCloudApplianceStatus(str, Enum):
    DELETING = "Deleting"
    HEALTHY = "Healthy"
    REMOVING = "Removing"
    UNAVAILABLE = "Unavailable"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

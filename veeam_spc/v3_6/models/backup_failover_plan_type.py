from enum import Enum


class BackupFailoverPlanType(str, Enum):
    CLOUD = "Cloud"
    LOCAL = "Local"
    TENANT = "Tenant"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

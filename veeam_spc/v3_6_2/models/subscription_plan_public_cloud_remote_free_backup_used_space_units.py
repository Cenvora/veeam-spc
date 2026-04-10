from enum import Enum


class SubscriptionPlanPublicCloudRemoteFreeBackupUsedSpaceUnits(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

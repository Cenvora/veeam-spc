from enum import Enum


class SubscriptionPlanFileShareBackupFreeFileShareRemoteBackupUsedSpaceUnits(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

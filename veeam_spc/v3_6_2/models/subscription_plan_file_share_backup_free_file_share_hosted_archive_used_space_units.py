from enum import Enum


class SubscriptionPlanFileShareBackupFreeFileShareHostedArchiveUsedSpaceUnits(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

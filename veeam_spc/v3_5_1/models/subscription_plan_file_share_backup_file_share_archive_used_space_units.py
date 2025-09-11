from enum import Enum


class SubscriptionPlanFileShareBackupFileShareArchiveUsedSpaceUnits(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

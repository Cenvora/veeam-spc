from enum import Enum


class SubscriptionPlanManagedBackupFreeBackupUsedSpaceUnits(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

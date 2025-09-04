from enum import Enum


class SubscriptionPlanVb365FreeArchiveStorageUsedSpaceUnits(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

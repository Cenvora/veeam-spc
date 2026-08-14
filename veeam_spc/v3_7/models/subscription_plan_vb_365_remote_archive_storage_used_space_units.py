from enum import Enum


class SubscriptionPlanVb365RemoteArchiveStorageUsedSpaceUnits(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

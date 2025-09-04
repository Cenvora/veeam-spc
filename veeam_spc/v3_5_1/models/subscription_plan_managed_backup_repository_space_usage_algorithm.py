from enum import Enum


class SubscriptionPlanManagedBackupRepositorySpaceUsageAlgorithm(str, Enum):
    ALLOCATED = "Allocated"
    CONSUMED = "Consumed"
    GRANULAR = "Granular"

    def __str__(self) -> str:
        return str(self.value)

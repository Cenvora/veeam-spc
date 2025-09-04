from enum import Enum


class SubscriptionPlanVb365RepositorySpaceUsageAlgorithm(str, Enum):
    ALLOCATED = "Allocated"
    CONSUMED = "Consumed"
    GRANULAR = "Granular"

    def __str__(self) -> str:
        return str(self.value)

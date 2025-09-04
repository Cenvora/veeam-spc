from enum import Enum


class SubscriptionPlanCloudReplicationComputeResourcesUnits(str, Enum):
    DAYS = "Days"
    HOURS = "Hours"
    MINUTES = "Minutes"
    MONTHS = "Months"
    WEEKS = "Weeks"

    def __str__(self) -> str:
        return str(self.value)

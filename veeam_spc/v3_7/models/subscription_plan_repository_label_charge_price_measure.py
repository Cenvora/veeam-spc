from enum import Enum


class SubscriptionPlanRepositoryLabelChargePriceMeasure(str, Enum):
    GB = "GB"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)

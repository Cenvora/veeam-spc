from enum import Enum


class SubscriptionPlanType(str, Enum):
    PREDEFINED = "Predefined"
    PROVIDER = "Provider"
    RESELLER = "Reseller"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

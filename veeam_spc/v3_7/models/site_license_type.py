from enum import Enum


class SiteLicenseType(str, Enum):
    COMMUNITY = "Community"
    EVALUATION = "Evaluation"
    NFR = "NFR"
    NOTINSTALLED = "NotInstalled"
    PERPETUAL = "Perpetual"
    RENTAL = "Rental"
    SUBSCRIPTION = "Subscription"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

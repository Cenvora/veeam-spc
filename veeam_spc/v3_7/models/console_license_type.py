from enum import Enum


class ConsoleLicenseType(str, Enum):
    COMMUNITY = "Community"
    EVALUATION = "Evaluation"
    FULL = "Full"
    NFR = "NFR"
    NOTINSTALLED = "NotInstalled"
    PERPETUAL = "Perpetual"
    PROMO = "Promo"
    RENTAL = "Rental"
    SUBSCRIPTION = "Subscription"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

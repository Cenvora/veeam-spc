from enum import Enum


class SubscriptionPlanTaxType(str, Enum):
    GST = "GST"
    SALESTAX = "SalesTax"
    UNKNOWN = "Unknown"
    VAT = "VAT"

    def __str__(self) -> str:
        return str(self.value)

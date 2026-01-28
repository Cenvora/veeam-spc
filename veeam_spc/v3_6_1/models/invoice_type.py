from enum import Enum


class InvoiceType(str, Enum):
    INVOICE = "Invoice"
    QUOTAUSAGE = "QuotaUsage"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class InvoiceStatus(str, Enum):
    OVERDUE = "Overdue"
    PAID = "Paid"
    UNKNOWN = "Unknown"
    UNPAID = "Unpaid"

    def __str__(self) -> str:
        return str(self.value)

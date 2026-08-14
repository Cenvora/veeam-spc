from enum import Enum


class ChangeInvoicePaidStateStatus(str, Enum):
    PAID = "Paid"
    UNPAID = "Unpaid"

    def __str__(self) -> str:
        return str(self.value)

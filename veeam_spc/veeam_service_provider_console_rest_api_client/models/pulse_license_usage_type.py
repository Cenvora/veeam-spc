from enum import Enum


class PulseLicenseUsageType(str, Enum):
    INTERNALUSE = "InternalUse"
    MULTICUSTOMERUSE = "MultiCustomerUse"
    SINGLECUSTOMERUSE = "SingleCustomerUse"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

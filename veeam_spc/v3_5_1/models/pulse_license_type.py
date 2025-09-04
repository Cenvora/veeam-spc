from enum import Enum


class PulseLicenseType(str, Enum):
    INTERNAL = "Internal"
    REMOVED_1 = "REMOVED_1"
    RENTAL = "Rental"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

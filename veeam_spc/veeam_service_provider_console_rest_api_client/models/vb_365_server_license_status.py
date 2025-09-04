from enum import Enum


class Vb365ServerLicenseStatus(str, Enum):
    ERROR = "Error"
    EXPIRED = "Expired"
    UNKNOWN = "Unknown"
    UNLICENSED = "Unlicensed"
    VALID = "Valid"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ConsoleLicenseStatus(str, Enum):
    ERROR = "Error"
    EXPIRED = "Expired"
    UNKNOWN = "Unknown"
    VALID = "Valid"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

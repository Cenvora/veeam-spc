from enum import Enum


class ConsoleLicenseLastUpdateStatus(str, Enum):
    ERROR = "Error"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

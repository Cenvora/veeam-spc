from enum import Enum


class BackupServerLicenseStatus(str, Enum):
    ERROR = "Error"
    EXPIRED = "Expired"
    UNKNOWN = "Unknown"
    UNLICENSED = "Unlicensed"
    VALID = "Valid"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

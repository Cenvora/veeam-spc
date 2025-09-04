from enum import Enum


class BackupServerAgentLicenseStatus(str, Enum):
    LICENSED = "Licensed"
    LICENSEREVOKED = "LicenseRevoked"
    UNKNOWN = "Unknown"
    UNLICENSED = "Unlicensed"

    def __str__(self) -> str:
        return str(self.value)

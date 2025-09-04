from enum import Enum


class BackupServerLicenseUnitType(str, Enum):
    INSTANCES = "Instances"
    POINTS = "Points"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class CurrentLicenseUsageWorkloadUnitType(str, Enum):
    INSTANCES = "Instances"
    POINTS = "Points"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

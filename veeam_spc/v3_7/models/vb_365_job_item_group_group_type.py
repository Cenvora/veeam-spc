from enum import Enum


class Vb365JobItemGroupGroupType(str, Enum):
    DISTRIBUTION = "Distribution"
    DYNAMICDISTRIBUTION = "DynamicDistribution"
    OFFICE365 = "Office365"
    SECURITY = "Security"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

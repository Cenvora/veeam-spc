from enum import Enum


class Vb365JobItemUserLocationType(str, Enum):
    CLOUD = "Cloud"
    HYBRID = "Hybrid"
    ONPREMISES = "OnPremises"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

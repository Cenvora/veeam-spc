from enum import Enum


class Vb365OrganizationBaseType(str, Enum):
    HYBRID = "Hybrid"
    MICROSOFT365 = "Microsoft365"
    ONPREMISES = "OnPremises"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

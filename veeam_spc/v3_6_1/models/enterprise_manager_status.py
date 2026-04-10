from enum import Enum


class EnterpriseManagerStatus(str, Enum):
    HEALTHY = "Healthy"
    INACCESSIBLE = "Inaccessible"
    OUTOFDATE = "OutofDate"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

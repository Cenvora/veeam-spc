from enum import Enum


class Vb365ServerStatus(str, Enum):
    HEALTHY = "Healthy"
    INACCESSIBLE = "Inaccessible"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

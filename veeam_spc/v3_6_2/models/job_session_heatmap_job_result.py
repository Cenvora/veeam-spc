from enum import Enum


class JobSessionHeatmapJobResult(str, Enum):
    FAILED = "Failed"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

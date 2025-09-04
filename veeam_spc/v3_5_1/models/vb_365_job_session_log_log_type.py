from enum import Enum


class Vb365JobSessionLogLogType(str, Enum):
    ERROR = "Error"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

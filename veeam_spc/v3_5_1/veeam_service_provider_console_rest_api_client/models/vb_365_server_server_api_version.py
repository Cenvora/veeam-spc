from enum import Enum


class Vb365ServerServerApiVersion(str, Enum):
    UNKNOWN = "Unknown"
    V6 = "V6"
    V7 = "V7"
    V8 = "V8"

    def __str__(self) -> str:
        return str(self.value)

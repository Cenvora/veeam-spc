from enum import Enum


class Vb365JobItemUserUserType(str, Enum):
    PUBLIC = "Public"
    SHARED = "Shared"
    UNKNOWN = "Unknown"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)

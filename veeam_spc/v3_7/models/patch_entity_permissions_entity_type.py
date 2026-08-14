from enum import Enum


class PatchEntityPermissionsEntityType(str, Enum):
    COMPANY = "Company"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class GetEntityPermissionsEntityType(str, Enum):
    COMPANY = "Company"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

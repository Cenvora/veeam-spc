from enum import Enum


class OrgContainerType(str, Enum):
    CUSTOM = "Custom"
    DEFAULTCOMPANIES = "DefaultCompanies"
    DEFAULTRESELLERS = "DefaultResellers"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

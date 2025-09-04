from enum import Enum


class OrganizationLocationType(str, Enum):
    CUSTOM = "Custom"
    DEFAULT = "Default"
    HOSTED = "Hosted"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

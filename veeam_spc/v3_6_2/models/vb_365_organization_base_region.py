from enum import Enum


class Vb365OrganizationBaseRegion(str, Enum):
    CHINA = "China"
    DEFAULT = "Default"
    GERMANY = "Germany"
    UNKNOWN = "Unknown"
    USDEFENCE = "USDefence"
    USGOVERNMENT = "USGovernment"

    def __str__(self) -> str:
        return str(self.value)

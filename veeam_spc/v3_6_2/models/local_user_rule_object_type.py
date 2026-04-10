from enum import Enum


class LocalUserRuleObjectType(str, Enum):
    ALL = "all"
    CLOUDCONNECT = "cloudConnect"
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)

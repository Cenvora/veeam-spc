from enum import Enum


class DiscoveryRuleSystemType(str, Enum):
    LINUX = "Linux"
    UNKNOWN = "Unknown"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)

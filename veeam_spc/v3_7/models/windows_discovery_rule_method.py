from enum import Enum


class WindowsDiscoveryRuleMethod(str, Enum):
    AD = "AD"
    MANUAL = "Manual"
    NETWORKBASED = "NetworkBased"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

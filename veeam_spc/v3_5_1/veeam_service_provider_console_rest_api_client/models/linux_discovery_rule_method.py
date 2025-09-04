from enum import Enum


class LinuxDiscoveryRuleMethod(str, Enum):
    MANUAL = "Manual"
    NETWORKBASED = "NetworkBased"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

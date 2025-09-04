from enum import Enum


class MachinesNetworkTrustOptionsTrustOption(str, Enum):
    ALL = "All"
    KNOWNLIST = "KnownList"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

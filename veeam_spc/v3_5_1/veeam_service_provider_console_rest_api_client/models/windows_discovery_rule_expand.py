from enum import Enum


class WindowsDiscoveryRuleExpand(str, Enum):
    DISCOVERYRULE = "DiscoveryRule"

    def __str__(self) -> str:
        return str(self.value)

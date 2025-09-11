from enum import Enum


class WindowsCustomDiscoveryRuleExpand(str, Enum):
    DISCOVERYRULE = "DiscoveryRule"
    WINDOWSDISCOVERYRULE = "WindowsDiscoveryRule"

    def __str__(self) -> str:
        return str(self.value)

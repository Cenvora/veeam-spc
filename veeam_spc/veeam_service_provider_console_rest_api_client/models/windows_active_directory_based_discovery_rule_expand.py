from enum import Enum


class WindowsActiveDirectoryBasedDiscoveryRuleExpand(str, Enum):
    DISCOVERYRULE = "DiscoveryRule"
    WINDOWSDISCOVERYRULE = "WindowsDiscoveryRule"

    def __str__(self) -> str:
        return str(self.value)

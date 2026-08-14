from enum import Enum


class LinuxCustomDiscoveryRuleExpand(str, Enum):
    DISCOVERYRULE = "DiscoveryRule"
    LINUXDISCOVERYRULE = "LinuxDiscoveryRule"

    def __str__(self) -> str:
        return str(self.value)

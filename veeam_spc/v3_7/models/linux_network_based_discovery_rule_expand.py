from enum import Enum


class LinuxNetworkBasedDiscoveryRuleExpand(str, Enum):
    DISCOVERYRULE = "DiscoveryRule"
    LINUXDISCOVERYRULE = "LinuxDiscoveryRule"

    def __str__(self) -> str:
        return str(self.value)

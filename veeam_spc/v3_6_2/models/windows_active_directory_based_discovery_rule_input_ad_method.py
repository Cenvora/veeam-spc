from enum import Enum


class WindowsActiveDirectoryBasedDiscoveryRuleInputAdMethod(str, Enum):
    CUSTOM = "Custom"
    QUERY = "Query"
    SEARCH = "Search"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

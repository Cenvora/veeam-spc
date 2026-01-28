from enum import Enum


class SiteLicenseSectionTypesItem(str, Enum):
    ALL = "All"
    INSTANCE = "Instance"
    SOCKET = "Socket"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

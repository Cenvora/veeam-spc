from enum import Enum


class GetMountServersTypeFilter(str, Enum):
    LINUX = "Linux"
    UNKNOWN = "Unknown"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)

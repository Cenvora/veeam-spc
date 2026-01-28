from enum import Enum


class DiscoveredComputerStatus(str, Enum):
    ERROR = "Error"
    OFFLINE = "Offline"
    ONLINE = "Online"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

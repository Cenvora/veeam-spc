from enum import Enum


class ManagementAgentConnectionStatus(str, Enum):
    INACCESSIBLE = "Inaccessible"
    ONLINE = "Online"
    REJECTED = "Rejected"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

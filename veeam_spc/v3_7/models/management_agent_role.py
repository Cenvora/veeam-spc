from enum import Enum


class ManagementAgentRole(str, Enum):
    CLIENT = "Client"
    MASTER = "Master"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

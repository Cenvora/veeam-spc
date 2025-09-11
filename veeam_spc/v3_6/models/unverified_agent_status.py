from enum import Enum


class UnverifiedAgentStatus(str, Enum):
    ACCEPTED = "Accepted"
    APPLYING = "Applying"
    INACCESSIBLE = "Inaccessible"
    PENDING = "Pending"
    REJECTED = "Rejected"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

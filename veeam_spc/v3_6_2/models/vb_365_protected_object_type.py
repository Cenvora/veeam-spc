from enum import Enum


class Vb365ProtectedObjectType(str, Enum):
    GROUP = "Group"
    SITE = "Site"
    TEAMS = "Teams"
    UNKNOWN = "Unknown"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)

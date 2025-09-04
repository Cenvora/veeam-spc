from enum import Enum


class BackupAgentPlatform(str, Enum):
    CLOUD = "Cloud"
    PHYSICAL = "Physical"
    UNKNOWN = "Unknown"
    VIRTUAL = "Virtual"

    def __str__(self) -> str:
        return str(self.value)

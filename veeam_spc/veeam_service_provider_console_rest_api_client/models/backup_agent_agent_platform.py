from enum import Enum


class BackupAgentAgentPlatform(str, Enum):
    LINUX = "Linux"
    MAC = "Mac"
    UNKNOWN = "Unknown"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)

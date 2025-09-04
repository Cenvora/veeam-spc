from enum import Enum


class BackupPolicySystemType(str, Enum):
    LINUX = "Linux"
    MAC = "Mac"
    UNKNOWN = "Unknown"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)

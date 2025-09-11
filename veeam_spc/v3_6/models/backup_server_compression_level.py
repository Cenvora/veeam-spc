from enum import Enum


class BackupServerCompressionLevel(str, Enum):
    DEDUPLICATIONFRIENDLY = "DeduplicationFriendly"
    EXTREME = "Extreme"
    HIGH = "High"
    NONE = "None"
    OPTIMAL = "Optimal"

    def __str__(self) -> str:
        return str(self.value)

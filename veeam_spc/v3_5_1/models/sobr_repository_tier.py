from enum import Enum


class SobrRepositoryTier(str, Enum):
    ARCHIVE = "Archive"
    CAPACITY = "Capacity"
    NONE = "None"
    PERFORMANCE = "Performance"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

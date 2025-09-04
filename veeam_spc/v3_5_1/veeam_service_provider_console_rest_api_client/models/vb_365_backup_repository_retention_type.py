from enum import Enum


class Vb365BackupRepositoryRetentionType(str, Enum):
    ITEMLEVEL = "ItemLevel"
    SNAPSHOTBASED = "SnapshotBased"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

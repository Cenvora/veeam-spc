from enum import Enum


class MacBackupStorageCompressionLevel(str, Enum):
    DEDUPE = "Dedupe"
    EXTREME = "Extreme"
    HIGH = "High"
    NOCOMPRESSION = "NoCompression"
    OPTIMAL = "Optimal"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

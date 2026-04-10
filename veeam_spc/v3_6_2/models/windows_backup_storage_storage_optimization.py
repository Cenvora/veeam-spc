from enum import Enum


class WindowsBackupStorageStorageOptimization(str, Enum):
    LAN512KB = "Lan512KB"
    LOCAL1MB = "Local1MB"
    LOCALLEGACY8MB = "LocalLegacy8Mb"
    LOCALPB4MB = "LocalPb4MB"
    UNKNOWN = "Unknown"
    WAN256KB = "Wan256KB"

    def __str__(self) -> str:
        return str(self.value)

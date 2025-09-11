from enum import Enum


class LinuxBackupStorageBlockSize(str, Enum):
    LAN512KB = "Lan512KB"
    LOCAL1MB = "Local1MB"
    LOCALPB4MB = "LocalPb4MB"
    UNKNOWN = "Unknown"
    WAN256KB = "Wan256KB"

    def __str__(self) -> str:
        return str(self.value)

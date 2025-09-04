from enum import Enum


class WindowsBackupStorageStorageOptimization(str, Enum):
    LAN = "Lan"
    LOCAL = "Local"
    LOCAL100TBPLUSBACKUP = "Local100TbPlusBackup"
    LOCALLEGACY8MB = "LocalLegacy8Mb"
    UNKNOWN = "Unknown"
    WAN = "Wan"

    def __str__(self) -> str:
        return str(self.value)

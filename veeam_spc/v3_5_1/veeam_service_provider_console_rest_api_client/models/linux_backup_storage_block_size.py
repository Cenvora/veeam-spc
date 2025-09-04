from enum import Enum


class LinuxBackupStorageBlockSize(str, Enum):
    LAN = "Lan"
    LOCAL = "Local"
    LOCAL100TBPLUSBACKUP = "Local100TbPlusBackup"
    UNKNOWN = "Unknown"
    WAN = "Wan"

    def __str__(self) -> str:
        return str(self.value)

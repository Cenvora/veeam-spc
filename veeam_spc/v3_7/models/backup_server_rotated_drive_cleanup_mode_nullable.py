from enum import Enum


class BackupServerRotatedDriveCleanupModeNullable(str, Enum):
    CLEARBACKUPFOLDER = "ClearBackupFolder"
    CLEARREPOSITORYFOLDER = "ClearRepositoryFolder"
    DISABLED = "Disabled"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

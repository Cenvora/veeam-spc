from enum import Enum


class LinuxBackupTargetTargetType(str, Enum):
    BACKUPREPOSITORY = "BackupRepository"
    CLOUDREPOSITORY = "CloudRepository"
    EXTERNALREPOSITORY = "ExternalRepository"
    LOCALFOLDER = "LocalFolder"
    SHAREDFOLDER = "SharedFolder"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

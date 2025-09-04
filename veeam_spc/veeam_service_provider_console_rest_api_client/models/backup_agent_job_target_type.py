from enum import Enum


class BackupAgentJobTargetType(str, Enum):
    BACKUPREPOSITORY = "BackupRepository"
    CLOUDREPOSITORY = "CloudRepository"
    LOCALFOLDER = "LocalFolder"
    SHAREDFOLDER = "SharedFolder"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

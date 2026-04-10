from enum import Enum


class BackupAgentJobTargetTypeDetailed(str, Enum):
    BACKUPREPOSITORY = "BackupRepository"
    CLOUDREPOSITORY = "CloudRepository"
    LOCALFOLDER = "LocalFolder"
    SHAREDFOLDER = "SharedFolder"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

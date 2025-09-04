from enum import Enum


class WindowsBackupTargetTargetType(str, Enum):
    BACKUPREPOSITORY = "BackupRepository"
    CLOUDREPOSITORY = "CloudRepository"
    LOCALFOLDER = "LocalFolder"
    OBJECTSTORAGE = "ObjectStorage"
    ONEDRIVE = "OneDrive"
    SHAREDFOLDER = "SharedFolder"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

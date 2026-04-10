from enum import Enum


class Vb365BackupJobBackupType(str, Enum):
    ENTIREORGANIZATION = "EntireOrganization"
    SELECTEDITEMS = "SelectedItems"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

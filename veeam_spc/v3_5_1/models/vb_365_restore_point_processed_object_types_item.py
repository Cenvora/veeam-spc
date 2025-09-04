from enum import Enum


class Vb365RestorePointProcessedObjectTypesItem(str, Enum):
    ARCHIVE = "Archive"
    MAILBOX = "Mailbox"
    ONEDRIVE = "OneDrive"
    SITE = "Site"
    TEAM = "Team"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

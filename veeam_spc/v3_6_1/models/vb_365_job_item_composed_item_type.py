from enum import Enum


class Vb365JobItemComposedItemType(str, Enum):
    GROUP = "Group"
    ONEDRIVEFOLDERS = "OneDriveFolders"
    PARTIALORGANIZATION = "PartialOrganization"
    PERSONALSITES = "PersonalSites"
    SITE = "Site"
    TEAM = "Team"
    UNKNOWN = "Unknown"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)

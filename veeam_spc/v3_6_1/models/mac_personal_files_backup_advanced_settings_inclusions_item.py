from enum import Enum


class MacPersonalFilesBackupAdvancedSettingsInclusionsItem(str, Enum):
    APPLICATIONDATA = "ApplicationData"
    DESKTOP = "Desktop"
    DOCUMENTS = "Documents"
    DOWNLOADS = "Downloads"
    FAVORITES = "Favorites"
    LIBRARY = "Library"
    MUSIC = "Music"
    OTHERFILESANDFOLDERS = "OtherFilesAndFolders"
    PICTURES = "Pictures"
    UNKNOWN = "Unknown"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)

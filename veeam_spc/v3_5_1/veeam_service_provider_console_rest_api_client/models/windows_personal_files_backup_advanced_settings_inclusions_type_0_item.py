from enum import Enum


class WindowsPersonalFilesBackupAdvancedSettingsInclusionsType0Item(str, Enum):
    APPLICATIONDATA = "ApplicationData"
    DESKTOP = "Desktop"
    DOCUMENTS = "Documents"
    DOWNLOADS = "Downloads"
    FAVORITES = "Favorites"
    MUSIC = "Music"
    OTHERFILESANDFOLDERS = "OtherFilesAndFolders"
    PICTURES = "Pictures"
    UNKNOWN = "Unknown"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)

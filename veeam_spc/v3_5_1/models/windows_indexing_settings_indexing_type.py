from enum import Enum


class WindowsIndexingSettingsIndexingType(str, Enum):
    EVERYTHING = "Everything"
    EXCEPTSPECIFIEDFOLDERS = "ExceptSpecifiedFolders"
    NONE = "None"
    SPECIFIEDFOLDERS = "SpecifiedFolders"

    def __str__(self) -> str:
        return str(self.value)

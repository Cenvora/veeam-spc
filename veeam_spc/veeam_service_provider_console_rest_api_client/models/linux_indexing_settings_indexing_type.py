from enum import Enum


class LinuxIndexingSettingsIndexingType(str, Enum):
    EVERYFOLDERS = "EveryFolders"
    EXCEPTSPECIFIEDFOLDERS = "ExceptSpecifiedFolders"
    NONE = "None"
    SPECIFIEDFOLDERS = "SpecifiedFolders"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class WindowsPersonalFilesBackupAdvancedSettingsExclusionsType0Item(str, Enum):
    ROAMINGUSERS = "RoamingUsers"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

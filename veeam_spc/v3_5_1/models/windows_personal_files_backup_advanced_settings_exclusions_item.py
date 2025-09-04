from enum import Enum


class WindowsPersonalFilesBackupAdvancedSettingsExclusionsItem(str, Enum):
    ROAMINGUSERS = "RoamingUsers"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

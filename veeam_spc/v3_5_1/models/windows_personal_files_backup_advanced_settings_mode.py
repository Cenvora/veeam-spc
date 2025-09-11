from enum import Enum


class WindowsPersonalFilesBackupAdvancedSettingsMode(str, Enum):
    ALL = "All"
    GRANULAR = "Granular"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

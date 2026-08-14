from enum import Enum


class BackupServerObjectStorageImmutabilityImmutabilityMode(str, Enum):
    REPOSITORYSETTINGS = "RepositorySettings"
    RETENTIONSETTINGS = "RetentionSettings"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

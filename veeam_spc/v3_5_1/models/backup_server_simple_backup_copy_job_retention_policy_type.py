from enum import Enum


class BackupServerSimpleBackupCopyJobRetentionPolicyType(str, Enum):
    GFS = "GFS"
    NONE = "None"
    SIMPLE = "Simple"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

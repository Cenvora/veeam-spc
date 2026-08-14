from enum import Enum


class BackupServerImmediateBackupCopyJobRetentionPolicyType(str, Enum):
    GFS = "GFS"
    NONE = "None"
    SIMPLE = "Simple"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

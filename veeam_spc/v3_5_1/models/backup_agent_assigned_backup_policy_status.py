from enum import Enum


class BackupAgentAssignedBackupPolicyStatus(str, Enum):
    APPLIED = "Applied"
    APPLYING = "Applying"
    FAILED = "Failed"
    REMOVING = "Removing"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

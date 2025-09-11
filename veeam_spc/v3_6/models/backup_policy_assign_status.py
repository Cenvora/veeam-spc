from enum import Enum


class BackupPolicyAssignStatus(str, Enum):
    APPLYING = "Applying"
    ASSIGNED = "Assigned"
    CUSTOM = "Custom"
    DELETING = "Deleting"
    FAILEDTOAPPLY = "FailedToApply"
    OUTDATED = "Outdated"
    UNASSIGNED = "Unassigned"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

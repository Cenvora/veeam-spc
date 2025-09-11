from enum import Enum


class PulseLicenseAssignStatus(str, Enum):
    ASSIGNED = "Assigned"
    ASSIGNING = "Assigning"
    EDITING = "Editing"
    FAILEDTOASSIGN = "FailedToAssign"
    FAILEDTOEDIT = "FailedToEdit"
    FAILEDTOREVOKE = "FailedToRevoke"
    NOTASSIGNED = "NotAssigned"
    REVOKING = "Revoking"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

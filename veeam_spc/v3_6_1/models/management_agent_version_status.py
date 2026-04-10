from enum import Enum


class ManagementAgentVersionStatus(str, Enum):
    OUTOFDATE = "OutOfDate"
    PATCHAVAILABLE = "PatchAvailable"
    UNKNOWN = "Unknown"
    UPTODATE = "UpToDate"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BackupFailoverPlanStatus(str, Enum):
    COMPLETED = "Completed"
    FAILED = "Failed"
    INPROGRESS = "InProgress"
    INUNDOPROGRESS = "InUndoProgress"
    READY = "Ready"
    SUCCESS = "Success"
    UNDOFAILED = "UndoFailed"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

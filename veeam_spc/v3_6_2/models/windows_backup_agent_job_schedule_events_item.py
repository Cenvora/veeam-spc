from enum import Enum


class WindowsBackupAgentJobScheduleEventsItem(str, Enum):
    ATLOCK = "AtLock"
    ATLOGOFF = "AtLogoff"
    UNKNOWN = "Unknown"
    WHENBACKUPTARGETISCONNECTED = "WhenBackupTargetIsConnected"

    def __str__(self) -> str:
        return str(self.value)

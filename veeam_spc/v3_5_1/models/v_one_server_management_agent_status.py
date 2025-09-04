from enum import Enum


class VOneServerManagementAgentStatus(str, Enum):
    ERROR = "Error"
    FAILEDTOUPDATE = "FailedToUpdate"
    HEALTHY = "Healthy"
    INACCESSIBLE = "Inaccessible"
    INSTALLATION = "Installation"
    RESTARTING = "Restarting"
    UNKNOWN = "Unknown"
    UPDATING = "Updating"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

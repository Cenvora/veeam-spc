from enum import Enum


class ManagementAgentTaskStatus(str, Enum):
    CANCELED = "Canceled"
    FAILED = "Failed"
    RUNNING = "Running"
    SCHEDULED = "Scheduled"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

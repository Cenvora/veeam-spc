from enum import Enum


class BackupAgentJobStatus(str, Enum):
    FAILED = "Failed"
    NONE = "None"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPING = "Stopping"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

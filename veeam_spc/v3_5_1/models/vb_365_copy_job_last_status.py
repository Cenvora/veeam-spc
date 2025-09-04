from enum import Enum


class Vb365CopyJobLastStatus(str, Enum):
    DELETING = "Deleting"
    DISCONNECTED = "Disconnected"
    FAILED = "Failed"
    NOTCONFIGURED = "NotConfigured"
    QUEUED = "Queued"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

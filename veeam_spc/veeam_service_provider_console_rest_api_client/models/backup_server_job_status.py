from enum import Enum


class BackupServerJobStatus(str, Enum):
    DISABLING = "Disabling"
    ENABLING = "Enabling"
    FAILED = "Failed"
    IDLE = "Idle"
    NONE = "None"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPING = "Stopping"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WAITINGREPOSITORY = "WaitingRepository"
    WAITINGTAPE = "WaitingTape"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

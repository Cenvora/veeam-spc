from enum import Enum


class PublicCloudPolicySessionStatusReadonly(str, Enum):
    DELETING = "Deleting"
    DISABLING = "Disabling"
    ENABLING = "Enabling"
    FAILED = "Failed"
    IDLE = "Idle"
    NONE = "None"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPING = "Stopping"
    SUCCESS = "Success"
    WAITINGREPOSITORY = "WaitingRepository"
    WAITINGTAPE = "WaitingTape"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)

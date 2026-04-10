from enum import Enum


class PublicCloudPolicyStatus(str, Enum):
    DELETING = "Deleting"
    IDLE = "Idle"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPING = "Stopping"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

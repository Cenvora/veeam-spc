from enum import Enum


class PublicCloudPolicyStatus(str, Enum):
    DELETING = "Deleting"
    NONE = "None"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPING = "Stopping"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class EPublicCloudObjectCreatingState(str, Enum):
    CREATING = "Creating"
    FAILED = "Failed"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)

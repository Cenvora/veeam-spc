from enum import Enum


class ScheduledDeploymentTaskType(str, Enum):
    DEPLOYVBR = "deployVbr"
    PATCHVBR = "patchVbr"
    UNKNOWN = "unknown"
    UPGRADEVBR = "upgradeVbr"

    def __str__(self) -> str:
        return str(self.value)

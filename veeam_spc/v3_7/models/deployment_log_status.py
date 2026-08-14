from enum import Enum


class DeploymentLogStatus(str, Enum):
    FAILED = "failed"
    SUCCESS = "success"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)

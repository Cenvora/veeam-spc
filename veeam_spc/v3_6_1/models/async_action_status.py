from enum import Enum


class AsyncActionStatus(str, Enum):
    CANCELED = "canceled"
    FAILED = "failed"
    RUNNING = "running"
    SUCCEED = "succeed"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ResponseErrorType(str, Enum):
    LOGICAL = "logical"
    RETRYABLELOGICAL = "retryableLogical"
    SECURITY = "security"
    TRANSPORT = "transport"
    UNSPECIFIED = "unspecified"

    def __str__(self) -> str:
        return str(self.value)

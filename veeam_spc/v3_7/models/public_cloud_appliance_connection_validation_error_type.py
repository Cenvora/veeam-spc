from enum import Enum


class PublicCloudApplianceConnectionValidationErrorType(str, Enum):
    CERTIFICATE = "Certificate"
    NONE = "None"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)

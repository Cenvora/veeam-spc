from enum import Enum


class ConsoleLicenseCloudConnect(str, Enum):
    ENTERPRISE = "Enterprise"
    NO = "No"
    UNKNOWN = "Unknown"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
